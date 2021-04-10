#!/usr/bin/env python3

lines = open('6.in').read()

part1 = 0
part2 = 0
for group in lines.split('\n\n'):
	p1 = set()
	p2 = None
	for line in group.split('\n'):
		temp = set()
		for char in line:
			temp.add(char)
		p1 |= temp
		p2 = temp if p2 is None else temp&p2
	part1 += len(p1)
	part2 += len(p2)
print('part1',part1)
print('part2',part2)