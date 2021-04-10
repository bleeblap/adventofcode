#!/usr/bin/env python3

lines = open('5.in').read().split('\n')

ROWS = 128
COLS = 8
seats = [[0 for _ in range(COLS)] for _ in range(ROWS)]

def decode(line):
	rh = line[:7]
	ch = line[7:]
	row = (0, ROWS-1)
	col = (0, COLS-1)
	for rc in rh:
		d = (row[1]-row[0])//2
		if rc == 'F':
			row = (row[0], row[1]-d-1)
		else:
			row = (row[0]+d+1, row[1])
	for cc in ch:
		d = (col[1]-col[0])//2
		if cc == 'L':
			col = (col[0], col[1]-d-1)
		else:
			col = (col[0]+d+1, col[1])
	return (row[0], col[0])

part1 = 0
for line in lines:
	r,c = decode(line)
	seats[r][c] = 1
	sid = r*8+c
	if sid > part1:
		part1 = sid
print('part1', part1)

for r in range(12,ROWS-12):
	for c in range(COLS):
		if seats[r][c] == 0:
			print('part2',r*8+c)