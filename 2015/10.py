#!/usr/bin/env python

infile = '3113322113'
#infile = '1'

def count(infile, num):
	for r in range(num):
		pos = 0
		out = ''
		while pos < len(infile):
			cur = infile[pos]
			pos += 1
			end = pos
			while end < len(infile) and infile[end] == cur:
				end += 1
			out += str(end-pos+1) + str(cur)
			pos = end

		infile = out
	return len(infile)

print 'Part1',count(infile, 40)
print 'Part2',count(infile, 50)