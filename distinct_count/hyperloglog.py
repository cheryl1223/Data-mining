#!/usr/bin/env python

import sys
import math
import hashlib
import random
from scipy.integrate import quad

N = 2 ** 32 # assume the no. of distinct items is at most N
e = 0.05 #standard est. error
m = int((1.03/e)**2) # no. of substreams
print m
R = [0] * m # the maximum of the bit-position of the rightmost 0

def computeBeta(m): #compute beta
    integral = quad(lambda u : math.log((2+u)/(1+u),2) ** m, 0, float("inf"))
    return (m*integral[0]) ** -1

def estimate(R): #HyperLogLog estimator
    numerator = beta * (m **2)
    denomenator = 0
    for i in range(len(R)):
        denomenator += math.pow(2,-1*R[i])
    return float(numerator)/denomenator

random.seed()
test = random.random()
beta = computeBeta(m)
for line in sys.stdin:
    line = line.strip()
    for word in line.split():
        h = hashlib.md5()
        h.update(word+str(test))  #shuffle     
        substream =abs(hash(word)) % m #hash word to a substream
        v = (int(h.hexdigest(), 16) % N) + 1 # hash word to [1, N]
        bit = math.log(v & -v, 2) + 1 # rightmost 0 bit position
        if (R[substream] < bit):
            R[substream] = bit
print "Hyperloglog estimator: ", int(round(estimate(R)))

