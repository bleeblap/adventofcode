#!/usr/bin/env python3

from copy import deepcopy

lines = '''L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL'''.split('\n')
lines = open('11.in').readlines()

state = [[c for c in line.rstrip()] for line in lines]

def dump(state):
	for row in state:
		for c in row:
			print(c,end='')
		print('')
	print('')

def count_occup(state):
	res = 0
	for r in range(len(state)):
		for c in range(len(state[r])):
			if state[r][c] == '#':
				res += 1
	return res

while True:
	prev = deepcopy(state)
	for r in range(len(state)):
		for c in range(len(state[r])):
			if prev[r][c] == '.':
				continue
			occup = 0
			for x in range(-1,2):
				for y in range(-1,2):
					if r+x < 0 or c+y < 0 or r+x >= len(prev) or c+y >= len(prev[r]) or (x==0 and y==0):
						continue
					if prev[r+x][c+y] == '#':
						occup += 1
			if prev[r][c] == 'L' and occup == 0:
				state[r][c] = '#'
			elif prev[r][c] == '#' and occup >= 4:
				state[r][c] = 'L'
	#dump(state)
	if prev == state:
		break

print('part1',count_occup(state))

def rtrace(state,px,py,dx,dy):
	n = 1
	while 0 <= px+n*dx < len(state) and 0 <= py+n*dy < len(state[0]):
		#print(n,dx,dy,px+n*dx,py+n*dy,state[px+n*dx][py+n*dy])
		if state[px+n*dx][py+n*dy] == '#':
			return 1
		elif state[px+n*dx][py+n*dy] == 'L':
			return 0
		n += 1
	return 0

state = [[c for c in line.rstrip()] for line in lines]
while True:
	prev = deepcopy(state)
	for r in range(len(state)):
		for c in range(len(state[r])):
			if prev[r][c] == '.':
				continue
			occup = 0
			for x in range(-1,2):
				for y in range(-1,2):
					if x==0 and y==0:
						continue
					if rtrace(prev,r,c,x,y):
						occup += 1
			if prev[r][c] == 'L' and occup == 0:
				state[r][c] = '#'
			elif prev[r][c] == '#' and occup >= 5:
				state[r][c] = 'L'
	#dump(state)
	if prev == state:
		break

print('part2',count_occup(state))

if False:
	lines = '''.......#.
	...#.....
	.#.......
	.........
	..#L....#
	....#....
	.........
	#........
	...#.....
	'''.split('\n')
	state = [[c for c in line.rstrip()] for line in lines]
	print(state)
	for x in range(-1,2):
		for y in range(-1,2):
			if x==0 and y==0:
				continue
			print('RES',x,y,rtrace(state,4,3,x,y))
