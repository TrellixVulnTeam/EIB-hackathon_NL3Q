#!/home/galaxy/data/galaxy_17.09/.venv/bin/python2.7

"""
Script to select random lines from a file. Reads entire file into
memory!

TODO: Replace this with a more elegant implementation.
"""

import sys
import random

ndesired = int( sys.argv[1] )

for line in random.sample( sys.stdin.readlines(), ndesired ):
    print line,
