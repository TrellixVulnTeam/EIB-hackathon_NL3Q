#!/home/galaxy/data/galaxy_17.09/galaxy-eib/.venv/bin/python2.7

"""
Read a file containing a 0 or 1 on each line (`feature_file`), output 
all lines from stdin for which that value was 1

TODO: no need to read the feature_file into memory here, just iterate in
      parallel.

usage: %prog feature_file < ...
"""

import psyco_full

import sys

def __main__():

    feature_file = sys.argv[1]

    if len( sys.argv ) > 2:
        match = int( sys.argv[2] )
    else:
        match = 1
    
    feature_vector = [ int( line ) for line in file( feature_file ) ]

    for index, line in enumerate( sys.stdin ):
        if feature_vector[ index ] == match: print line,

if __name__ == "__main__": __main__()
