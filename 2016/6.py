#!/usr/bin/env python3

lines = open('6.in').read().split('\n')
stats = [{} for x in range(len(lines[0]))]
for line in lines:
	for p in range(len(line)):
		if line[p] in stats[p]:
			stats[p][line[p]] += 1
		else:
			stats[p][line[p]] = 1

part1 = ''
part2 = ''
for s in stats:
	part1 += max(s.keys(), key=(lambda k: s[k]))
	part2 += min(s.keys(), key=(lambda k: s[k]))
print('part1 '+part1)
print('part2 '+part2)