#!/usr/bin/env python
#Purpose: Test #windows diffs for pytest

import os
from subprocess import getstatusoutput, getoutput
import subprocess


prg = 'tiny1.py'

"""Both versions of the tests below work, commented or not"""
# --------------------------------------------------
#def test_usage():
 #   """usage"""
  #  for flag in ['-h', '--help']:
   #     stdout = subprocess.run(['python', 'hello.py', flag], capture_output=True, text=True)
    #assert stdout.stdout.lower().startswith('usage')
    #assert stdout.returncode == 0

def test_usage():
    """usage"""
    for flag in ['-h', '--help']:
        rv, statusout = getstatusoutput(f'python {prg} {flag}')
    assert statusout.lower().startswith('usage')
    assert rv == 0

# --------------------------------------------------

def test_input():
    """test for input"""

    for val in ['Universe', 'Multiverse']:
        for option in ['-n', '--name']:
            out = subprocess.run(['python', 'tiny1.py', option, val], capture_output=True, text=True)
    assert out.returncode == 0, "return code != to 0"
    assert out.stdout.strip() == f'Hello, {val}!', "assertion fail strip value not correct"


test_usage()
test_input()

