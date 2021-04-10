#!/usr/bin/env python

import re
from itertools import combinations_with_replacement

infile = open('15.in','r').read()
infile2 = '''Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3'''

ingred =[]
for line in infile.split('\n'):
	name = line.split(' ')[0]
	c,d,f,t,cal = map(int, re.findall('-?\d+', line))
	ingred.append((name,c,d,f,t,cal))

maxscore = 0
maxwithcal = 0
for combo in combinations_with_replacement(ingred, 100):
	c = sum([x[1] for x in combo])
	d = sum([x[2] for x in combo])
	f = sum([x[3] for x in combo])
	t = sum([x[4] for x in combo])
	cal = sum([x[5] for x in combo])
	if min(c,d,f,t) <= 0:
		score = 0
		withcal = 0
	else:
		withcal = score = c*d*f*t
		if cal > 500:
			withcal = 0
	if score > maxscore:
		maxscore = score
	if withcal > maxwithcal:
		maxwithcal = withcal

print 'Part1',maxscore
print 'Part2',maxwithcal
