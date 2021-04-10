#!/usr/bin/env python

import re
from itertools import permutations

infile = open('14.in','r').read()
infile2 = '''Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.'''

racers = {}
for line in infile.split('\n'):
	speed, time, rest = map(int, re.findall('\d+', line))
	racer = line.split(' ')[0]
	racers[racer] = {'speed':speed, 'time':time, 'rest':rest, 'pos':0,
						'racing':time, 'resting':0, 'score':0}

for r in range(1,2503+1):
	for v in racers.values():
		if v['racing'] > 0:
			v['pos'] += v['speed']
			v['racing'] -= 1
			if v['racing'] == 0:
				v['resting'] = v['rest']
		elif v['resting'] > 0:
			v['resting'] -= 1
			if v['resting'] == 0:
				v['racing'] = v['time']
		else:
			raise (k,v)
	winpos = max([r['pos'] for r in racers.values()])
	for v in racers.values():
		if v['pos'] == winpos:
			v['score'] += 1

print 'Part1', max([r['pos'] for r in racers.values()])
print 'Part2', max([r['score'] for r in racers.values()])
# 2688 TOO LOW