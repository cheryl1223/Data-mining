#!/usr/bin/env python

import sys
import math
import hashlib
import random
N = 2 ** 32 # assume the no. of distinct items is at most N
e = 0.1#standard est. error
m = int((1.3/e)**2) # no. of substreams
print "m = ", m
R = [0] * m # the maximum of the bit-position of the rightmost 0
random.seed()
test = random.random()
for line in sys.stdin:
    line = line.strip()
    for word in line.split():
        h = hashlib.md5()
        h.update(word+str(test))   
        substream =int(h.hexdigest(),16) % m #hash word to a substream       
        v = (int(h.hexdigest(), 16) % N) + 1 # hash word to [1, N]
        bitpos = math.log(v & -v, 2) + 1 # rightmost 0 bit position
        if (R[substream] < bitpos):
            R[substream] = bitpos
alpha = ((math.gamma(-1 / float(m)) * (1 - 2 ** (1 / float(m))) / math.log(2))) ** -m
print "Loglog estimator: ", int(round(alpha* m * 2 ** (sum(R) / float(m))))

