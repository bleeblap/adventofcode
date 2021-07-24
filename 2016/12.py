#!/usr/bin/env python3

lines = '''cpy 41 a
inc a
inc a
dec a
jnz a 2
dec a'''.split('\n')
lines = open('12.in').read().split('\n')

def solve(reg):
	ip = 0
	while ip < len(lines):
		cmd = lines[ip].split(' ')[0]
		if cmd == 'cpy':
			_,one,two = lines[ip].split(' ')
			if one in 'abcd':
				reg[two] = reg[one]
			else:
				reg[two] = int(one)
		elif cmd == 'inc':
			reg[lines[ip].split(' ')[1]] += 1
		elif cmd == 'dec':
			reg[lines[ip].split(' ')[1]] -= 1
		elif cmd == 'jnz':
			_,one,two = lines[ip].split(' ')
			if one in 'abcd':
				if reg[one] != 0:
					ip += int(two) - 1
			elif int(one) != 0:
				ip += int(two) - 1 
		else:
			print('unk cmd', cmd)
		ip += 1
	return reg['a']

reg = {'a':0,'b':0,'c':0,'d':0}
print('part1',solve(reg))
reg = {'a':0,'b':0,'c':1,'d':0}
print('part2',solve(reg))