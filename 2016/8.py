#!/usr/bin/env python3

from copy import deepcopy

lines = open('8.in').read().split('\n')
screen = [[' ' for x in range(50)] for y in range(6)]

def dispScreen(screen):
	for row in screen:
		for c in row:
			print(c, end='')
		print('')
	print('')

for line in lines:
	if line.startswith('rect'):
		c,r = [int(x) for x in line.split(' ')[1].split('x')]
		#print('rect',c,r)
		for x in range(r):
			for y in range(c):
				screen[x][y] = '#'	
	elif line.startswith('rotate'):
		_,_,idx,_,amt = line.split(' ')
		xy,idx = idx.split('=')
		idx = int(idx)
		amt = int(amt)
		#print('rotate',xy,idx,amt)
		if xy == 'y':
			screen[idx] = screen[idx][-amt:] + screen[idx][:-amt]
		else:
			for _ in range(amt):
				orig = deepcopy(screen)
				for r in range(len(screen)):
					screen[r][idx] = orig[r-1][idx]

p1 = sum([len([col for col in row if col == '#']) for row in screen])
print('part1',p1)
dispScreen(screen)