#!/usr/bin/env python
"""
Author : ArkSealand>
Date   : 2021-06-08
Purpose: Inform the captain
"""

import argparse

vowels = ('A', 'E', 'I', 'O', 'U')
# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='name the object sighted',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('object',
                        metavar='object',
                        help='name the object sighted')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    if args.object.capitalize().startswith(tuple(vowels)):
        print(f'Ahoy, Captain an {args.object.capitalize()} has been spotted on the larbord bow')
    else:
        print(f'Ahoy Captain a {args.object.capitalize()} has been spotted on the Larbord bow!')


# --------------------------------------------------
if __name__ == '__main__':
    main()
