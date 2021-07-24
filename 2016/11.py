#!/usr/bin/env python3

from copy import deepcopy
from heapq import heappush, heappop
from itertools import combinations
import re

lines = '''The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.
The second floor contains a hydrogen generator.
The third floor contains a lithium generator.
The fourth floor contains nothing relevant.'''.split('\n')
lines = open('11.in').read().split('\n')

init = [set() for _ in range(len(lines))]
types = []
for l in range(len(lines)): 
	init[l] |= {'m'+x[:2] for x in re.findall('(\S+)\-compatible', lines[l])}
	init[l] |= ({'g'+x[:2] for x in re.findall('(\S+) generator', lines[l])})
	types += [x[:2] for x in re.findall('(\S+)\-compatible', lines[l])]

def is_valid(state):
	for f in state:
		for s in f:
			if s[0] == 'm' and 'g'+s[1:] not in f and len([x for x in f if x[0]=='g'])>0:
				return False
	return True

def get_pairs(state):
	pairs = []
	for t in types:
		mf = 0
		gf = 0
		for fn in range(len(state)):
			if 'm'+t in state[fn]:
				mf = fn
			elif 'g'+t in state[fn]:
				gf = fn
		pairs.append((mf,gf))
	return sorted(pairs)

def in_history(item, history):
	for h in history:
		if item[0] == h[0] and get_pairs(item[1]) == get_pairs(h[1]):
			return True
	return False

def sim(init):
	pq = []
	history = []
	total = sum([len(x) for x in init])
	heappush(pq, (0, 0, init))
	while len(pq) > 0:
		steps, elev, state = heappop(pq)
		#print(len(pq), steps, elev, state)

		if len(state[-1]) == total:
			return steps

		if in_history((elev,state), history):
			continue
		history.append((elev,state))

		if elev < len(state)-1:
			found2 = False
			for c in combinations(state[elev], 2):
				ns = deepcopy(state)
				for i in c:
					ns[elev].remove(i)
					ns[elev+1].add(i)
				if is_valid(ns):
					found2 = True
					heappush(pq, (steps+1, elev+1, ns))

			if not found2:
				for i in state[elev]:
					ns = deepcopy(state)
					ns[elev].remove(i)
					ns[elev+1].add(i)
					if is_valid(ns):
						heappush(pq, (steps+1, elev+1, ns))

		if elev > 0:
			found1 = False
			for i in state[elev]:
				ns = deepcopy(state)
				ns[elev].remove(i)
				ns[elev-1].add(i)
				if is_valid(ns):
					found1 = True
					heappush(pq, (steps+1, elev-1, ns))

			if not found1:
				for c in combinations(state[elev], 2):
					ns = deepcopy(state)
					for i in c:
						ns[elev].remove(i)
						ns[elev-1].add(i)
					if is_valid(ns):
						heappush(pq, (steps+1, elev-1, ns))

print('part1',sim(init))
init[0] |= {'mel','gel','mdi','gdi'}
types += ['el','di']
print('part2',sim(init))
