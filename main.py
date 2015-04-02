import optparse
import sys

import config
from paletti import get_palette, print_palette, create_palette


class PalettiApp(object):
    def __init__(self):
        self.parser = self.get_parser()

    def get_parser(self):
        usage = 'python %prog [options]'
        parser = optparse.OptionParser(usage=usage)

        parser.add_option(
            '-k',
            '--num-colors',
            action='store',
            dest='num_colors',
            type='int',
            default=config.NUM_COLORS,
            help='The maximum number of colors to output per palette [{}]'
                 .format(config.NUM_COLORS))
        parser.add_option(
            '-o',
            '--output',
            action='store_true',
            dest='save_palette',
            default=False,
            help="Plot and store the palette in an image file")
        parser.add_option(
            '-m',
            '--method',
            action='store',
            dest='method',
            default=config.METHOD,
            help="The method used to extract the color palette [{}]".format(
                config.METHOD))

        return parser

    def run(self):
        argv = sys.argv[1:]
        options, args = self.parser.parse_args(argv)
        if args:
            for fname in args:
                try:
                    palette = get_palette(
                        fname, k=options.num_colors, method=options.method)
                except Exception as e:
                    print >> sys.stderr, fname, e
                    continue
                print_palette(fname, palette, method=options.method)
                if options.save_palette:
                    create_palette(palette, outname=fname)
            sys.exit(1)


def main():
    app = PalettiApp()
    app.run()


if __name__ == '__main__':
    main()
