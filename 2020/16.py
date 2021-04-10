#!/usr/bin/env python3

inp = '''class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9'''
inp = open('16.in').read()

sections = inp.split('\n\n')
rules = {}
for line in sections[0].split('\n'):
	cat,ranges = line.split(':')
	rules[cat] = []
	for rule in ranges.split(' or '):
		start,end = [int(x) for x in rule.split('-')]
		rules[cat].append((start,end))
#print(rules)

p1 = 0
vnear = []
for nearby in sections[2].split('\n')[1:]:
	allvalid = True
	for test in [int(x) for x in nearby.split(',')]:
		valid = False
		for r in rules:
			for check in rules[r]:
				if check[0] <= test <= check[1]:
					valid = True
		if not valid:
			p1 += test
			allvalid = False
	if allvalid:
		vnear.append(nearby)

print('part1',p1)

ruleoptions = {}
for pos in range(len(rules)):
	for r in rules:
		allmatch = True
		for v in vnear:
			vt = int(v.split(',')[pos])
			anycheck = False
			for check in rules[r]:
				if check[0] <= vt <= check[1]:
					anycheck = True
			if not anycheck:
				allmatch = False
		if allmatch:
			if r in ruleoptions:
				ruleoptions[r].append(pos)
			else:
				ruleoptions[r] = [pos]

rulemap = {}
for rule in sorted(ruleoptions, key = lambda x: len(ruleoptions[x])):
	#print(rule,ruleoptions[rule])
	for x in ruleoptions[rule]:
		if x not in rulemap:
			rulemap[x] = rule
#print(rulemap)

p2 = 1
ticket = [int(x) for x in sections[1].split('\n')[1].split(',')]
for f in range(len(ticket)):
	if rulemap[f].startswith('departure'):
		p2 *= ticket[f]
print('part2',p2) 
# too low 614