#!/usr/bin/env python3

import hashlib
from memorize import memorize

salt = 'abc'
salt = 'cuanljph'

@memorize(maxsize=1024)
def hashrep(seed, rep):
	hsh = hashlib.md5(seed.encode('utf-8')).hexdigest()
	for _ in range(rep):
		hsh = hashlib.md5(hsh.encode('utf-8')).hexdigest()
	return hsh

def solve(rep=0):
	keys = set()
	idx = 0
	while len(keys) < 64:
		hsh = hashrep(salt+str(idx), rep)
		for i in range(len(hsh)-3):
			if hsh[i] == hsh[i+1] == hsh[i+2]:
				for x in range(1, 1000):
					hsh2 = hashrep(salt+str(idx+x), rep)
					for j in range(len(hsh2)-5):
						if hsh[i] == hsh2[j] == hsh2[j+1] == hsh2[j+2] == hsh2[j+3] == hsh2[j+4]:
							#print(idx,hsh,idx+x,hsh2)
							keys.add(hsh)
							break
				break
		idx += 1
	return idx-1

print('part1',solve())
print('part2',solve(2016))

