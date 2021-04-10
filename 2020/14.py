#!/usr/bin/env python3

lines = '''mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1'''.split('\n')
lines = open('14.in').read().split('\n')

mem1 = {}
mem2 = {}
curmask = None
for line in lines:
	if line.split(' ')[0] == 'mask':
		curmask = line.split(' = ')[1]
	else:
		val = bin(int(line.split(' = ')[1]))[2:].zfill(36)
		addr = int(line[line.find('[')+1:line.find(']')])
		addrs = bin(addr)[2:].zfill(36)
		res = ''
		p2addrs = ['']
		for i in range(len(val)):
			if curmask[i] == 'X':
				res += val[i]
				temp = []
				for r in p2addrs:
					temp.append(r+'0')
					temp.append(r+'1')
				p2addrs = temp
			else:
				res += curmask[i]
				for i2 in range(len(p2addrs)):
					if curmask[i] == '0':
						p2addrs[i2] += addrs[i]
					else:
						p2addrs[i2] += '1'
		#print(curmask)
		#print(addrs)
		#print(val)
		#print(p2addrs)
		for x in p2addrs:
			mem2[int(x,2)] = int(val,2)
		mem1[addr] = int(res,2)
print('part1',sum(mem1.values()))
print('part2',sum(mem2.values()))