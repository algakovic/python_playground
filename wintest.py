#!/usr/bin/env python
#Purpose: Test #windows diffs for pytest


import os
import subprocess
from subprocess import getstatusoutput, getoutput

# --------------------------------------------------
def test_usage():
   """usage"""

for flag in ['-h', '--help']:
    stdout = subprocess.run(['python', 'tiny1.py', flag])
print(stdout)


# --------------------------------------------------

test_usage()

