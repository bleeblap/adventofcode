#!/usr/bin/env python3

import hashlib

doorid = open('5.in').read()
#doorid = 'abc'

part1 = ''
part2 = '????????'
c=0
while len(part1)<8 or '?' in part2:
	t = hashlib.md5((doorid+str(c)).encode('utf-8')).hexdigest()
	if t[:5] == '00000':
		part1 += t[5:6]
		print('1',part1)
		p = int(t[5:6],16)
		if p < 8 and part2[p] == '?':
			part2 = part2[:p] + t[6:7] + part2[p+1:]
			print('2',part2)
	c+=1

print('part1',part1[:8])
print('part2',part2)