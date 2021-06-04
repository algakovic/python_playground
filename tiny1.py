#!/usr/bin/env python
'''
Author: Alek Gakovic
Email: algakovic@gmail.com
Purpose: testing
'''

import argparse


def get_args():
    '''
    gets arguments from argparse
    '''
    parser = argparse.ArgumentParser(description='Say hello')
    parser.add_argument('-n',
                        '--name',
                        metavar="name",
                        default='World',
                        help='Name to greet')
    return parser.parse_args()


def main():
    '''
    Main function runs script
    '''
    args = get_args()
    name = args.name
    print("Hello, " + name + "!")


if __name__ == '__main__':
    main()
