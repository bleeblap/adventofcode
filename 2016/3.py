#!/usr/bin/env python3
import re

lines = open('3.in').read().split('\n')
part1 = 0
for line in lines:
	a,b,c = [int(x) for x in re.findall('(\d+)', line)]
	if a+b>c and a+c>b and b+c>a:
		part1+=1
print('part1',part1)

part2 = 0
for x in range(0,len(lines),3):
	a1,b1,c1 = [int(x) for x in re.findall('(\d+)', lines[x])]
	a2,b2,c2 = [int(x) for x in re.findall('(\d+)', lines[x+1])]
	a3,b3,c3 = [int(x) for x in re.findall('(\d+)', lines[x+2])]
	if a1+a2>a3 and a1+a3>a2 and a2+a3>a1:
		part2+=1
	if b1+b2>b3 and b1+b3>b2 and b2+b3>b1:
		part2+=1
	if c1+c2>c3 and c1+c3>c2 and c2+c3>c1:
		part2+=1
print('part2',part2)