#!/usr/bin/env python

import re
from itertools import permutations

infile = open('13.in','r').read()
infile2 = '''Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol.'''

rules = {}
for line in infile.split('\n'):
	p1 = line.split(' ')[0]
	op = line.split(' ')[2]
	amt = int(line.split(' ')[3])
	p2 = line.split(' ')[-1].rstrip('.')
	if p1 not in rules:
		rules[p1] = {}
	rules[p1][p2] = amt if op == 'gain' else -amt

def find_max_score(rules):
	maxscore = 0
	for option in permutations(set(x for x in rules.keys())):
		score = 0
		for x in range(len(option)):
			score += rules[option[x]][option[(x+1)%len(option)]]
			score += rules[option[(x+1)%len(option)]][option[x]]
		if score > maxscore:
			#print option
			maxscore = score
	return maxscore

print 'Part1',find_max_score(rules)

rules['me'] = {}
for k,v in rules.items():
	rules['me'][k] = 0
	v['me'] = 0

print 'Part2',find_max_score(rules)