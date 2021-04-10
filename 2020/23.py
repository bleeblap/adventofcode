#!/usr/bin/env python3

nums = [int(x) for x in '389125467']
nums = [int(x) for x in '219748365']

gmin = min(nums)
gmax = max(nums)
glookup = {}

class node:
	def __init__(self, num):
		self.num = num
		self.next = None

def initnodes(nums,p2=False):
	head = node(nums[0])
	glookup[nums[0]] = head
	cur = head
	for n in nums[1:]:
		nxt = node(n)
		glookup[n] = nxt
		cur.next = nxt
		cur = nxt
	if p2:
		nexti = 10
		while nexti <= 1000000:
			nxt = node(nexti)
			glookup[nexti] = nxt
			cur.next = nxt
			cur = nxt
			nexti += 1
	cur.next = head
	return head

def dump(head):
	ptr = head
	while ptr.next != head:
		print(ptr.num,end=',')
		ptr = ptr.next
	print(ptr.num)	

def sim(cur,niter):
	move = 1
	while move <= niter:
		#print('move',move)
		#print('cur',cur.num)
		#dump(cur)
		pick = cur.next
		cur.next = pick.next.next.next
		pick.next.next.next = pick
		#dump(pick)
		dst = cur.num-1
		if dst < gmin:
			dst = gmax
		while dst in [pick.num,pick.next.num,pick.next.next.num]:
			dst -= 1
			if dst < gmin:
				dst = gmax
		#print('dest',dst,'\n')
		dnode = glookup[dst]
		pick.next.next.next = dnode.next
		dnode.next = pick
		cur = cur.next
		move += 1
	return cur

cur = initnodes(nums)
cur = sim(cur,100)
p1 = ''
ptr = glookup[1].next
while ptr.num != 1:
	p1 += str(ptr.num)
	ptr = ptr.next
print('part1',p1)

glookup = {}
gmax = 1000000
cur = initnodes(nums,True)
cur = sim(cur,10000000)
one = glookup[1]
print('part2',one.next.num*one.next.next.num)
