#!/usr/bin/env python

from itertools import combinations

infile = open('17.in','r').read()
nums = map(int, infile.split('\n'))

matching = []
for r in range(len(nums)):
	matching.extend(filter(lambda y: sum(y)==150, combinations(nums,r)))

print 'Part1',len(matching)
print 'Part2',len([x for x in matching if len(x)==len(matching[0])])