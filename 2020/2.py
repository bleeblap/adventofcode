#!/usr/bin/env python3

import re

lines = '''1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc'''.split('\n')
lines = open('2.in').read().split('\n')

valid1 = 0
valid2 = 0
for line in lines:
	minr,maxr = [int(x) for x in re.findall('(\d+)', line)]
	l = line.split(':')[0].split(' ')[1]
	pasw = line.split(': ')[1]
	if minr <= pasw.count(l) and maxr >= pasw.count(l):
		valid1 += 1
	if int(pasw[minr-1] == l) + int(pasw[maxr-1] == l) == 1:
		valid2 += 1
print('part1',valid1)
print('part2',valid2)