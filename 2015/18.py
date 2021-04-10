#!/usr/bin/env python

infile = open('18.in').read()
infile2 = '''.#.#.#
...##.
#....#
..#...
#.#..#
####..'''

board = []
for line in infile.split('\n'):
	board.append([c for c in line])

def count_neighbors(board, x, y):
	count = 0
	for dy in range(-1,2):
		for dx in range(-1,2):
			if dy == 0 and dx == 0:
				continue
			if x+dx < 0 or x+dx >= len(board[0]):
				continue
			if y+dy < 0 or y+dy >= len(board):
				continue
			if board[y+dy][x+dx] == '#':
				count += 1
	return count

def dump(board):
	for y in range(len(board)):
		line = ''
		for x in range(len(board[y])):
			line += board[y][x]
		print line

def sim(board, rounds, part2=False):
	for step in range(1,rounds+1):
		nextb = []
		for y in range(len(board)):
			nextr = []
			for x in range(len(board[0])):
				n = count_neighbors(board, x, y)
				if board[y][x] == '.':
					if n == 3:
						nextr.append('#')
					else:
						nextr.append('.')
				else:
					if n == 2 or n == 3:
						nextr.append('#')
					else:
						nextr.append('.')
			nextb.append(nextr)
		if part2:
			nextb[0][0] = '#'
			nextb[len(nextb)-1][0] = '#'
			nextb[0][len(nextb[0])-1] = '#'
			nextb[len(nextb)-1][len(nextb[0])-1] = '#'
		board = nextb
	return board

p1 = sim(board, 100)
print 'Part1',''.join([''.join(r) for r in p1]).count('#')
p2 = sim(board, 100, True)
print 'Part2',''.join([''.join(r) for r in p2]).count('#')



