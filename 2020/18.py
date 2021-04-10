#!/usr/bin/env python3


lines = ['1 + 2 * 3 + 4 * 5 + 6',
'2 * 3 + (4 * 5)',
'5 + (8 * 3 + 9 + 3 * 4 * 3)',
'5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))',
'((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2']
lines = open('18.in').read().split('\n')

def matchclose(line):
	if line[0] != '(':
		print('wrong',line)
		return None
	n = 1
	for i in range(1,len(line)):
		if line[i] == '(':
			n += 1
		elif line[i] == ')':
			n -= 1
		if n == 0:
			return i 

def reval(line, op1=None):
	#print('reval({}, {})'.format(line,op1))

	i = 0
	if op1 is None:
		if '0' <= line[i] <= '9':
			op1 = int(line[i])
		elif line[i] == '(':
			end = matchclose(line[i:])
			op1 = reval(line[i+1:i+end])
			i += end
		else:
			print('unk',line[i])
		i += 1
		
	if line[i] != ' ':
		print('unk1',line[i])
	i += 1
	
	opr = line[i]
	if opr not in ['+','*']:
		print('unk opr',opr)
	i += 1
	
	if line[i] != ' ':
		print('unk3',line[i])
	i += 1
	
	if '0' <= line[i] <= '9':
		op2 = int(line[i])
	elif line[i] == '(':
		end = matchclose(line[i:])
		op2 = reval(line[i+1:i+end])
		i += end
	else:
		print('unk4',line[i])
	i+= 1

	foo = '{} {} {}'.format(op1,opr,op2)
	res = eval(foo)
	#print('{} = {}'.format(foo,res))
	if len(line) > i:
		return reval(line[i:],res)
	return res

def reval2(line, op1=None):
	#print('reval2',line)

	while '(' in line:
		start = line.index('(')
		end = matchclose(line[start:])
		line = line[:start] + str(reval2(line[start+1:start+end])) + line[start+end+1:]
		#print(line)

	while '+' in line:
		i = line.index('+')
		s = i-2
		e = i+2
		while s > 0 and line[s] != ' ':
			s -= 1
		while e < len(line) and line[e] != ' ':
			e += 1

		op1 = int(line[s:i-1])
		op2 = int(line[i+1:e])
		line = line[:s] + ' ' + str(op1+op2) + line[e:]
		#print('{}+{} => {}'.format(op1,op2,line))

	#print('eval',line)
	return eval(line)

p1 = 0
p2 = 0
for line in lines:
	#print('DONE {} = {}'.format(line,reval2(line)))
	p1 += reval(line)
	p2 += reval2(line)

print('part1',p1)
print('part2',p2)
