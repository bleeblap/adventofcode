#!/usr/bin/env python

import sys
import copy
import re

input = open('3.in','r').read()

board = []
row = []
for x in range(1000):
    row.append(0)
for x in range(1000):
    board.append(copy.deepcopy(row))

for claim in input.split('\n'):
    id,x,y,w,h = map(int, re.findall('\d+',claim))
    for curw in range(w):
        for curh in range(h):
            board[x+curw][y+curh] += 1

overlaps = 0
for x in range(len(board)):
    for y in range(len(board[x])):
        if board[x][y] > 1:
            overlaps += 1
print 'Part1',overlaps

for claim in input.split('\n'):
    id,x,y,w,h = map(int, re.findall('\d+',claim))
    wrong = False
    for curw in range(w):
        for curh in range(h):
            if board[x+curw][y+curh] != 1:
                wrong = True
    if not wrong:
        print 'Part2',id
        break
