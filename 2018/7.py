#!/usr/bin/env python

import sys
import copy

input = open('7.in','r').read()

rules = []
steps = []
for c in input.split('\n'):
    first = c.split(' must ')[0].split(' ')[1]
    second = c.split(' step ')[1].split(' can ')[0]
    #print first, second
    if first not in steps:
        steps.append(first)
    if second not in steps:
        steps.append(second)
    rules.append({'f':first, 's':second})

allrules = copy.deepcopy(rules)
allsteps = copy.deepcopy(steps)
part1 = ''
while len(steps) > 0:
    stepc = copy.deepcopy(steps)
    for x in rules:
        if x['s'] in stepc:
            stepc.remove(x['s'])
    nextc = sorted(stepc)[0]
    part1 += nextc
    steps.remove(nextc)
    rules = [x for x in rules if x['f'] != nextc]

print 'Part1',part1

workers = [{'id':x,'working':None,'timerem':0} for x in range(5)]
steps = allsteps
rules = allrules
time = 0
while len(steps) > 0:
    stepc = copy.deepcopy(steps)
    for x in rules:
        if x['s'] in stepc:
            stepc.remove(x['s'])
    stepc = sorted(stepc)
    while len(stepc) > 0 and len([x for x in workers if x['working'] == None]) > 0:
        for w in workers:
            if w['working'] == None:
                c = stepc[0]
                w['working'] = c
                w['timerem'] = 61 + ord(c) - ord('A')
                stepc.remove(c)
                steps.remove(c)
                break

    for w in workers:
        if w['working'] != None:
            w['timerem'] -= 1
            if w['timerem'] <= 0:
                rules = [x for x in rules if x['f'] != w['working']]
                w['working'] = None

    time += 1

print 'Part2',time+max([x['timerem'] for x in workers])


