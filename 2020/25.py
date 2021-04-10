#!/usr/bin/env python3

lines = '''5764801
17807724'''.split('\n')
lines = open('25.in').read().split('\n')

pubs = [int(x) for x in lines]
rounds = [None,None]

val = 1
i = 1
while None in rounds:
	val = (val*7)%20201227
	#print(val)
	if val == pubs[0]:
		rounds[0] = i
	if val == pubs[1]:
		rounds[1] = i
	i += 1

val = 1
for i in range(rounds[1]):
	val = (val*pubs[0])%20201227
print('part1',val)
