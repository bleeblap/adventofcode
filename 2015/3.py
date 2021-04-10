#!/usr/bin/env python

infile = open('3.in','r').read()
#infile = '^>v<'

SIZE = 500
board = [[0 for y in range(SIZE)] for x in range(SIZE)]

x,y = SIZE/2, SIZE/2
board[y][x] = 1

for c in infile:
	if c == '^':
		y-=1
	elif c == 'v':
		y+=1
	elif c == '>':
		x+=1
	elif c == '<':
		x-=1
	else:
		assert(x)
	board[y][x] += 1

delivered = 0
for y in range(SIZE):
	for x in range(SIZE):
		if board[y][x] >= 1:
			delivered += 1
print 'Part1',delivered

board = [[0 for y in range(SIZE)] for x in range(SIZE)]
x1,y1 = SIZE/2, SIZE/2
x2,y2 = SIZE/2, SIZE/2
board[y1][x1] = 2

for c in range(len(infile)):
	if c%2 == 0:
		cx = x1
		cy = y1
	else:
		cx = x2
		cy = y2
	if infile[c] == '^':
		cy-=1
	elif infile[c] == 'v':
		cy+=1
	elif infile[c] == '>':
		cx+=1
	elif infile[c] == '<':
		cx-=1
	else:
		assert(x)
	board[cy][cx] += 1
	if c%2 == 0:
		x1 = cx
		y1 = cy
	else:
		x2 = cx
		y2 = cy

delivered = 0
for y in range(SIZE):
	for x in range(SIZE):
		if board[y][x] >= 1:
			delivered += 1
print 'Part2',delivered # 2361 HIGH