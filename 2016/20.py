#!/usr/bin/env python3

lines = open('20.in').read().split('\n')

ranges = []
for line in lines:
	a,b = [int(x) for x in line.split('-')]
	ranges.append([a,b])

def sim(ranges):
	p1 = 0
	for r in sorted(ranges):
		if p1>=r[0] and p1<=r[1]:
			p1 = r[1]+1
	return p1

print('part1',sim(ranges))

p2 = 0
while True:
	x = sim(ranges)
	if x > 4294967295:
		break
	ranges.append([x,x])
	p2 += 1
print('part2',p2)
