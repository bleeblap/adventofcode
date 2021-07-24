#!/usr/bin/env python3

from heapq import heappush, heappop
from itertools import permutations
import networkx as nx

lines = '''###########
#0.1.....2#
#.#######.#
#4.......3#
###########'''.split('\n')
lines = open('24.in').read().split('\n')

grid = [[x for x in line] for line in lines]

def find_paths(seed, grid):
	for y in range(len(grid)):
		for x in range(len(grid[y])):
			if grid[y][x] == seed:
				start = (x,y)
				break
	pq = []
	history = []
	paths = {}
	heappush(pq, (0, start))
	while len(pq) > 0:
		d,pos = heappop(pq)

		if grid[pos[1]][pos[0]] not in ['#','.',seed]:
			#print('FOUND {}->{}={}'.format(seed,grid[pos[1]][pos[0]],d))
			if grid[pos[1]][pos[0]] not in paths:
				paths[grid[pos[1]][pos[0]]] = d
			continue

		for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
			if (pos[0]+dx,pos[1]+dy) in history:
				continue
			history.append((pos[0]+dx,pos[1]+dy))
			if grid[pos[1]+dy][pos[0]+dx] != '#':
				heappush(pq, (d+1, (pos[0]+dx,pos[1]+dy)))
	return paths

NUM = 8
G = nx.Graph()
for x in range(NUM):
	G.add_node(chr(ord('0')+x))

for x in range(NUM):
	paths = find_paths(chr(ord('0')+x), grid)
	for p in paths:
		G.add_edge(chr(ord('0')+x), p, weight=paths[p])

tsp = 9999999999999
for path in permutations(G.nodes()):
	cost = 0
	if path[0] != '0':
		continue
	for i in range(len(path)-1):
		cost += nx.shortest_path_length(G,path[i],path[i+1],'weight')
	if cost < tsp:
		tsp = cost
		#print(tsp,path)
print('part1',tsp)

tsp = 9999999999999
for path in permutations(G.nodes()):
	cost = 0
	if path[0] != '0':
		continue
	path += ('0',)
	for i in range(len(path)-1):
		cost += nx.shortest_path_length(G,path[i],path[i+1],'weight')
	if cost < tsp:
		tsp = cost
		#print(tsp,path)
print('part2',tsp)
