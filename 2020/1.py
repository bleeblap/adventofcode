#!/usr/bin/env python3

lines = open('1.in').read().split('\n')
nums = [int(n) for n in lines]

for x in range(len(nums)):
	for y in range(x,len(nums)):
		if nums[x] + nums[y] == 2020:
			print('part1',nums[x]*nums[y])

for x in range(len(nums)):
	for y in range(x,len(nums)):
		for z in range(y,len(nums)):
			if nums[x] + nums[y] + nums[z] == 2020:
				print('part2',nums[x]*nums[y]*nums[z])
