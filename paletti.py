from collections import namedtuple
from colorama import init, Fore, Back, Style
import colorific
import cv2
import json
import numpy as np
from PIL import Image, ImageDraw
import requests
import os.path as osp
from sklearn.cluster import KMeans
import sys

init()

Palette = namedtuple('Palette', 'colors percent')


def kmeans_palette(imfile, k=5):
    """ Extract a color palette using k-means clustering. """
    origimg = cv2.cvtColor(cv2.imread(imfile), cv2.COLOR_BGR2LAB)
    img = origimg.astype('float64') / 255.

    w, h, d = tuple(img.shape)
    assert d == 3
    imarr = np.reshape(img, (w * h, d))

    # Perform k-means clustering
    kmeans = KMeans(n_clusters=k, n_jobs=-1).fit(imarr)
    labels = kmeans.predict(imarr)
    maincolors = kmeans.cluster_centers_
    maincolors = (maincolors.reshape((k, 1, 3)) * 255).astype('uint8')
    maincolors = cv2.cvtColor(maincolors, cv2.COLOR_LAB2RGB)
    maincolors = maincolors.astype('float64') / 255.

    # Compute percentage of each main color
    percent, _ = np.histogram(labels, bins=len(maincolors), normed=True)
    percent /= float(percent.sum())

    return Palette(maincolors.squeeze(), percent)


def colorific_palette(imfile, k=5):
    """ Extract a color palette using colorific. """
    result = np.asarray(colorific.extract_colors(imfile, max_colors=k)[0])
    maincolors = np.asarray([list(c) for c in result[:, 0]]) / 255.
    percent = result[:, 1] / np.sum(result[:, 1])
    return Palette(maincolors, percent)


def pil_palette(imfile, k=5):
    """ Extract a color palette using PIL. """
    rsize = 150
    image = Image.open(imfile)
    image = image.resize((rsize, rsize))
    result = image.convert('P', palette=Image.ADAPTIVE, colors=k)
    result.putalpha(0)
    res = result.getcolors(rsize * rsize)

    maincolors = np.asarray([list(x[1][:-1]) for x in res]) / 255.
    percent = np.asarray([x[0] for x in res], dtype='float')
    percent /= percent.sum()

    return Palette(maincolors, percent)


def pictaculous_palette(imfile):
    """ Extract a color palette using the pictaculous API. """
    endpoint = 'http://pictaculous.com/api/1.0/'
    r = requests.post(endpoint, {'image': open(imfile, 'rb').read()})
    data = json.loads(r.text)
    maincolors = data['info']['colors']
    maincolors = np.asarray([hex2rgb(c) for c in maincolors]) / 255.
    return Palette(maincolors, [1.0 / len(maincolors)] * len(maincolors))


def hex2rgb(hexcolor):
    value = hexcolor.lstrip('#') if hexcolor.startswith('#') else hexcolor
    lv = len(value)
    return [int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3)]


def rgb2hex(rgb):
    return '#%02x%02x%02x' % rgb


def complementary_color(incolor):
    """ Compute the complementary RGB color. """
    if incolor.startswith('#'):
        incolor = incolor[1:]
    rgb = (incolor[0:2], incolor[2:4], incolor[4:6])
    comp = ['02%X' % (255 - int(a, 16)) for a in rgb]
    return comp.join()


def get_palette(fname, k=5, method='k-means', color_format='rgb'):
    """ Extract a color palette from an image using the specified method. """
    if method == 'k-means':
        return kmeans_palette(fname, k=k)
    elif method == 'colorific':
        return colorific_palette(fname, k=k)
    elif method == 'pil':
        return pil_palette(fname, k=k)
    elif method == 'pictaculous':
        return pictaculous_palette(fname)


def print_palette(fname, palette, method, color_format):
    """ Print palette colors. """
    maincolors = [(np.asarray(c) * 255).astype('uint8')
                  for c in palette.colors]
    print('Color palette of ' + Fore.CYAN + Style.BRIGHT + '{}'.format(fname)
          + Style.RESET_ALL + ' using ' + Back.BLUE + Fore.WHITE + Style.BRIGHT
          + '{}'.format(method) + Style.RESET_ALL + ':')
    if color_format == 'hex':
        maincolors = [rgb2hex(tuple(c)) for c in maincolors]
    print '\n'
    for i, c in enumerate(maincolors):
        print('\t' + '{} '.format(color_format) + Fore.BLACK + Back.WHITE +
              Style.BRIGHT + str(c) + Style.RESET_ALL + '\t{:.2}'.format(
                palette.percent[i]))
    print '\n'
    sys.stdout.flush()


def create_palette(palette, outname='palette.png', save=True, size=(300, 80)):
    """ Create (and save) palette. """
    width, height = size
    img = Image.new('RGB', size)
    draw = ImageDraw.Draw(img)
    maincolors = [(np.array(c) * 255).astype('uint8') for c in palette.colors]
    start_x = 0
    for c, p in zip(maincolors, palette.percent):
        end_x = start_x + (p * width)
        (x1, y1) = (start_x, 0)
        (x2, y2) = (end_x, height-1)
        draw.rectangle([(x1, y1), (x2, y2)], fill=tuple(c))
        start_x = end_x
    if not save:
        return img
    if not outname.endswith('.png'):
        outname = '{}_palette.png'.format(osp.splitext(outname)[0])
    img.save(outname, "PNG")
