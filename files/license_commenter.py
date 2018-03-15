#!/usr/bin/env python3
# -----
# MIT License
#
# Copyright 2017 Sequencing Analysis Support Core - Leiden University Medical Center
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# .....
import argparse
import os
'''
Copyright 2017 Ruben Vorderman
Copyright 2017 SASC Group (LUMC)
'''


def argument_parser():
    parser = argparse.ArgumentParser(prog='License Commenter',
                                     description='Parses a text file and returns a commented out license header')
    parser.add_argument('-i', '--input', required=True, type=str, help='File containing the header without comments')
    parser.add_argument('-o', '--output')
    parser.add_argument('-p', '--prefix', default='# ')
    parser.add_argument('-s', '--suffix', default='')
    parser.add_argument('--overwrite', action='store_true')
    parser.add_argument('--whitespace_strip_off', action='store_true')
    return parser.parse_args()


def main():
    args = argument_parser()

    # Open input_file in read mode
    try:
        with open(args.input, 'r') as input_file:

            # create output filename if does not exist
            if not args.output:
                args.output = os.path.splitext(os.path.basename(args.input))[0] + '.commented.txt'

            # Check if output file can be written.
            if os.path.exists(args.output):
                if not args.overwrite:
                    raise FileExistsError(args.output)
                else:
                    if os.path.isdir(args.output):
                        raise IsADirectoryError(args.output)
                    if os.path.isfile:
                        os.remove(args.output)


            # Write to output file
            with open(args.output, 'w') as output_file:
                for line in input_file.readlines():
                    output_line = args.prefix + line.replace('\n','') + args.suffix
                    if not args.whitespace_strip_off:
                        output_line = output_line.strip()
                    output_file.write( output_line + '\n')

    except FileNotFoundError:
        raise FileNotFoundError(args.input)


if __name__ == '__main__':
    main()
