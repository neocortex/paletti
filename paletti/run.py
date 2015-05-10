import optparse
import sys
from tempfile import NamedTemporaryFile

import requests

from config import METHOD, NUM_COLORS
from paletti import create_palette, get_palette, print_palette


class PalettiApp(object):
    def __init__(self):
        self.parser = self.get_parser()

    def get_parser(self):
        usage = 'python %prog [options] IMAGE_FILE'
        parser = optparse.OptionParser(usage=usage)

        parser.add_option(
            '-k',
            '--num-colors',
            action='store',
            dest='num_colors',
            type='int',
            default=NUM_COLORS,
            help='The maximum number of colors per palette [{}].'
                 .format(NUM_COLORS))
        parser.add_option(
            '-m',
            '--method',
            action='store',
            dest='method',
            default=METHOD,
            help="The method used to extract the color palette. Can be 'k-"
                 "means', 'colorific', 'pil', or 'pictaculous'. Default is 'k-"
                 "means'. In addition to the color palette, if 'k-means' is "
                 "chosen, a color-reduced image with the specified number of "
                 "colors is saved to disk.".format(METHOD))
        parser.add_option(
            '-u',
            '--url',
            action='store_true',
            dest='url',
            default=False,
            help="Image to be analyzed is a URL.")
        parser.add_option(
            '-o',
            '--output',
            action='store_true',
            dest='save_palette',
            default=False,
            help="Plot and store the palette in an image file.")

        return parser

    def run(self):
        argv = sys.argv[1:]
        options, args = self.parser.parse_args(argv)
        if args:
            for fname in args:
                try:
                    if options.url:
                        response = requests.get(fname)
                        f = NamedTemporaryFile(delete=False)
                        f.write(response.content)
                        f.close()
                        fname = f.name
                    palette = get_palette(
                        fname, k=options.num_colors, method=options.method)
                except Exception as e:
                    print 'Skipping \'{}\': {}.'.format(fname, e)
                    continue
                print_palette(fname, palette, method=options.method)
                if options.save_palette:
                    create_palette(palette, outname=fname)
        else:
            print 'No image file specified --'
            print self.parser.get_usage()
        sys.exit(1)


def main():
    app = PalettiApp()
    app.run()


if __name__ == '__main__':
    main()
