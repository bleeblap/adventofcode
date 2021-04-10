#!/usr/bin/env python3

lines = '''35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576'''.split('\n')
LEN=5

lines = open('9.in').readlines()
LEN = 25

nums = [int(x) for x in lines]

p1 = None
for i in range(LEN,len(nums)):
	found = False
	for y in range(LEN):
		for z in range(y+1,LEN):
			if nums[i] == nums[y-(LEN-i)]+nums[z-(LEN-i)]:
				#print('valid',nums[i])
				found = True
				break
		if found:
			break
	if not found:
		p1 = nums[i]
		print('part1',p1)
		break

for l in range(2,100):
	for i in range(len(nums)):
		if sum(nums[i:i+l]) == p1:
			print('part2',min(nums[i:i+l])+max(nums[i:i+l]))
			break
