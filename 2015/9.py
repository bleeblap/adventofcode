#!/usr/bin/env python

from itertools import permutations

infile = open('9.in','r').read()

infile2 = '''London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141'''

nodes = set()
mygraph = {}
for line in infile.split('\n'):
	d = int(line.split(' = ')[1])
	start = line.split(' to ')[0]
	end = line.split(' to ')[1].split(' ')[0]

	nodes.add(start)
	nodes.add(end)
	if start not in mygraph:
		mygraph[start] = {}
	mygraph[start][end] = d
	if end not in mygraph:
		mygraph[end] = {}
	mygraph[end][start] = d
	#print start,end,d

# BRUTE FORCE!
dist = []
for path in permutations(nodes):
	d = 0
	for x in range(len(path)-1):
		d += mygraph[path[x]][path[x+1]]
	dist.append(d)

print 'Part1',min(dist)
print 'Part2',max(dist)