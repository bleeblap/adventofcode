#!/usr/bin/env python

import sys
import re
import copy

infile = open('19.in','r').read()

infile2 = '''#ip 0
seti 5 0 1
seti 6 0 2
addi 0 1 0
addr 1 2 3
setr 1 0 0
seti 8 0 4
seti 9 0 5'''

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
while True:
    #print pc,reg,instrs[pc],
    if pc < 0 or pc >= len(instrs):
        break
    reg[pcreg] = pc
    globals()[instrs[pc][0]](reg,instrs[pc][1],instrs[pc][2],instrs[pc][3])
    pc = reg[pcreg]
    pc += 1

print 'Part1',reg[0]

manual_disassem = '''
#ip 5
     0  addi 5 16 5 # goto A (execute 17)
B:   1  seti 1 8 2  # r[2] = 1
D:   2  seti 1 1 1  # r[1] = 1
C:   3  mulr 2 1 4  # r[4] = r[2] * r[1] --> r[4] = 1
     4  eqrr 4 3 4  # r[4] = (r[4] == r[3])
     5  addr 4 5 5  # pc = pc + r[4] --> jmp +r[4] --> if r[4] == r[3] add bignum to r[0]
     6  addi 5 1 5  # r[5] = r[5] + 1 --> jump +1 (skip next instr)
     7  addr 2 0 0  # (skipped) r[0] = r[2] + r[0]  ---- how many times in this instr hit?
     8  addi 1 1 1  # r[1] = r[1] + 1
     9  gtrr 1 3 4  # r[4] = (r[1] > r[3])
    10  addr 5 4 5  # r[5] = r[5] + r[4] --> jmp +r[4]
    11  seti 2 8 5  # r[5] = 2 --> goto C                       --- inner loop until r[1] > r[3]
    12  addi 2 1 2  # r[2] = r[2] + 1
    13  gtrr 2 3 4  # r[4] = (r[2] > r[3])
    14  addr 4 5 5  # r[5] = r[5] + r[4] --> pc += r[4]   ------ if r[2] > r[3] goto HALT
    15  seti 1 7 5  # r[5] = 1 --> goto D
    16  mulr 5 5 5  # r[5] = r[5] * 5 --> pc = 16*5 --> HALT
A:  17  addi 3 2 3  # r[3] = r[3] + 2 --> r3 = 2
    18  mulr 3 3 3  # r[3] = r[3] * r[3] --> r3 = 4
    19  mulr 5 3 3  # r[3] = r[5] * r[3] --> r3 *= 19 --> r3 = 76
    20  muli 3 11 3
    21  addi 4 6 4
    22  mulr 4 5 4
    23  addi 4 5 4
    24  addr 3 4 3
    25  addr 5 0 5
    26  seti 0 0 5
    27  setr 5 3 4
    28  mulr 4 5 4
    29  addr 5 4 4
    30  mulr 5 4 4
    31  muli 4 14 4
    32  mulr 4 5 4
    33  addr 3 4 3  # ... r3 = 10551373 from trace
    34  seti 0 3 0  # r[0] = 0
    35  seti 0 0 5  # goto B
'''

first_psuedocode = '''
r3 = 10551373
r2 = 1
r0 = 0
Dloop = True
Cloop = True
while Dloop:
    r1 = 1
    while Cloop:
        r4 = r1*r2
        if r4 == 10551373:
            r0 += r2
        r1 += 1
        if r1 <= 10551373:
            continue # conintue Cloop
        r2 += 1
        if r2 <= 10551373:
            break # continue Dloop
        # HALT / WIN
'''

simplified = '''
r2 = 1
while r2 < bignum:
    r1 = 1
    while r1 < bignum:
        if r1*r2 == bignum:
            res += r2
        r1 += 1
    r2 += 1
# So find the sum of all of the factors of bignum
'''

# Thanks stackoverflow
def factors(n):
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

print 'Part2',sum(factors(10551373))