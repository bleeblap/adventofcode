#!/usr/bin/env python3

import math
#from z3 import *

lines = '''939
1789,37,47,1889'''.split('\n')
lines = open('13.in').read().split('\n')

start = int(lines[0])
buses = [int(x) for x in lines[1].split(',') if x is not 'x']

mwait = start
p1 = None
for bus in buses:
	wait = ((start//bus)+1)*bus-start
	if wait < mwait:
		mwait = wait
		p1 = wait*bus
print('part1',p1)

def lcm(a,b):
	return abs(a*b) // math.gcd(a,b)

step = 1
p2 = 0
buses = lines[1].split(',')
blist = []
for i in range(len(buses)):
	if buses[i] == 'x':
		continue
	blist.append((i,int(buses[i])))
for i in range(len(blist)-1):
	step = lcm(step,blist[i][1])
	#print(i,blist[i],step,p2)
	while (p2 + blist[i+1][0]) % blist[i+1][1] != 0:
		p2 += step
print('part2',p2)


'''
s = Solver()
p2 = Int('p2')
buses = lines[1].split(',')
for i in range(len(buses)):
	if buses[i] == 'x':
		continue
	s.add((p2 + i) % int(buses[i]) == 0)
print(s.check())
print(s.model())
'''