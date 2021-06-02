#!/usr/bin/env python
#Purpose: Test #windows diffs for pytest


import subprocess


# --------------------------------------------------
def test_usage():
   """usage"""

for flag in ['-h', '--help']:
    stdout = subprocess.run(['python', 'tiny1.py', flag], capture_output=True, text=True)
    
assert stdout.stdout.lower().startswith('usage')
assert stdout.returncode == 0
# --------------------------------------------------

test_usage()

