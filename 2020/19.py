#!/usr/bin/env python3

import re

rin = '''0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb'''

rin = open('19.in').read()

rules = {}
for line in rin.split('\n\n')[0].split('\n'):
	rules[int(line.split(': ')[0])] = line.split(': ')[1]

def makeregex(rule, recur=0):
	if recur > 50:
		return '(NEVER)'
	if 'a' in rules[rule]:
		return 'a'
	elif 'b' in rules[rule]:
		return 'b'
	elif '|' in rules[rule]:
		p = '('
		for op in rules[rule].split(' | '):
			for op2 in op.split(' '):
				p += makeregex(int(op2),recur+1)
			p += '|'
		return p[:-1]+')'
	else:
		p = ''
		for op in rules[rule].split(' '):
			p += makeregex(int(op),recur+1)
		return p

rec = re.compile('^'+makeregex(0)+'$')
p1 = 0
for line in rin.split('\n\n')[1].split('\n'):
	if rec.match(line):
		p1 += 1
print('part1',p1)

rules[8] = '42 | 42 8'
rules[11] = '42 31 | 42 11 31'
rec = re.compile('^'+makeregex(0)+'$')
p2 = 0
for line in rin.split('\n\n')[1].split('\n'):
	if rec.match(line):
		p2 += 1
print('part2',p2)