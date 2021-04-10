#!/usr/bin/env python

import sys

input = open('4.in','r').read()

from datetime import datetime
entries = input.split('\n')
parsed = {}
for entry in entries:
    tm = datetime.strptime(entry.split(']')[0][1:], '%Y-%m-%d %H:%M')
    val = entry.split(']')[1]
    parsed[tm] = val

ordered = sorted(parsed.keys())
curguard = None
sleeptime = None
sleepstats = {}

for x in ordered:
    #print x.isoformat(),parsed[x]
    if 'Guard' in parsed[x]:
        curguard = int(parsed[x].split('Guard #')[1].split(' ')[0])
    elif 'falls asleep' in parsed[x]:
        sleeptime = x
    elif 'wakes up' in parsed[x]:
        if curguard not in sleepstats:
            sleepstats[curguard] = (x-sleeptime).seconds/60
            sleeptime = None
        else:
            sleepstats[curguard] += (x-sleeptime).seconds/60
            sleeptime = None

#print sleepstats
mostsleepyguard = None
mostsleepytime = 0
for g in sleepstats:
    if sleepstats[g] > mostsleepytime:
        mostsleepytime = sleepstats[g]
        mostsleepyguard = g
#print 'Most sleep guard ID {0} for sleep minutes {1}'.format(mostsleepyguard, mostsleepytime)

sleeparray = []
for x in range(60):
    sleeparray.append(0)

for x in ordered:
    if 'Guard' in parsed[x]:
        curguard = int(parsed[x].split('Guard #')[1].split(' ')[0])
    elif 'falls asleep' in parsed[x]:
        sleeptime = x
    elif 'wakes up' in parsed[x]:
        if curguard == mostsleepyguard:
            for y in range((x-sleeptime).seconds/60):
                sleeparray[y+sleeptime.minute] += 1

maxsleep = 0
maxsleepmin = None
for x in range(len(sleeparray)):
    if sleeparray[x] > maxsleep:
        maxsleep = sleeparray[x]
        maxsleepmin = x
#print 'Most sleep {0} at min {1}'.format(maxsleep, maxsleepmin)

print 'Part1 {0}'.format(mostsleepyguard*maxsleepmin)

part2sleeptime = 0
part2guard = None
part2min = None
for g in sleepstats:
    sleeparray = []
    for x in range(60):
        sleeparray.append(0)
    for x in ordered:
        if 'Guard' in parsed[x]:
            curguard = int(parsed[x].split('Guard #')[1].split(' ')[0])
        elif 'falls asleep' in parsed[x]:
            sleeptime = x
        elif 'wakes up' in parsed[x]:
            if curguard == g:
                for y in range((x-sleeptime).seconds/60):
                    sleeparray[y+sleeptime.minute] += 1
    for x in range(len(sleeparray)):
        if sleeparray[x] > part2sleeptime:
            part2guard = g
            part2min = x
            part2sleeptime = sleeparray[x]

print 'Part2 {0}'.format(part2guard*part2min)
