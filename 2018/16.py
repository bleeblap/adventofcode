#!/usr/bin/env python

import sys
import re
import copy

infile = open('16.in').read()

def addr(reg,a,b,c):
    reg[c] = reg[a] + reg[b]

def addi(reg,a,b,c):
    reg[c] = reg[a] + b

def mulr(reg,a,b,c):
    reg[c] = reg[a] * reg[b]

def muli(reg,a,b,c):
    reg[c] = reg[a] * b

def banr(reg,a,b,c):
    reg[c] = reg[a] & reg[b]

def bani(reg,a,b,c):
    reg[c] = reg[a] & b

def borr(reg,a,b,c):
    reg[c] = reg[a] | reg[b]

def bori(reg,a,b,c):
    reg[c] = reg[a] | b

def setr(reg,a,b,c):
    reg[c] = reg[a]

def seti(reg,a,b,c):
    reg[c] = a

def gtir(reg,a,b,c):
    reg[c] = int(a > reg[b])

def gtri(reg,a,b,c):
    reg[c] = int(reg[a] > b)

def gtrr(reg,a,b,c):
    reg[c] = int(reg[a] > reg[b])

def eqir(reg,a,b,c):
    reg[c] = int(a == reg[b])

def eqri(reg,a,b,c):
    reg[c] = int(reg[a] == b)

def eqrr(reg,a,b,c):
    reg[c] = int(reg[a] == reg[b])

instrs = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]

lines = infile.split('\n')
cur = 0
part1 = 0
samples = []

while 'Before' in lines[cur]:
    breg = [int(c) for c in re.findall('\d+', lines[cur])]
    i = [int(c) for c in re.findall('\d+', lines[cur+1])]
    areg = [int(c) for c in re.findall('\d+', lines[cur+2])]
    #print breg, i, areg
    pot_ops = []
    for instr in instrs:
        temp = copy.deepcopy(breg)
        instr(temp, i[1], i[2], i[3])
        if temp == areg:
            #print instr.func_name
            pot_ops.append(instr.func_name)
    if len(pot_ops) >= 3:
        part1 += 1
    samples.append([i[0],pot_ops])
    cur += 4

print 'Part1',part1

opmap = [None for i in range(16)]
while None in opmap:
    foundopcode = None
    foundopname = None
    for s in samples:
        if len(s[1]) == 1:
            foundopcode = s[0]
            foundopname = s[1][0]
            opmap[foundopcode] = foundopname
            #print foundopcode, foundopname
            break
    samples = [s for s in samples if s[0] != foundopcode]
    for s in samples:
        if foundopname in s[1]:
            s[1].remove(foundopname)

#print opmap
reg = [0,0,0,0]
for line in infile.split('\n\n\n\n')[1].split('\n'):
    op, a, b ,c = [int(c) for c in re.findall('\d+', line)]
    #print op,a,b,c
    globals()[opmap[op]](reg, a,b,c)

print 'Part2',reg[0]

