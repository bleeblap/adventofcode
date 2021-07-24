#!/usr/bin/env python3

lines = open('2.in').read().split('\n')

keypad = [
	[1,2,3],
	[4,5,6],
	[7,8,9]
]
pos = [1,1]
part1 = ''

for line in lines:
	for char in line:
		if char == 'U' and pos[0]>0:
			pos[0] -= 1
		elif char == 'R' and pos[1]<2:
			pos[1] += 1
		elif char == 'D' and pos[0]<2:
			pos[0] += 1
		elif char == 'L' and pos[1]>0:
			pos[1] -= 1
	part1 += str(keypad[pos[0]][pos[1]])

print('part1',part1)

keypad = [
	[0, 0, 1, 0, 0],
	[0, 2, 3, 4, 0],
	[5, 6, 7, 8, 9],
	[0, 'A', 'B', 'C', 0],
	[0, 0, 'D', 0, 0]
]
pos = [2,0]
part2=''
for line in lines:
	for char in line:
		if char == 'U' and pos[0]>0 and keypad[pos[0]-1][pos[1]] != 0:
			pos[0] -= 1
		elif char == 'R' and pos[1]<4 and keypad[pos[0]][pos[1]+1] != 0:
			pos[1] += 1
		elif char == 'D' and pos[0]<4 and keypad[pos[0]+1][pos[1]] != 0:
			pos[0] += 1
		elif char == 'L' and pos[1]>0 and keypad[pos[0]][pos[1]-1] != 0:
			pos[1] -= 1
	part2 += str(keypad[pos[0]][pos[1]])

print('part2',part2)