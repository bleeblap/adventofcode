#!/usr/bin/env python

infile = 'hxbxwxba'

def is_valid_pass(password):
	assert len(password) == 8
	straight = 0
	invalid_char = False
	pairs = 0
	pairchrs = []
	for x in range(len(password)-2):
		if ord(password[x])+1 == ord(password[x+1]) and ord(password[x])+2 == ord(password[x+2]):
			straight += 1
	if 'i' in password or 'o' in password or 'l' in password:
		invalid_char = True
	for x in range(len(password)-1):
		if password[x] == password[x+1] and password[x] not in pairchrs:
			pairs += 1
			pairchrs.append(password[x])
	#print straight, invalid_char, pairs
	if straight >= 1 and not invalid_char and pairs >= 2:
		return True
	return False

def increment(password):
	c = ord(password[-1])-ord('a')
	if (c+1) % 26 == 0:
		return increment(password[:-1]) + 'a'
	else:
		return password[:-1] + chr(((c+1)%26)+ord('a'))

while not is_valid_pass(infile):
	infile = increment(infile)
print 'Part1',infile

infile = increment(infile)
while not is_valid_pass(infile):
	infile = increment(infile)
print 'Part2',infile