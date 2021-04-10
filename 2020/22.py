#!/usr/bin/env python3

from copy import copy

lines = '''Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10'''
lines = open('22.in').read()

p1 = []
p2 = []
for card in lines.split('\n\n')[0].split('\n')[1:]:
	p1.append(int(card))
for card in lines.split('\n\n')[1].split('\n')[1:]:
	p2.append(int(card))

def play(p1,p2,recur=False):
	ground = 0
	history = set()
	while len(p1) > 0 and len(p2) > 0:
		test = (''.join([str(x) for x in p1]),''.join([str(x) for x in p2])) 
		if test in history:
			#print('loop')
			return ([None],[])
		history.add(test)
		#print(p1)
		#print(p2)
		#print('play',p1[0],p2[0])
		if recur and p1[0] < len(p1) and p2[0] < len(p2):
			#print('recur')
			sub1,sub2 = play(copy(p1[1:p1[0]+1]),copy(p2[1:p2[0]+1]), True)
			if len(sub1) == 0:
				#print('p2 win recur')
				t = p2[0]
				p2.append(t)
				p2.append(p1[0])
				p1 = p1[1:]
				p2 = p2[1:]
			else:
				#print('p1 win recur')
				t = p1[0]
				p1.append(t)
				p1.append(p2[0])
				p1 = p1[1:]
				p2 = p2[1:]
		else:
			if p1[0] > p2[0]:
				t = p1[0]
				p1.append(t)
				p1.append(p2[0])
				p1 = p1[1:]
				p2 = p2[1:]
			else:
				t = p2[0]
				p2.append(t)
				p2.append(p1[0])
				p1 = p1[1:]
				p2 = p2[1:]
		ground += 1
		#print(ground,p1,p2)
	return (p1, p2)

end1,end2 = play(copy(p1),copy(p2))
win = end1 if len(end1) > 0 else end2
part1 = 0
for i in range(len(win)):
	part1 += (len(win)-i)*win[i]
print('part1', part1)

end1,end2 = play(copy(p1),copy(p2),True)
win = end1 if len(end1) > 0 else end2
part2 = 0
for i in range(len(win)):
	part2 += (len(win)-i)*win[i]
print('part2', part2)