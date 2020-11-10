#!/usr/bin/env python
import argparse
import sys
from translate.storage.tmx import tmxfile


def parse_args():
    parser = argparse.ArgumentParser(description='This script extracts \
                                     source and target sentences from \
                                     a tmx file.')
    parser.add_argument('-f', '--file', metavar='file', required=True,
                        help='tmx file from which to extrac the sentences.')
    parser.add_argument('-s', '--source', metavar='src_language',
                        required=True, help='source language.')
    parser.add_argument('-t', '--target', metavar='tgt_language',
                        required=True, help='target language.')
    parser.add_argument('-n', '--name', metavar='files_name', required=True,
                        help='name to use for creating the output files. \
                        files_name.src will contain the source sentences and \
                        files_name.tgt the target sentences.')

    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()

    try:
        with open(args.file, 'rb') as f:
            tmx_file = tmxfile(f, args.source, args.target)
    except OSError:
        sys.stderr.write('Error: ' + args.file + ' does not exist.\n')
        sys.exit(-1)
    except SyntaxError:
        sys.stderr.write('Error: ' + args.file + ' is not a tmx file.\n')
        sys.exit(-1)

    src = open(args.name + '.src', 'w')
    tgt = open(args.name + '.tgt', 'w')
    for node in tmx_file.unit_iter():
        try:
            src.write(node.gettarget(lang=args.source) + '\n')
        except TypeError:
            sys.stderr.write('Error: ' + args.source
                             + ' language not in file.\n')
            sys.exit(-1)
        try:
            tgt.write(node.gettarget(lang=args.target) + '\n')
        except TypeError:
            sys.stderr.write('Error: ' + args.target
                             + ' language not in file.\n')
            sys.exit(-1)
    src.close()
    tgt.close()
