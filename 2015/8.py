#!/usr/bin/env python

from StringIO import StringIO
import re

infile = open('8.in','r').read()

out = StringIO()
inlen = 0
p2len = 0
for line in infile.split('\n'):
	out.write(eval(line))
	inlen += len(line)
	p2len += len(re.escape(line))+2

print 'Part1',inlen-len(out.getvalue())
print 'Part2',p2len-inlen