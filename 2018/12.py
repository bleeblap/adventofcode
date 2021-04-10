#!/usr/bin/env python

import sys

infile = open('12.in','r').read()

inputtest = '''initial state: #..#.#..##......###...###

...## => #
..#.. => #
.#... => #
.#.#. => #
.#.## => #
.##.. => #
.#### => #
#.#.# => #
#.### => #
##.#. => #
##.## => #
###.. => #
###.# => #
####. => #'''

def makescores(numiters):
    pad = 5
    state = '.'*pad + infile.split('\n')[0][len('initial state: '):] + '.'*(1000*pad)

    trans = []
    for line in infile.split('\n')[2:]:
        init,res = line.split(' => ')
        if res == '#':
            trans.append(init)

    def getscore(pad, state):
        idx = -pad
        sum = 0
        for c in state:
            if c == '#':
                sum += idx
            idx += 1
        return sum

    scores = []
    for gen in range(numiters):
        s = getscore(pad, state)
        scores.append(s)
        nextstate = '.'
        for x in range(2, len(state)-2):
            if state[x-3:x+2] in trans:
                nextstate += '#'
            else:
                nextstate += '.'
        state = nextstate + '...'
    return scores


scores = makescores(500)
print 'Part1',scores[20]

diffs = []
for x in range(len(scores)-1):
    diffs.append(scores[x+1]-scores[x])

constat = diffs.index(57)
print 'Part2', scores[constat] + 57*(50000000000-constat)



