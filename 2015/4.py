#!/usr/bin/env python

import hashlib

infile = 'iwrupvqb'

count = 0
while True:
	if hashlib.md5(infile+str(count)).hexdigest()[:5] == '0'*5:
		print 'Part1',count
		break
	count += 1

while True:
	if hashlib.md5(infile+str(count)).hexdigest()[:6] == '0'*6:
		print 'Part2',count
		break
	count += 1