#!/usr/bin/env python3

lines = '''.#.
..#
###'''.split('\n')
lines = open('17.in').read().split('\n')


SIZE = 40

state = [[['.' for _ in range(SIZE)] for _ in range(SIZE)] for _ in range(SIZE)]
state2 = [[[['.' for _ in range(SIZE)] for _ in range(SIZE)] for _ in range(SIZE)] for _ in range(SIZE)]
for y in range(len(lines)):
	for x in range(len(lines[y])):
		state[SIZE//2][SIZE//2+y-len(lines)//2][SIZE//2+x-len(lines[y])//2] = lines[y][x]
		state2[SIZE//2][SIZE//2][SIZE//2+y-len(lines)//2][SIZE//2+x-len(lines[y])//2] = lines[y][x]

def dumpz(state):
	for y in range(len(state)):
		for x in range(len(state[y])):
			print(state[y][x],end='')
		print()
	print()

def count(state,x,y,z):
	res = 0
	for dz in range(-1,2):
		if z+dz < 0 or z+dz >= len(state):
			continue
		for dy in range(-1,2):
			if y+dy < 0 or y+dy >= len(state[z]):
				continue
			for dx in range(-1,2):
				if x+dx < 0 or x+dx >= len(state[z][y]):
					continue
				if dx == dy == dz == 0:
					continue
				if state[z+dz][y+dy][x+dx] == '#':
					res += 1
	return res

def count2(state,x,y,z,w):
	res = 0
	for dw in range(-1,2):
		if w+dw < 0 or w+dw >= len(state):
			continue
		for dz in range(-1,2):
			if z+dz < 0 or z+dz >= len(state[w]):
				continue
			for dy in range(-1,2):
				if y+dy < 0 or y+dy >= len(state[w][z]):
					continue
				for dx in range(-1,2):
					if x+dx < 0 or x+dx >= len(state[w][z][y]):
						continue
					if dw == dx == dy == dz == 0:
						continue
					if state[w+dw][z+dz][y+dy][x+dx] == '#':
						res += 1
	return res

for cycle in range(6):
	nexts = []
	for z in range(len(state)):
		nextz = []
		for y in range(len(state[z])):
			nexty = []
			for x in range(len(state[z][y])):
				c = count(state, x, y, z)
				if state[z][y][x] == '#':
					if 2 <= c <= 3:
						nexty.append('#')
					else:
						nexty.append('.')
				else:
					if c == 3:
						nexty.append('#')
					else:
						nexty.append('.')
			nextz.append(nexty)
		nexts.append(nextz)
	state = nexts
	#print(cycle)
	#dumpz(state[SIZE//2])

p1 = 0
for z in range(len(state)):
	for y in range(len(state[z])):
		for x in range(len(state[z][y])):
			if state[z][y][x] == '#':
				p1 += 1
print('part1',p1)


state = state2
for cycle in range(6):
	nexts = []
	for w in range(len(state)):
		nextw = []
		for z in range(len(state[w])):
			nextz = []
			for y in range(len(state[w][z])):
				nexty = []
				for x in range(len(state[w][z][y])):
					c = count2(state, x, y, z, w)
					if state[w][z][y][x] == '#':
						if 2 <= c <= 3:
							nexty.append('#')
						else:
							nexty.append('.')
					else:
						if c == 3:
							nexty.append('#')
						else:
							nexty.append('.')
				nextz.append(nexty)
			nextw.append(nextz)
		nexts.append(nextw)
	state = nexts
	#print(cycle)
	#dumpz(state[SIZE//2][SIZE//2])

p2 = 0
for w in range(len(state)):
	for z in range(len(state[w])):
		for y in range(len(state[w][z])):
			for x in range(len(state[w][z][y])):
				if state[w][z][y][x] == '#':
					p2 += 1
print('part2',p2)