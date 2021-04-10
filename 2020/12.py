#!/usr/bin/env python3

lines = open('12.in').read().split('\n')

pos = complex(0,0)
pos2 = complex(0,0)
way = complex(10,1)
cdir = complex(1,0)
dirs = {'N':complex(0,1), 'S':complex(0,-1), 'E':complex(1,0), 'W':complex(-1,0)}

for line in lines:
	d = int(line[1:])
	if line[0] == 'F':
		pos += d*cdir
		pos2 += d*way
	elif line[0] == 'R':
		for _ in range(d//90):
			cdir *= complex(0,-1)
			way *= complex(0,-1)
	elif line[0] == 'L':
		for _ in range(d//90):
			cdir *= complex(0,1)
			way *= complex(0,1)
	else:
		pos += d*dirs[line[0]]
		way += d*dirs[line[0]]
	#print(line,pos2,way)

print('part1',int(abs(pos.real)+abs(pos.imag)))
print('part2',int(abs(pos2.real)+abs(pos2.imag)))