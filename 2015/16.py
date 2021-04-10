#!/usr/bin/env python

infile = open('16.in','r').read()

target = {'children': 3,
'cats': 7,
'samoyeds': 2,
'pomeranians': 3,
'akitas': 0,
'vizslas': 0,
'goldfish': 5,
'trees': 3,
'cars': 2,
'perfumes': 1}

for line in infile.split('\n'):
	suenum = int(line.split(' ')[1].rstrip(':'))
	p1match = True
	p2match = True
	for val in ':'.join(line.split(':')[1:]).split(','):
		k,v = map(lambda x:x.lstrip(), val.split(':'))
		if target[k] != int(v):
			p1match = False
		if k in ['cats', 'trees']:
			if target[k] >= int(v):
				p2match = False
		elif k in ['pomeranians', 'goldfish']:
			if target[k] <= int(v):
				p2match = False
		else:
			if target[k] != int(v):
				p2match = False
	if p1match:
		print 'Part1',suenum
	if p2match:
		print 'Part2',suenum