#!/usr/bin/env python3

import hashlib
from heapq import heappush, heappop

opend = ['b','c','d','e','f']
passcode = 'ihgpwlah'

pq = []
p2 = 0
heappush(pq, (0, passcode, (0,0)))
while len(pq) > 0:
	d,path,pos = heappop(pq)
	#print(d,path,pos)
	if pos == (3,3):
		if p2 == 0:
			print('part1',path[len(passcode):])
		p2 = max(p2, len(path)-len(passcode))
	else:
		hsh = hashlib.md5(path.encode('utf-8')).hexdigest()
		if hsh[0] in opend and pos[1] > 0:
			heappush(pq, (len(path)+1, path+'U', (pos[0],pos[1]-1)))
		if hsh[1] in opend and pos[1] < 3:
			heappush(pq, (len(path)+1, path+'D', (pos[0],pos[1]+1)))
		if hsh[2] in opend and pos[0] > 0:
			heappush(pq, (len(path)+1, path+'L', (pos[0]-1,pos[1])))
		if hsh[3] in opend and pos[0] < 3:
			heappush(pq, (len(path)+1, path+'R', (pos[0]+1,pos[1])))
print('part2',p2)