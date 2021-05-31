#!/usr/bin/env python

#Purpose testing:

import argparse

parser = argparse.ArgumentParser(description='Say hello')
parser.add_argument('name', help='Name to greet')
args = parser.parse_args()
name = args.name

print("Hello, " + name + "!")
