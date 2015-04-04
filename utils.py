import numpy as np


def rgb2lab(image):
    """ Transforms an RGB-image to a LAB-image. """
    return xyz2lab(rgb2xyz(image))


def lab2rgb(image):
    """ Transforms a LAB-image to an RGB-image. """
    return xyz2rgb(lab2xyz(image))


def rgb2xyz(image):
    """ Transforms an RGB-mage to a XYZ-image. """
    image = np.array(image, dtype='float64')
    r = image[:, :, 0] / 255.
    g = image[:, :, 1] / 255.
    b = image[:, :, 2] / 255.

    ri = r > .04045
    r[ri] = ((r[ri] + .055) / 1.055) ** 2.4
    r[~ri] = r[~ri] / 12.92
    gi = g > .04045
    g[gi] = ((g[gi] + .055) / 1.055) ** 2.4
    g[~gi] = g[~gi] / 12.92
    bi = b > .04045
    b[bi] = ((b[bi] + .055) / 1.055) ** 2.4
    b[~bi] = b[~bi] / 12.92

    r *= 100.
    g *= 100.
    b *= 100.

    x = r * .4124 + g * .3576 + b * .1805
    y = r * .2126 + g * .7152 + b * .0722
    z = r * .0193 + g * .1192 + b * .9505

    return np.transpose(np.array([x, y, z]), (1, 2, 0))


def xyz2rgb(image):
    """ Transforms a XYZ-image to an RGB-image. """
    x = image[:, :, 0] / 100.
    y = image[:, :, 1] / 100.
    z = image[:, :, 2] / 100.

    var_R = x * 3.2406 + y * -1.5372 + z * -0.4986
    var_G = x * -0.9689 + y * 1.8758 + z * 0.0415
    var_B = x * 0.0557 + y * -0.2040 + z * 1.0570

    def convert(var):
        i = var > 0.0031308
        var[i] = 1.055 * (var[i] ** (1 / 2.4)) - 0.055
        var[~i] = var[~i] * 12.92
        return var

    var_R = convert(var_R)
    var_G = convert(var_G)
    var_B = convert(var_B)

    var_R[var_R < 0] = 0
    var_B[var_B < 0] = 0
    var_G[var_G < 0] = 0

    var_R[var_R > 1] = 1
    var_B[var_B > 1] = 1
    var_G[var_G > 1] = 1

    R = var_R * 255
    G = var_G * 255
    B = var_B * 255

    return np.transpose(np.array([R, G, B], dtype='uint8'), (1, 2, 0))


def xyz2lab(image):
    """ Transforms a XYZ-image to a LAB-image. """
    var_X = image[:, :, 0] / 95.047
    var_Y = image[:, :, 1] / 100.
    var_Z = image[:, :, 2] / 108.883

    xi = var_X > .008856
    var_X[xi] = var_X[xi] ** (1. / 3.)
    var_X[~xi] = (7.787 * var_X[~xi]) + (16. / 116.)
    yi = var_Y > .008856
    var_Y[yi] = var_Y[yi] ** (1. / 3.)
    var_Y[~yi] = (7.787 * var_Y[~yi]) + (16. / 116.)
    zi = var_Z > .008856
    var_Z[zi] = var_Z[zi] ** (1. / 3.)
    var_Z[~zi] = (7.787 * var_Z[~zi]) + (16. / 116.)

    L = (116 * var_Y) - 16
    a = 500. * (var_X - var_Y)
    b = 200. * (var_Y - var_Z)

    return np.transpose(np.array([L, a, b]), (1, 2, 0))


def lab2xyz(image):
    """ Transforms a LAB-image to a XYZ-image. """
    var_Y = (image[:, :, 0] + 16.) / 116.
    var_X = image[:, :, 1] / 500. + var_Y
    var_Z = var_Y - image[:, :, 2] / 200.

    yi = var_Y > 0.2069
    var_Y[yi] = var_Y[yi] ** 3
    var_Y[~yi] = (var_Y[~yi] - 16. / 116.) / 7.787
    xi = var_X > 0.2069
    var_X[xi] = var_X[xi] ** 3
    var_X[~xi] = (var_X[~xi] - 16. / 116.) / 7.787
    zi = var_Z > 0.2069
    var_Z[zi] = var_Z[zi] ** 3
    var_Z[~zi] = (var_Z[~zi] - 16. / 116.) / 7.787

    X = 95.047 * var_X
    Y = 100. * var_Y
    Z = 108.883 * var_Z

    return np.transpose(np.array([X, Y, Z]), (1, 2, 0))


def hex2rgb(hexcolor):
    """ Convert a color in Hex format to RGB. """
    value = hexcolor.lstrip('#') if hexcolor.startswith('#') else hexcolor
    lv = len(value)
    return [int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3)]


def rgb2hex(rgb):
    """ Convert an RGB color to Hex format. """
    return '#%02x%02x%02x' % rgb
