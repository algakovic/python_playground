#!/usr/bin/env python
#Purpose: Test #windows diffs for pytest


import os
import subprocess
from subprocess import getstatusoutput, getoutput

prg = '.\hello.py'
# --------------------------------------------------
#def test_usage():
#   """usage"""

#   for flag in ['-h', '--help']:
#        print(subprocess.check_output(f'{prg}, {flag}'))
        


# --------------------------------------------------

#test_usage()

for flag in ['-h', '--help']:
    subprocess.check_output(f'{prg}, {flag}', shell=True)
