#!/usr/bin/env python3

lines = '''28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3'''.split('\n')
lines = open('10.in').readlines()

nums = [int(x) for x in lines]
cur = 0
p1_1 = 0
p1_3 = 0
while len(nums)>0:
	nxt = min(nums)
	if nxt-cur == 1:
		p1_1 += 1
	elif nxt-cur == 3:
		p1_3 += 1
	cur = nxt
	nums.remove(cur)
p1_3 += 1
print('part1',p1_1*p1_3)


nums = [int(x) for x in lines]
counts = {0: 1}
for n in sorted(nums):
	counts[n] = sum([counts[n-i] for i in range(1,4) if n-i in counts])
print('part2',counts[max(nums)])