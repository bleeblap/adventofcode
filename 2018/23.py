#!/usr/bin/env python

import sys
import copy
import re
import math
from heapq import heappush, heappop


infile = open('23.in','r').read()

infile2 = '''pos=<0,0,0>, r=4 
pos=<1,0,0>, r=1
pos=<4,0,0>, r=3
pos=<0,2,0>, r=1
pos=<0,5,0>, r=3
pos=<0,0,3>, r=1
pos=<1,1,1>, r=1
pos=<1,1,2>, r=1
pos=<1,3,1>, r=1'''

infile2 = '''pos=<10,12,12>, r=2
pos=<12,14,12>, r=2
pos=<16,12,12>, r=4
pos=<14,14,14>, r=6
pos=<50,50,50>, r=200
pos=<10,10,10>, r=5'''

def man_dist(b1, b2):
    return abs(b1[0]-b2[0]) + abs(b1[1]-b2[1]) + abs(b1[2]-b2[2])

def math_dist(b1, b2):
    return math.sqrt((b2[0]-b1[0])**2 + (b2[1]-b1[1])**2 + (b2[2]-b1[2])**2)

nanobots = []
for line in infile.split('\n'):
    x,y,z,r = map(int, [x for x in re.findall('-?\d+', line)])
    nanobots.append((x,y,z,r))

maxr = max([n[3] for n in nanobots])
strongbot = [n for n in nanobots if n[3] == maxr][0]
#print maxr, strongbot, len(nanobots)

inrange = [n for n in nanobots if man_dist(strongbot, n) <= maxr]
print 'Part1',len(inrange)

def calc_bots(x,y,z):
    global nanobots
    inrange = 0
    for bot in nanobots:
        if man_dist(bot, (x,y,z)) <= bot[3]:
            inrange += 1
    return inrange


minx = min([n[0] for n in nanobots])
maxx = max([n[0] for n in nanobots])
miny = min([n[1] for n in nanobots])
maxy = max([n[1] for n in nanobots])
minz = min([n[2] for n in nanobots])
maxz = max([n[2] for n in nanobots])

# Next strategy is to start with a huge cube and the divide into 8 sections
# each iteration and count bots overlapping with each cube

# Since man_dist, this should work?
def bot_cube_overlap(bot, cube):
    d = 0
    if bot[0] < cube[0]: d += cube[0]-bot[0]
    if bot[0] > cube[0]+cube[3]-1: d += bot[0]-(cube[0]+cube[3]-1)
    if bot[1] < cube[1]: d += cube[1]-bot[1]
    if bot[1] > cube[1]+cube[3]-1: d += bot[1]-(cube[1]+cube[3]-1)
    if bot[2] < cube[2]: d += cube[2]-bot[2]
    if bot[2] > cube[2]+cube[3]-1: d += bot[2]-(cube[2]+cube[3]-1)
    return d <= bot[3]


def subdiv_cube(cube):
    newr = cube[3]/2
    return [(cube[0], cube[1], cube[2], newr),
        (cube[0]+newr, cube[1], cube[2], newr),
        (cube[0], cube[1]+newr, cube[2], newr),
        (cube[0]+newr, cube[1]+newr, cube[2], newr),
        (cube[0], cube[1], cube[2]+newr, newr),
        (cube[0]+newr, cube[1], cube[2]+newr, newr),
        (cube[0], cube[1]+newr, cube[2]+newr, newr),
        (cube[0]+newr, cube[1]+newr, cube[2]+newr, newr)]

def score_cube(cube):
    global nanobots
    overlap = 0
    for bot in nanobots:
        if bot_cube_overlap(bot,cube):
            overlap += 1
    return overlap

pq = []
r = 1
# Let r be a power of 2 so we can just /= 2 on subdivide without worrying about rounding
while r < max(maxx-minx, maxy-miny, maxz-minz):
    r *= 2

# Start with huge cube that should include every nanobot
heappush(pq, (-len(nanobots), 0, (minx, miny, minz, r)))

while True:
    score,d,c = heappop(pq)
    #print '***',score,c
    if c[3] == 1:
        #print calc_bots(c[0],c[1],c[2])
        print 'Part2',man_dist(c,(0,0,0))
        break
    for x in subdiv_cube(c):
        score = score_cube(x)
        if score > 0: # Safe to skip empty
            d = man_dist((min(c[0],c[0]+c[3]),min(c[1],c[1]+c[3]),min(c[2],c[2]+c[3])),(0,0,0))
            heappush(pq, (-score, d, x))


