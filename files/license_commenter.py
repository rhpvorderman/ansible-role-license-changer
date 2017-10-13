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
        with open(args.input,'r') as input_file =
    except:
        raise FileNotFoundError(args.input)

    # Open output file in write mode
    # Check if output file already exists
    if not args.output:
        args.output = os.path.splitext(os.path.basename(args.input))[0] + '.commented.txt'
    if os.path.exists(args.output):
        if not args.overwrite:
            raise FileExistsError(args.output)
        else:
            if os.path.isfile:
                os.remove(args.output)
            if os.path.isdir:
                raise IsADirectoryError(args.output)
    with open(args.output,'w') as output_file

    for line in input_file.readlines():
        output_file.write( args.prefix + line + args.suffix + '\n' )


                os.
if __name__=='__main__':
    main()
