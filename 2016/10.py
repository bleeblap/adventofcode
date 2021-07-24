#!/usr/bin/env python3

lines = '''value 5 goes to bot 2
bot 2 gives low to bot 1 and high to bot 0
value 3 goes to bot 1
bot 1 gives low to output 1 and high to bot 0
bot 0 gives low to output 2 and high to output 0
value 2 goes to bot 2'''.split('\n')
lines = open('10.in').read().split('\n')

N = 300
bots = [[] for _ in range(N)]
output = [[] for _ in range(N)]
rules = [None for _ in range(N)]
for line in lines:
	if line.startswith('value'):
		v = int(line.split(' ')[1])
		b = int(line.split(' ')[5])
		bots[b].append(v)
	else:
		src = int(line.split(' ')[1])
		ltype = line.split(' ')[5]
		ldst = int(line.split(' ')[6])
		htype = line.split(' ')[10]
		hdst = int(line.split(' ')[11])
		rules[src] = (ltype,ldst,htype,hdst)

while True:
	term = False
	for b in range(len(bots)):
		if len(bots[b]) == 2:
			if 61 in bots[b] and 17 in bots[b]:
				print('part1',b)
			if rules[b][0] == 'output':
				output[rules[b][1]].append(min(bots[b]))
			else:
				bots[rules[b][1]].append(min(bots[b]))
			if rules[b][2] == 'output':
				output[rules[b][3]].append(max(bots[b]))
			else:
				bots[rules[b][3]].append(max(bots[b]))
			bots[b] = []
			term = True
			break
	if not term:
		break

print('part2',output[0][0]*output[1][0]*output[2][0])