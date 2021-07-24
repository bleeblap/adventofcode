#!/usr/bin/env python3

row = open('18.in').read()

def sim(row, rounds):
	res = row.count('.')
	for r in range(rounds-1):
		n = ''
		p = '.' + row + '.'
		for i in range(1,len(p)-1):
			n += '^' if p[i-1:i+2] in ['^^.', '.^^', '^..', '..^'] else '.'
		res += n.count('.')
		row = n
	return res

#print(sim('.^^.^.^^^^', 10))
print('part1',sim(row, 40))
print('part2',sim(row, 400000))