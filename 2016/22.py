#!/usr/bin/env python3

import re
from copy import deepcopy
from heapq import heappush, heappop

nodes = [[[] for x in range(38)] for y in range(26)]
lines = open('22.in').read().split('\n')
for line in lines[2:]:
	x,y,sz,us,av,per = [int(x) for x in re.findall('(\d+)', line)]
	nodes[y][x] = [sz,us,av]

p1 = 0

for y1 in range(len(nodes)):
	for x1 in range(len(nodes[y1])):
		for y2 in range(len(nodes)):
			for x2 in range(len(nodes[y1])):
				if x1 == x2 and y1 == y2:
					continue
				if nodes[y1][x1][1] != 0 and nodes[y1][x1][1] <= nodes[y2][x2][2]:
					p1 += 1

print('part1',p1)

start = None
for y1 in range(len(nodes)):
	line = '|'
	for x1 in range(len(nodes[y1])):
		if nodes[y1][x1][1] == 0:
			start = (x1,y1)
			line += '_'
		elif nodes[y1][x1][1] > 100:
			line += 'X'
		else:
			line += ' '
	print(line+'|')

# dist move all left, then all up, then to start, and move G once
p2 = start[0] + start[1] + 36 + 1
# D L L U to get open around, then move G for 5 moves per cycle, safe because no blocks in y=0 or y=1
p2 += 5 * 36
print('part2',p2) # 253 too low