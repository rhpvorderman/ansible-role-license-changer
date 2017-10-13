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
                    output_file.write(args.prefix + line.replace('\n','') + args.suffix + '\n')

    except FileNotFoundError:
        raise FileNotFoundError(args.input)


if __name__ == '__main__':
    main()
