#!/usr/bin/env python3

nums = [int(x) for x in '12,20,0,6,1,17,7'.split(',')]
#nums = [int(x) for x in '0,3,6'.split(',')]

dp = {}
prev = None
for turn in range(1, 30000001):
	if turn <= len(nums):
		dp[nums[turn-1]] = turn
		prev = nums[turn-1]
	else:
		if prev in dp:
			n = turn - dp[prev] - 1
		else:
			n = 0
		dp[prev] = turn-1
		prev = n

	if turn == 2020:
		print('part1',prev)
	if turn == 30000000:
		print('part2',prev)
