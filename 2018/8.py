#!/usr/bin/env python

import sys
import copy

input = open('8.in','r').read()

nums = [int(x) for x in input.replace('\n',' ').split(' ')]

def recur(nums):
    children = nums.pop(0)
    nummeta = nums.pop(0)
    #print len(nums), children, nummeta
    p1 = 0
    p2 = 0
    if children == 0:
        for x in range(nummeta):
            num = nums.pop(0)
            p1 += num
            p2 += num
    else:
        childvals = [0]
        for x in range(children):
            childvals.append(recur(nums))
            p1 += childvals[-1][0]
        for x in range(nummeta):
            val = nums.pop(0)
            p1 += val
            if val < len(childvals):
                p2 += childvals[val][1]

    return p1,p2

p1,p2 = recur(nums)
print 'Part1',p1
print 'Part2',p2
