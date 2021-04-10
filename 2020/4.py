#!/usr/bin/env python3

import re

lines = open('4.in').read()

part1 = 0
part2 = 0
for passp in lines.split('\n\n'):
	pdict = {}
	for line in passp.split('\n'):
		for kv in line.split(' '):
			k,v = kv.split(':')
			pdict[k] = v
	if len(pdict) == 8 or (len(pdict) == 7 and 'cid' not in pdict):
		part1 += 1

		if int(pdict['byr']) < 1920 or int(pdict['byr']) > 2002:
			continue
		if int(pdict['iyr']) < 2010 or int(pdict['iyr']) > 2020:
			continue
		if int(pdict['eyr']) < 2020 or int(pdict['eyr']) > 2030:
			continue
		if 'cm' in pdict['hgt']:
			h = int(pdict['hgt'][:-2])
			if h < 150 or h > 193:
				continue
		elif 'in' in pdict['hgt']:
			h = int(pdict['hgt'][:-2])
			if h < 59 or h > 76:
				continue
		else:
			continue
		if not re.match('^#[0-9a-f]{6}$', pdict['hcl']):
			continue
		if pdict['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
			continue
		if not re.match('^[0-9]{9}$', pdict['pid']):
			continue

		part2 += 1

print('part1',part1)
print('part2',part2)

