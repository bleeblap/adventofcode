#!/usr/bin/env python

import re
from heapq import heappush, heappop

infile = open('19.in').read()
infile2 = '''H => HO
H => OH
O => HH
e => H
e => O

HOHOHO'''

rules = {}
for line in infile.split('\n\n')[0].split('\n'):
	a,b = line.split(' => ')
	if a in rules:
		rules[a].append(b)
	else:
		rules[a] = [b]
mol = infile.split('\n\n')[1]

res = set()
for rule in rules:
	for match in re.finditer(rule, mol):
		for out in rules[rule]:
			res.add(mol[:match.start()]+out+mol[match.end():])

print 'Part1',len(res)

pq = []
heappush(pq,(len(mol),0,mol))

while True:
	l,hops,cmol = heappop(pq)
	#print l,hops,cmol
	if l == 1 and cmol == 'e':
		print 'Part2',hops
		break
	for k,v in rules.items():
		for r in v:
			for match in re.finditer(r,cmol):
				newmol = cmol[:match.start()]+k+cmol[match.end():]
				heappush(pq,(len(newmol),hops+1,newmol))