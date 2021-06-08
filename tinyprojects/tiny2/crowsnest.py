#!/usr/bin/env python
"""
Author : ArkSealand>
Date   : 2021-06-08
Purpose: Inform the captain
"""

import argparse


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
    print(f'Captain theres a {args.object} on the larbord bow')


# --------------------------------------------------
if __name__ == '__main__':
    main()
