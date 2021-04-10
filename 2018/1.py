#!/usr/bin/env python

import sys

input = open('1.in','r').read().rstrip('\n')

nums = [int(x) for x in input.split('\n')]
sum = 0
history = [0]
for round in range(1000):
    for x in nums:
        sum += x
        if sum in history:
            print 'Part2',sum
            sys.exit(0)
        else:
            history.append(sum)
    if round == 0:
        print 'Part1',sum
