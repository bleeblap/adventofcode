#!/usr/bin/env python

import sys
import copy
from blist import blist

players = 429
#players = 30
scores = [0 for x in range(players)]
p1marble = 70901
lastmarble = p1marble*100
#lastmarble = 5807
board = blist([0, 2, 1])
curidx = 1
curplayer = 2
nextm = 3

while nextm < lastmarble:
    m = nextm
    nextm += 1
    #if m%(int(lastmarble/100)) == 0:
    #    print '{}%'.format(int(100*(float(m)/float(lastmarble))))
    if m == p1marble:
        print 'Part1',max(scores)
    if m % 23 == 0:
        rem = board[(curidx-7)%len(board)]
        curidx = (curidx-7)%len(board)
        #print 'REM',rem
        scores[curplayer] += m+rem
        del board[curidx]
    else:
        if curidx == len(board)-2:
            board.append(m)
            curidx = len(board)-1
        else:
            board.insert((curidx+2)%len(board), m)
            curidx = (curidx+2)%(len(board)-1)
    curplayer = (curplayer+1)%players

print 'Part2',max(scores)
