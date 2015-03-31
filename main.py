# -*- coding: utf-8 -*-
import sys
import optparse

import config
from paletti import get_palette, print_palette, save_palette


class PalettiApp(object):
    def __init__(self):
        self.parser = self.create_option_parser()

    def create_option_parser(self):
        usage = '\n'.join([
            "%prog [options]",
            "",
            "Extract color palettes from image. "])
        parser = optparse.OptionParser(usage)
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
            '-f',
            '--color-format',
            action='store',
            dest='color_format',
            default=config.COLOR_FORMAT,
            help="The output format of the colors [{}]".format(
                config.COLOR_FORMAT))
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
            for filename in args:
                try:
                    palette = get_palette(
                        filename,
                        k=options.num_colors,
                        method=options.method,
                        color_format=options.color_format)
                except Exception as e:
                    print >> sys.stderr, filename, e
                    continue
                print_palette(filename, palette, method=options.method,
                              color_format=options.color_format)
                if options.save_palette:
                    save_palette(filename, palette)
            sys.exit(1)


def main():
    app = PalettiApp()
    app.run()


if __name__ == '__main__':
    main()
