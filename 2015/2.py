#!/usr/bin/env python

import re 

infile = open('2.in','r').read()

area = 0
ribbon = 0
for line in infile.split('\n'):
	l,w,h = map(int, re.findall('\d+',line))
	area += min(l*w,l*h,w*h) + 2*l*w + 2*l*h + 2*w*h
	ribbon += (sum([l,w,h])-max([l,w,h]))*2 + l*w*h

print 'Part1',area
print 'Part2',ribbon