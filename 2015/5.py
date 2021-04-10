#!/usr/bin/env python

import re

infile = open('5.in','r').read()

nice = 0
for line in infile.split('\n'):
	vowels = sum([line.count(c) for c in 'aeiou'])
	doubles = re.findall(r'(.)\1', line)
	bad = sum(int(x in line) for x in ['ab','cd','pq','xy'])
	if vowels>=3 and len(doubles)>0 and bad==0:
		nice += 1

print 'Part1',nice

nice = 0
for line in infile.split('\n'):
	pairs = 0
	splits = 0
	for x in range(len(line)-1):
		if line.count(line[x:x+2]) >= 2:
			pairs += 1
		if x > 0 and line[x-1] == line[x+1]:
			splits += 1
	if pairs >=1 and splits >= 1:
		nice += 1
print 'Part2',nice

