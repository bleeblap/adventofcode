#!/usr/bin/env python3

moves = open('1.in').read().split(', ')
pos = complex(0,0)
cdir = complex(1,0)
locations = []
p2found = False

for move in moves:
	cdir *= complex(0,1) if move[0] == 'L' else complex(0,-1)
	for i in range(int(move[1:])):
		pos += cdir
		if pos in locations and not p2found:
			print('part2', int(abs(pos.real)+abs(pos.imag)))
			p2found = True
		else:
			locations.append(pos)

print('part1', int(abs(pos.real)+abs(pos.imag)))

