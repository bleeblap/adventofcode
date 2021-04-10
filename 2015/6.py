#!/usr/bin/env python

import re

infile = open('6.in','r').read()

def do_part1(board,action,x,y):
	if action == 'on':
		board[y][x] = 1
	elif action == 'off':
		board[y][x] = 0
	elif action == 'toggle':
		board[y][x] = int(board[y][x]==0)
	else:
		assert(action)

def do_part2(board,action,x,y):
	if action == 'on':
		board[y][x] += 1
	elif action == 'off':
		board[y][x] = max(board[y][x]-1,0)
	elif action == 'toggle':
		board[y][x] += 2
	else:
		assert(action)

def do_loop(infile, do_action, board):
	for line in infile.split('\n'):
		x1,y1,x2,y2 = map(int, re.findall('\d+', line))
		action = None
		if line.split(' ')[0] == 'turn':
			action = line.split(' ')[1]
		else:
			action = line.split(' ')[0]
		#print action,x1,y1,x2,y2

		for x in range(x1, x2+1):
			for y in range(y1, y2+1):
				do_action(board,action,x,y)

SIZE = 1000
board = [[0 for y in range(SIZE)] for x in range(SIZE)]
do_loop(infile, do_part1, board)
print 'Part1',sum([sum(x) for x in board])

board = [[0 for y in range(SIZE)] for x in range(SIZE)]
do_loop(infile, do_part2, board)
print 'Part2',sum([sum(x) for x in board])