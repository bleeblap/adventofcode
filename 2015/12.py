#!/usr/bin/env python

import re
import json

infile = open('12.in','r').read()

print 'Part1',sum(map(int, re.findall('-?\d+',infile)))

def recur_count(js):
	if type(js) == list:
		return sum([recur_count(x) for x in js])
	elif type(js) == dict:
		foundRed = False
		s = 0
		for k,v in js.items():
			if v == 'red':
				foundRed = True
			s += recur_count(v)
		return 0 if foundRed else s
	elif type(js) == int:
		return js
	else:
		#print type(js),js
		return 0

print 'Part2',recur_count(json.loads(infile))