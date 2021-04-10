#!/usr/bin/env python3

import math

lines = '''Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###...'''
lines = open('20.in').read()

def dump(tile):
	for r in tile:
		print(r)
	print()

def rotateCW(tile):
	res = []
	for i in range(len(tile)):
		res.append(''.join([r[i] for r in tile])[::-1])
	return res

def flipH(tile):
	return [tile[i] for i in range(len(tile)-1,-1,-1)]

def flipV(tile):
	return [r[::-1] for r in tile]

def stripBorder(tile):
	res = []
	for i in range(1,len(tile)-1):
		res.append(tile[i][1:-1])
	return res

combofuncs = [
	lambda x: x,
	lambda x: flipH(x),
	lambda x: flipV(x),
	lambda x: rotateCW(x),
	lambda x: flipH(rotateCW(x)),
	lambda x: flipV(rotateCW(x)),
	lambda x: rotateCW(rotateCW(x)),
	lambda x: rotateCW(rotateCW(rotateCW(x))),
]
def combos(tile):
	for cf in combofuncs:
		yield cf(tile)

tiles = {}
for tile in lines.split('\n\n'):
	tid = int(tile.split('\n')[0].split(' ')[1].split(':')[0])
	tiles[tid] = []
	for r in tile.split('\n')[1:]:
		tiles[tid].append(r)
sz = int(math.sqrt(len(tiles)))
grid = [[(None,None) for _ in range(sz)] for _ in range(sz)]

adjacency = {}
for tid in tiles:
	adjacency[tid] = {}
	c1c = 0
	for c1 in combos(tiles[tid]):
		t = c1[0]
		b = c1[-1]
		l = ''.join([r[0] for r in c1])
		r = ''.join([r[-1] for r in c1])
		adjacency[tid][c1c] = {}

		for ctid in tiles:
			if tid == ctid:
				continue
			c2c = 0
			for c2 in combos(tiles[ctid]):
				ct = c2[0]
				cb = c2[-1]
				cl = ''.join([r[0] for r in c2])
				cr = ''.join([r[-1] for r in c2])
				if l == cr:
					adjacency[tid][c1c]['l'] = (ctid,c2c)
				if r == cl:
					adjacency[tid][c1c]['r'] = (ctid,c2c)
				if t == cb:
					adjacency[tid][c1c]['t'] = (ctid,c2c)
				if b == ct:
					adjacency[tid][c1c]['b'] = (ctid,c2c)
				c2c += 1
		c1c += 1
		
	#print(tid,adjacency[tid])
pieces = [k for k in adjacency.keys()]
p1 = 1
for adj in adjacency:
	conns = max([len(adjacency[adj][x].keys()) for x in adjacency[adj]])
	if conns == 2:
		p1 *= adj
print('part1',p1)

for x in range(sz):
	for y in range(sz):
		#print()
		#print(x,y)
		#print('grid',grid)
		#print('pieces',pieces)
		for p in pieces:
			if grid[x][y] != (None, None):
				break
			if x == 0 and y == 0:
				# First piece, pick an corner and orient correctly
				conns = max([len(adjacency[p][x].keys()) for x in adjacency[p]])
				if conns == 2:
					for c,v in adjacency[p].items():
						if 'r' in v and 'b' in v:
							grid[x][y] = (p,c)
							pieces.remove(p)
							break
			elif y == 0:
				conna = adjacency[grid[x-1][y][0]][grid[x-1][y][1]]
				if p == conna['b'][0]:
					conne = adjacency[p][conna['b'][1]]
					grid[x][y] = (p,conna['b'][1])
					pieces.remove(p)
					break
			else:
				conna = adjacency[grid[x][y-1][0]][grid[x][y-1][1]]
				if p == conna['r'][0]:
					conne = adjacency[p][conna['r'][1]]
					grid[x][y] = (p,conna['r'][1])
					pieces.remove(p)
					break

#print(grid)
imagesz = sz*(len(tiles[grid[0][0][0]][0])-2)
image = [' '*imagesz for _ in range(imagesz)]
for x in range(sz):
	for y in range(sz):
		tmp = stripBorder(combofuncs[grid[x][y][1]](tiles[grid[x][y][0]]))
		for r in range(len(tmp)):
			image[r+x*len(tmp)] = image[r+x*len(tmp)][:y*len(tmp)] + tmp[r] + image[r+x*len(tmp)][(y+1)*len(tmp):]
#dump(image)

monster = '''                  # 
#    ##    ##    ###
 #  #  #  #  #  #   '''
monster = [[c for c in row] for row in monster.split('\n')]

monsters = 0
for check in combos(image):
	for x in range(len(check)):
		for y in range(len(check[x])):
			found = True
			for x2 in range(len(monster)):
				for y2 in range(len(monster[x2])):
					if x+x2 >= len(check) or y+y2 >= len(check[x]):
						found = False
					elif monster[x2][y2] == '#':
						if check[x+x2][y+y2] == '.':
							found = False
			if found:
				for x2 in range(len(monster)):
					for y2 in range(len(monster[x2])):
						if monster[x2][y2] == '#':
							check[x+x2] = check[x+x2][:y+y2] + 'O' + check[x+x2][y+y2+1:]
				monsters += 1
	if monsters > 0:
		p2 = 0
		#dump(check)
		for x in range(len(check)):
			for y in range(len(check[x])):
				if check[x][y] == '#':
					p2 += 1
		print('part2',p2)
		break
