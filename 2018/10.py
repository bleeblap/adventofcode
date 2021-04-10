#!/usr/bin/env python

import sys
import copy
from blist import blist
import matplotlib.pyplot as plt

infile = open('10.in','r').read()

data = []
for l in infile.split('\n'):
    e = {}
    e['x'] = int(l.split('<')[1].split(',')[0])
    e['y'] = int(l.split(',')[1].split('>')[0])
    e['dx'] = int(l.split('<')[2].split(',')[0])
    e['dy'] = int(l.split(',')[2].split('>')[0])
    data.append(e)

round = 1
while True:
    for e in data:
        e['x'] += e['dx']
        e['y'] += e['dy']
    x = [e['x'] for e in data]
    y = [-e['y'] for e in data]
    if max(x) < 200 and max(y) < 200:
        print round
        plt.scatter(x,y)
        plt.show()
    round += 1

# Run and look at the images until you see the letters
# Part1 RECLRNZE
# Part2 10007
