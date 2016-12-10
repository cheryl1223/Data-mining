#!/usr/bin/env python

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    #words = ''.join(c for c in line if c.isalpha() or c.isspace()).split()
    words = line.split()
    for word in words:
        print '%s\t%s' % (word, 1)
