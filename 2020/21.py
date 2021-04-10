#!/usr/bin/env python3

from copy import copy

lines = '''mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)'''.split('\n')
lines = open('21.in').read().split('\n')

foodlist = []
alli = set()
alla = set()
for line in lines:
	f = {}
	f['i'] = set(line.split(' (')[0].split(' '))
	alli |= f['i']
	f['a'] = set(line.split('contains ')[1].split(')')[0].split(', '))
	alla |= f['a']
	foodlist.append(f)

posslist = {}
for al in alla:
	poss = copy(alli)
	for f in foodlist:
		if al in f['a']:
			poss &= f['i']
	posslist[al] = poss
	#print(al,poss)

confirm = {}
while len(posslist) > 0:
	for p in posslist:
		if len(posslist[p]) == 1:
			confirm[p] = posslist[p].pop()
			for q in posslist:
				if confirm[p] in posslist[q]:
					posslist[q].remove(confirm[p])
			del posslist[p]
			#print(confirm)
			#print(posslist)
			break
p1 = 0
for i in (alli - set(confirm.values())):
	for f in foodlist:
		if i in f['i']:
			p1 += 1
print('part1',p1)

p2 = ','.join([confirm[c] for c in sorted(confirm)])
print('part2',p2)