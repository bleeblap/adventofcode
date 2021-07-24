#!/usr/bin/env python3

lines = '''cpy 2 a
tgl a
tgl a
tgl a
cpy 1 a
dec a
dec a'''.split('\n')
lines = open('23.in').read().split('\n')

def solve(reg):
	ip = 0
	while ip >= 0 and ip < len(lines):
		#print(ip,lines[ip],reg)
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
			if two in 'abcd':
				two = int(reg[two])
			if one in 'abcd':
				if reg[one] != 0:
					ip += int(two) - 1
			elif int(one) != 0:
				ip += int(two) - 1
		elif cmd == 'tgl':
			one = lines[ip].split(' ')[1]
			tglip = ip + reg[one]
			if tglip >= 0 and tglip < len(lines):
				debugorig = lines[tglip]
				tglcmd = lines[tglip].split(' ')[0]
				if len(lines[tglip].split(' ')) == 2:
					if tglcmd == 'inc':
						lines[tglip] = 'dec ' + lines[tglip].split(' ')[1]
					else:
						lines[tglip] = 'inc ' + lines[tglip].split(' ')[1]
				else:
					if tglcmd == 'jnz':
						lines[tglip] = 'cpy ' + ' '.join(lines[tglip].split(' ')[1:])
					else:
						lines[tglip] = 'jnz ' + ' '.join(lines[tglip].split(' ')[1:])
				#print('tgl[{}] {} -> {}'.format(tglip,debugorig,lines[tglip]))
		else:
			print('unk cmd', cmd)
		ip += 1
	return reg['a']

reg = {'a':7,'b':0,'c':0,'d':0}
print('part1',solve(reg))
reg = {'a':12,'b':0,'c':0,'d':0}
lines = open('23.in').read().split('\n')
print('part2',solve(reg))


'''
tgl[24] inc c -> dec c
tgl[22] inc d -> dec d
tgl[20] jnz 81 d -> cpy 81 d
tgl[18] jnz 1 c -> cpy 1 c

	cpy a b			# b = a
	dec b			# b--
D:	cpy a d			# d = a
	cpy 0 a			# a = 0
B:	cpy b c 		# c = b
A:	inc a 			# a++
	dec c 			# c--
	jnz c -2 		# if (c) goto A
	dec d 			# d--
	jnz d -5 		# if (d) goto B
	dec b 			# b--
	cpy b c 		# c = b
	cpy c d 		# d = c
C:	dec d 			# d--
	inc c 			# c++
	jnz d -2		# if (d) goto C
	tgl c 			# ...
	cpy -16 c 		# c = -16
	jnz 1 c 		# if (true) goto D
	cpy 90 c 		# c = 90
F:	jnz 81 d 		# if (true) goto reg[d] // but reg[d] is 0 so nop until tgl I guess
E:	inc a 			# a++
	inc d 			# d++
	jnz d -2 		# if (d) goto E
	inc c 			# c++
	jnz c -5 		# if (c) goto F
'''

