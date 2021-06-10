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
    word = args.object
    article = 'an' if word[0].lower() in 'aeiou' else 'a'

    print(f"Ahoy, Captain, {article} {word} off the larboard bow!")
    # if args.object.capitalize().startswith(tuple(vowels)):
    #     print(f'Ahoy, Captain, an {args.object} off the larboard bow!')
    # else:
    #     print(f'Ahoy, Captain, a {args.object} off the larboard bow!')


# --------------------------------------------------
if __name__ == '__main__':
    main()
