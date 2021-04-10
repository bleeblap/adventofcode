#!/usr/bin/env python

infile = open('1.in','r').read()

print 'Part1',infile.count('(')-infile.count(')')

floor = 0
for x in range(len(infile)):
	floor += 1 if infile[x] == '(' else -1
	if floor == -1:
		print 'Part2',x+1
		break