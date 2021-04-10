#!/usr/bin/env python

import sys
import re
import copy

infile = open('25.in','r').read()
test1 = '''0,0,0,0
 3,0,0,0
 0,3,0,0
 0,0,3,0
 0,0,0,3
 0,0,0,6
 9,0,0,0
12,0,0,0'''

test2 = '''-1,2,2,0
0,0,2,-2
0,0,0,-2
-1,2,0,0
-2,-2,-2,2
3,0,2,-1
-1,3,2,2
-1,0,-1,0
0,2,1,-2
3,0,0,0'''

test3 = '''1,-1,0,1
2,0,-1,0
3,2,-1,0
0,0,3,1
0,0,-1,-1
2,3,-2,0
-2,2,0,0
2,-2,0,-1
1,-1,0,-1
3,2,0,2'''

test4 = '''1,-1,-1,-2
-2,-2,0,1
0,2,1,3
-2,3,-2,1
0,2,3,-2
-1,-1,1,-2
0,-2,-1,0
-2,2,3,-1
1,2,2,0
-1,-2,0,-2'''

test5 = test1 + '\n6,0,0,0'

tests = [test1, test2, test3, test4, test5]
testanswer = [2, 4, 3, 8, 1]

def man_dist(b1, b2):
    return abs(b1[0]-b2[0]) + abs(b1[1]-b2[1]) + abs(b1[2]-b2[2]) + abs(b1[3]-b2[3])

def count_constellation(infile):
	consts = {}
	points = []
	for line in infile.split('\n'):
		x,y,z,t = map(int, re.findall('-?\d+', line))
		points.append((x,y,z,t))

	consts[0] = [points.pop(0)]
	cid = 1
	while len(points) > 0:
		p = points.pop(0)
		match = []
		for k,v in consts.items():
			for p2 in v:
				if man_dist(p,p2) <= 3 and k not in match:
					match.append(k)
		if len(match) == 0:
			consts[cid] = [p]
			cid += 1
		elif len(match) == 1:
			consts[match[0]].append(p)
		else:
			#print 'JOIN', p, match
			newconst = [p]
			for m in match:
				newconst.extend(copy.deepcopy(consts[m]))
				del consts[m]
			consts[cid] = newconst
			cid += 1

	return consts

for x in range(len(tests)):
	assert testanswer[x] == len(count_constellation(tests[x]))

consts = count_constellation(infile)
print 'Part1',len(consts)

