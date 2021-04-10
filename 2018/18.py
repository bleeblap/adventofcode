#!/usr/bin/env python

import sys
import re
import copy

infile = open('18.in').read()

infile2 = '''.#.#...|#.
.....#|##|
.|..|...#.
..|#.....#
#.#|||#|#|
...#.||...
.|....|...
||...#|.#|
|.||||..|.
...#.|..|.'''

state = []
for line in infile.split('\n'):
    state.append([x for x in line])

def countAdjacent(state, x, y, c):
    count = 0
    for dx in range(-1, 2):
        for dy in range(-1,2):
            if dx == 0 and dy == 0:
                continue
            try:
                # Yay python negative index is valid
                if y+dy >= 0 and x+dx >= 0:
                    #print dy,dx,state[y+dy][x+dx]
                    count += int(state[y+dy][x+dx]==c)
            except:
                pass
    return count

def dump(state):
    for y in range(len(state)):
        line = ''
        for x in range(len(state[y])):
            line += state[y][x]
        print line

def calcScore(state):
    numTree = 0
    numLumber = 0
    for y in range(len(state)):
        for x in range(len(state[y])):
            if state[y][x] == '|':
                numTree += 1
            elif state[y][x] == '#':
                numLumber += 1
    return (numTree,numLumber)

#print countAdjacent(state,0,4,'|')
#sys.exit(0)
#dump(state)

gridHistory = [state]
scores = [calcScore(state)]
for min in range(1,1000):
    nextstate = []
    for y in range(len(state)):
        nextrow = []
        for x in range(len(state[y])):
            if state[y][x] == '.':
                #print x,y,countAdjacent(state,x,y,'|')
                if countAdjacent(state,x,y,'|') >= 3:
                    nextrow.append('|')
                else:
                    nextrow.append('.')
            elif state[y][x] == '|':
                if countAdjacent(state,x,y,'#') >= 3:
                    nextrow.append('#')
                else:
                    nextrow.append('|')
            elif state[y][x] == '#':
                if countAdjacent(state,x,y,'#') >= 1 and countAdjacent(state,x,y,'|') >= 1:
                    nextrow.append('#')
                else:
                    nextrow.append('.')
        nextstate.append(nextrow)

    if nextstate in gridHistory:
        cycleStart = gridHistory.index(nextstate)
        cycleEnd = min
        #print 'Found repeat at ',min,' of grid ',gridHistory.index(nextstate)
        break
    state = nextstate
    #print min
    #dump(state)
    nt,nl = calcScore(state)
    scores.append((min,nt,nl,nt*nl))
    gridHistory.append(state)
    if min == 10:
        print 'Part1',nt*nl
    min += 1

cycleRem = (1000000000 - cycleStart) % (cycleEnd - cycleStart)
print 'Part2',scores[cycleStart+cycleRem][3]
