#!/usr/bin/env python

import sys
import re
from collections import deque

infile = open('21.in','r').read()


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

instrs = []
pcreg = None
for line in infile.split('\n'):
    instr = line.split(' ')[0]
    if instr == '#ip':
        pcreg = int(line.split(' ')[1])
    else:
        a,b,c = map(int, [x for x in re.findall('\d+',line)])
        instrs.append((instr,a,b,c))

#print len(instrs)

pc = 0
reg = [0,0,0,0,0,0]
count = 0
r4s = []
while count < 2446062944:
    #if pc == 28:
    #    print pc,reg,instrs[pc]
    if pc < 0 or pc >= len(instrs):
    #    print 'HALT',count
        break
    reg[pcreg] = pc
    globals()[instrs[pc][0]](reg,instrs[pc][1],instrs[pc][2],instrs[pc][3])
    if pc == 28:
        if reg[4] in r4s:
    #        print 'REPEAT',count,pc,reg,instrs[pc]
            break
        r4s.append(reg[4])
    pc = reg[pcreg]
    #print reg
    pc += 1
    count+= 1

print 'Part1',r4s[0]
print 'Part2',r4s[-1]

#print r4s

comment = '''

Control r[0] at start

#ip 5
00   seti 123 0 4           # r[4] = 123
01   bani 4 456 4           # r[4] = r[4] & 456
02   eqri 4 72 4.           # r[4] = r[4] == 72 # Should always be 1 if implemented correctly
03   addr 4 5 5             # r[5] = r[5] + r[4 --> pc += 1 --> goto 07
04   seti 0 0 5             # r[5] = 0 --> goto 01
05   seti 0 8 4             # r[4] = 0
06   bori 4 65536 3         # r[3] = r[4] | 65536 --> r3 = 0
07   seti 14464005 5 4      # r[4] = 14464005
08   bani 3 255 2           # r[2] = r[3] & 255
09   addr 4 2 4             # r[4] = r[4] + r[2]
10   bani 4 16777215 4      # r[4] = r[4] & 16777215
11   muli 4 65899 4         # r[4] = r[4] * 65899
12   bani 4 16777215 4      # r[4] = r[4] & 16777215
13   gtir 256 3 2           # r[2] = 256 > r[3]
14   addr 2 5 5             # r[5] = r[2] + r[5] --> jmp r[2]
15   addi 5 1 5             # r[5] = r[5] + 1 --> goto 17
16   seti 27 7 5            # r[5] = 27 --> goto 28
17   seti 0 3 2             # r[2] = 0
18   addi 2 1 1             # r[1] = r[2] + 1
19   muli 1 256 1           # r[1] = r[1] * 256
20   gtrr 1 3 1             # r[1] = r[1] > r[3]
21   addr 1 5 5             # r[5] = r[5] + r[1] --> jump 
22   addi 5 1 5             # r[5] = r[5] + 1 --> goto 24
23   seti 25 2 5            # r[5] = 25 --> goto 26
24   addi 2 1 2             # r[2] = r[2] + 1
25   seti 17 9 5            # r[5] = 17 --> goto 18
26   setr 2 2 3             # r[3] = r[2]
27   seti 7 3 5             # r[5] = 7 --> goto 8
28   eqrr 4 0 2             # r[2] = r[4] == r[0]
29   addr 2 5 5             # r[5] = r[2] + r[5] --> jmp r[2]
30   seti 5 9 5             # r[5] = 5 --> goto 06
'''