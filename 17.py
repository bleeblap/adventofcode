#!/usr/bin/env python

import sys
import re
import copy

infile = open('17.in').read()

infile2 = '''x=495, y=2..7
y=7, x=495..501
x=501, y=3..7
x=498, y=2..4
x=506, y=1..2
x=498, y=10..13
x=504, y=10..13
y=13, x=498..504'''

def dump(board):
    for y in range(len(board)):
        line = ''
        for x in range(len(board[y])):
            line += board[y][x]
        print line

clayscans = []
for line in infile.split('\n'):
    if line[0] == 'x':
        x1, y1, y2 = [int(x) for x in re.findall('\d+', line)]
        x2 = x1
    else:
        y1, x1, x2 = [int(x) for x in re.findall('\d+', line)]
        y2 = y1
    clayscans.append([x1,x2,y1,y2,line[0]])

minx = min([x[0] for x in clayscans])-5
maxx = max([x[1] for x in clayscans])+5
miny = min([x[2] for x in clayscans])
maxy = max([x[3] for x in clayscans])
spring = (500,0)

maxsane = 50500 #(maxy-miny)*(maxx-minx)

board = [['.' for x in range(minx,maxx+1)] for y in range(0,maxy+2)]
board[spring[1]][spring[0]-minx] = '+'

for scan in clayscans:
    for y in range(scan[2],scan[3]+1):
        for x in range(scan[0]-minx,scan[1]+1-minx):
            board[y][x] = '#'

startpos = [(spring[1]+1,spring[0]-minx)]
overFlow = False
round = 0
while (not overFlow or len(startpos) != 0) and round < maxsane:
    round += 1
    if len(startpos) == 0:
        #print 'Something bad probably'
        startpos = [(spring[1]+1,spring[0]-minx)]
    cy,cx = startpos[0]
    while True:
        if board[cy][cx] == '~':
            # Start point underwater (nested box?)
            #print 'del startpos'
            del startpos[0]
            break
        if board[cy+1][cx] in '.|':
            # Freefall easy, flow down one
            board[cy][cx] = '|'
            if cy >= maxy:
                overFlow = True
                del startpos[0]
                break
            cy += 1
        elif board[cy+1][cx] in '#~':
            # Check if contained or keep flowing
            foundLeft = False
            foundRight = False
            foundWaterfall = False
            lx = None
            rx = None
            tx = cx
            while tx >= 0:
                if board[cy][tx] in '.|':
                    board[cy][tx] = '|'
                    if board[cy+1][tx] in '.|':
                        # Not contained, back to freefall
                        if (cy,tx) not in startpos:
                            #print 'append',cy,tx
                            startpos.append((cy,tx))
                        foundWaterfall = True
                        break
                    tx -= 1
                elif board[cy][tx] in '#~':
                    foundLeft = True
                    lx = tx+1
                    break
            tx = cx
            while tx < maxx-minx+1:
                if board[cy][tx] in '.|':
                    board[cy][tx] = '|'
                    if board[cy+1][tx] in '.|':
                        # Not contained, back to freefall
                        if (cy,tx) not in startpos:
                            #print 'append',cy,tx
                            startpos.append((cy,tx))
                        foundWaterfall = True
                        break
                    tx += 1
                elif board[cy][tx] in '#~':
                    foundRight = True
                    rx = tx-1
                    break
            # Hit surface, settle if contained
            #print foundLeft, foundRight, lx, rx
            if foundLeft and foundRight:
                if cx-lx > rx-cx:
                    board[cy][lx] = '~'
                else:
                    board[cy][rx] = '~'
            if foundWaterfall:
                #print 'del',startpos
                del startpos[0]
            break

#dump(board)

wetspots = 0
retained = 0
for y in range(miny, maxy+1):
    for x in range(minx, maxx+1):
        if board[y][x-minx] in '~|':
            wetspots += 1
        if board[y][x-minx] == '~':
            retained += 1
print 'Part1',wetspots
print 'Part2',retained
