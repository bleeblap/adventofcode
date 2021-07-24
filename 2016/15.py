#!/usr/bin/env python3

lines = '''Disc #1 has 5 positions; at time=0, it is at position 4.
Disc #2 has 2 positions; at time=0, it is at position 1.'''.split('\n')
lines = open('15.in').read().split('\n')

discs = []
for line in lines:
	npos = int(line.split(' ')[3])
	spos = int(line.split(' ')[11][:-1])
	discs.append((npos, spos))

def sim(discs):
	t = 0
	while True:
		success = True
		for i in range(len(discs)):
			if (t+i+1+discs[i][1]) % discs[i][0]:
				success = False
				break
		if success:
			return t
		t += 1

print('part1',sim(discs))
discs.append((11,0))
print('part2',sim(discs))