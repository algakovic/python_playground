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
def test_input():
    """test for input"""

    for val in ['Universe', 'Multiverse']:
        for option in ['-n', '--name']:
            out = subprocess.run(['python', 'tiny1.py', option, val], capture_output=True, text=True)
    assert out.returncode == 0, "return code != to 0"
    assert out.stdout.strip() == f'Hello, {val}!', "assertion fail strip value not correct"

test_input()
