#!/usr/bin/env python3

inp = open('9.in').read().strip('\n')
#inp = 'A(1x5)BC'
#inp = '(3x3)XYZ'
#inp = 'A(2x2)BCD(2x2)EFG'
#inp = '(6x1)(1x3)A'
#inp = 'X(8x2)(3x3)ABCY'
#inp = '(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN'
pos = 0

while pos < len(inp):
	if inp[pos] == '(':
		strpos = inp.index(')', pos)
		n,r = [int(x) for x in inp[pos+1:strpos].split('x')]
		inp = inp[:pos] + inp[strpos+1:strpos+1+n]*r + inp[strpos+n+1:]
		pos = pos + n*r
	else:
		pos += 1

print('part1',len(inp))

def p2_len(inp):
	if '(' in inp:
		pos = inp.index('(')
		strpos = inp.index(')',pos)
		n,r = [int(x) for x in inp[pos+1:strpos].split('x')]
		return p2_len(inp[:pos]) + p2_len(inp[strpos+1:strpos+1+n])*r + p2_len(inp[strpos+n+1:])
	else:
		return len(inp)

print('part2',p2_len(inp))