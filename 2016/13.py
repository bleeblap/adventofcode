#!/usr/bin/env python3

from heapq import heappush, heappop

SIZE = 50
FAVNUM = 1358
#FAVNUM = 10
grid = [['.' for _ in range(SIZE)] for _ in range(SIZE)]

def dump(grid):
	for line in grid:
		print(''.join(line))
	print('\n')

for x in range(SIZE):
	for y in range(SIZE):
		val = x*x + 3*x + 2*x*y + y + y*y + FAVNUM
		if bin(val).count('1') % 2:
			grid[y][x] = '#'

def dist(one, two):
	return abs(one[0]-two[0])+abs(one[1]-two[1])

pos = (1,1)
#target = (7,4)
target = (31,39)

pq = []
history = set()
heappush(pq, (0, dist(pos,target), pos))
p2found = False
while len(pq) > 0:
	step,d,pos = heappop(pq)
	#print(step,d,pos)
	if pos == target:
		print('part1',step)
		break
	if step > 50 and not p2found:
		print('part2',len(history))
		p2found = True
	history.add(pos)
	for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
		if pos[0]+dx >= 0 and pos[1]+dy >= 0:
			newp = (pos[0]+dx, pos[1]+dy)
			if grid[newp[1]][newp[0]] == '.' and newp not in history:
				heappush(pq, (step+1, dist(newp, target), newp))
