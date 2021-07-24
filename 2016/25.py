#!/usr/bin/env python3

lines = '''cpy 2 a
tgl a
tgl a
tgl a
cpy 1 a
dec a
dec a'''.split('\n')
lines = open('25.in').read().split('\n')

def solve(reg, MAXI):
	ip = 0
	output = ''
	instc = 0
	while ip >= 0 and ip < len(lines) and instc < MAXI:
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
		elif cmd == 'out':
			one = lines[ip].split(' ')[1]
			if one in 'abcd':
				output += str(reg[one])
			else:
				output += str(one)
		else:
			print('unk cmd', cmd)
		ip += 1
		instc += 1
	return output

p1 = 0
while True:
	reg = {'a':p1,'b':0,'c':0,'d':0}
	pattern = solve(reg, 100000)
	#print(p1,pattern)
	found = True
	for i in range(len(pattern)):
		if (i % 2 == 0 and pattern[i] != '0') or (i % 2 == 1 and pattern[i] != '1'):
			found = False
	if found:
		print('part1',p1)
		break
	p1 += 1

