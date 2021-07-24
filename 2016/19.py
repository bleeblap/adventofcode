#!/usr/bin/env python3

from collections import deque

state = deque()
for i in range(3005290):
	state.append((i+1))

while len(state) > 1:
	a = state.popleft()
	b = state.popleft()
	state.append(a)
	
print('part1',state.pop())

class Node:
	def __init__(self,id):
		self.id  = id
		self.nxt = None
		self.prv = None

	def delete(self):
		self.prv.nxt = self.nxt
		self.nxt.prv = self.prv

state = []
N = 3005290
for i in range(N):
	state.append(Node(i+1))
for i in range(len(state)):
	state[i].nxt = state[(i+1)%N]
	state[i].prv = state[(i-1)%N]

cur = state[0]
mid = state[N//2]
for i in range(len(state)-1):
	nm = mid.nxt
	mid.delete()
	mid = nm
	if i % 2 == 1:
		mid = mid.nxt
	cur = cur.nxt
print('part2',cur.id)
