#!/usr/bin/env python3

def step(inp):
	b = ['0' if i == '1' else '1' for i in inp[::-1]]
	return inp + '0' + ''.join(b)

def check(inp):
	return ''.join(['1' if inp[i*2:i*2+2] in ['00','11'] else '0' for i in range(len(inp)//2)])

def sim(data, l):
	while len(data) < l:
		data = step(data)
	data = data[:l]
	while len(data) % 2 == 0:
		data = check(data)
	return data

data = '11110010111001001'
print('part1',sim(data, 272))
print('part2',sim(data, 35651584))
