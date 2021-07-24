#!/usr/bin/env python3

from itertools import permutations

lines = '''swap position 4 with position 0
swap letter d with letter b
reverse positions 0 through 4
rotate left 1 step
move position 1 to position 4
move position 3 to position 0
rotate based on position of letter b
rotate based on position of letter d'''.split('\n')
lines = open('21.in').read().split('\n')

def rotater(value):
	return value[-1]+value[:-1]
def rotatel(value):
	return value[1:]+value[0]

def scramble(value):
	for line in lines:
		cmd1,cmd2 = line.split(' ')[:2]
		if cmd1 == 'swap':
			if cmd2 == 'position':
				a = int(line.split(' ')[2])
				b = int(line.split(' ')[5])
			elif cmd2 == 'letter':
				a = value.index(line.split(' ')[2])
				b = value.index(line.split(' ')[5])
			ta = value[a]
			tb = value[b]
			value = value[:b]+ta+value[b+1:]
			value = value[:a]+tb+value[a+1:]	
		elif cmd1 == 'reverse':
			a = int(line.split(' ')[2])
			b = int(line.split(' ')[4])
			value = value[:a]+value[a:b+1][::-1]+value[b+1:]
		elif cmd1 == 'rotate':
			if cmd2 == 'based':
				a = line.split(' ')[6]
				ta = value.index(a)
				steps = ta+1
				if ta >= 4:
					steps += 1
				for _ in range(steps):
					value = rotater(value)
			else:
				steps = int(line.split(' ')[2])
				for _ in range(steps):
					if cmd2 == 'left':
						value = rotatel(value)
					else:
						value = rotater(value)
		elif cmd1 == 'move':
			a = int(line.split(' ')[2])
			b = int(line.split(' ')[5])
			t = value[a]
			value = value[:a]+value[a+1:]
			value = value[:b]+t+value[b:]
		#print(line, value)
	return value

print('part1', scramble('abcdefgh'))
for test in [''.join(x) for x in permutations('abcdefgh')]:
	if scramble(test) == 'fbgdceah':
		print('part2',test)
		break