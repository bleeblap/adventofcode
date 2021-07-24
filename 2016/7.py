#!/usr/bin/env python3

lines = open('7.in').read().split('\n')
#lines = ['abba[mnop]qrst','abcd[bddb]xyyx','aaaa[qwer]tyui','ioxxoj[asdfgh]zxcvbn']
part1 = 0
part2 = 0

for line in lines:
	inBracket = False
	foundOut = False
	foundIn = False
	ABAs = set()
	BABs = set()
	for pos in range(len(line)-2):
		if line[pos] == '[':
			inBracket = True
			continue
		elif line[pos] == ']':
			inBracket = False
			continue
		if pos<len(line)-3 and line[pos] == line[pos+3] and line[pos+1] == line[pos+2] and line[pos] != line[pos+1]:
			if inBracket:
				foundIn = True
			else:
				foundOut = True
		if line[pos] == line[pos+2] and line[pos] != line[pos+1] and line[pos+1] not in '[]':
			if inBracket:
				BABs.add(line[pos:pos+3])
			else:
				ABAs.add(line[pos:pos+3])
	if foundOut and not foundIn:
		part1 += 1
	for a in ABAs:
		if a[1]+a[0]+a[1] in BABs:
			part2 += 1
			break

print('part1',part1)
print('part2',part2)