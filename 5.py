#!/usr/bin/env python

import sys

rawinput = open('5.in','rb').read()

def react(instr):
    while True:
        didtrim = False
        for x in range(len(instr)-1):
            if instr[x].lower() == instr[x+1].lower() and instr[x] != instr[x+1]:
                #print 'Cut',x,input[x],input[x+1]
                instr = instr[:x] + instr[x+2:]
                #print input
                didtrim = True
                break

        if not didtrim:
            break
    return instr

print 'Part1',len(react(rawinput))

minlen = len(rawinput)
for stripme in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    instr = ''
    for x in rawinput:
        if x.lower() != stripme.lower():
            instr += x
    l = len(react(instr))
    if l < minlen:
        minlen = l
    
print 'Part2',minlen
