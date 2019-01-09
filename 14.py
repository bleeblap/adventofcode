#!/usr/bin/env python

import sys

input = '074501'

e1 = 0
e2 = 1
tape = [3, 7]

while True:
    newchar = [int(c) for c in str(tape[e1]+tape[e2])]
    for c in newchar:
        tape.append(c)
        if len(tape) > len(input):
            #print ''.join([str(x) for x in tape[-len(input):]])
            if input == ''.join([str(x) for x in tape[-len(input):]]):
                print 'Part1',''.join([str(x) for x in tape[int(input):int(input)+10]])
                print 'Part2',len(tape)-len(input)
                sys.exit(0)
    e1 = (e1 + tape[e1] + 1) % len(tape)
    e2 = (e2 + tape[e2] + 1) % len(tape)
    #print tape[e1],tape[e2],tape

