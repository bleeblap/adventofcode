#!/usr/bin/env python3

from copy import copy

lines = '''sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew'''.split('\n')
lines = open('24.in').read().split('\n')

SIZE=600
grid = [[' ' if x%2==y%2 else '.' for x in range(SIZE)] for y in range(SIZE)]

for line in lines:
	pos = [SIZE//2,SIZE//2]
	while len(line) > 0:
		n = line[0]
		if n in ['n','s']:
			n = line[:2]
		line = line[len(n):]
		if n == 'e':
			pos[1] += 2
		elif n == 'se':
			pos[0] -= 1
			pos[1] += 1
		elif n == 'ne':
			pos[0] += 1
			pos[1] += 1
		elif n == 'w':
			pos[1] -= 2
		elif n == 'sw':
			pos[0] -= 1
			pos[1] -= 1
		elif n == 'nw':
			pos[0] += 1
			pos[1] -= 1
		else:
			print('error')
	#print(pos, grid[pos[1]][pos[0]])
	if grid[pos[1]][pos[0]] == ' ':
		grid[pos[1]][pos[0]] = '#'
	else:
		grid[pos[1]][pos[0]] = ' '

def count(grid):
	c = 0
	for x in range(SIZE):
		for y in range(SIZE):
			if grid[x][y] == '#':
				c += 1
	return c

def dump(grid):
	for x in range(SIZE):
		for y in range(SIZE):
			print(grid[x][y],end='')
		print()

print('part1',count(grid))

for day in range(1,101):
	newg = []
	for x in range(SIZE):
		newr = []
		for y in range(SIZE):
			if x%2 != y%2:
				newr.append('.')
				continue
			c = 0
			for dx,dy in [(2,0),(-2,0),(1,1),(1,-1),(-1,1),(-1,-1)]:
				if x+dx >= 0 and x+dx < SIZE and y+dy >= 0 and y+dy < SIZE:
					if grid[x+dx][y+dy] == '#':
						c += 1
			if grid[x][y] == '#' and (c == 0 or c > 2):
				newr.append(' ')
			elif grid[x][y] == ' ' and c == 2:
				newr.append('#')
			else:
				newr.append(grid[x][y])
		newg.append(newr)
	grid = newg
	#print(day,count(grid))
	
#dump(grid)
print('part2',count(grid))

