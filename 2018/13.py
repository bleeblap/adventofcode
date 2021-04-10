#!/usr/bin/env python

import sys

infile = open('13.in','r').read().rstrip('\n')

board = [[c for c in line] for line in infile.split('\n')]

cid = 0
carts = []
for y in range(len(board)):
    for x in range(len(board[y])):
        if board[y][x] in '<>':
            carts.append({'x':x,'y':y,'next':'l','dir':board[y][x],'id':cid})
            board[y][x] = '-'
            cid += 1
        if board[y][x] in '^v':
            carts.append({'x':x,'y':y,'next':'l','dir':board[y][x],'id':cid})
            board[y][x] = '|'
            cid += 1

tick = 0
firstCrash = True
while True:
    carts = sorted(carts, key=lambda k:(k['y'],k['x']))
    #print carts
    if len(carts) <= 1:
        print 'Part2 {},{}'.format(carts[0]['x'],carts[0]['y'])
        break
    for c in carts:
        if c['dir'] == '>':
            c['x'] = c['x'] + 1
            next = board[c['y']][c['x']]
            if next == '\\':
                c['dir'] = 'v'
            elif next == '/':
                c['dir'] = '^'
            elif next == '+':
                if c['next'] == 'l':
                    c['next'] = 's'
                    c['dir'] = '^'
                elif c['next'] == 's':
                    c['next'] = 'r'
                    c['dir'] = '>'
                elif c['next'] == 'r':
                    c['next'] = 'l'
                    c['dir'] = 'v'
        elif c['dir'] == 'v':
            c['y'] = c['y'] + 1
            next = board[c['y']][c['x']]
            if next == '\\':
                c['dir'] = '>'
            elif next == '/':
                c['dir'] = '<'
            elif next == '+':
                if c['next'] == 'l':
                    c['next'] = 's'
                    c['dir'] = '>'
                elif c['next'] == 's':
                    c['next'] = 'r'
                    c['dir'] = 'v'
                elif c['next'] == 'r':
                    c['next'] = 'l'
                    c['dir'] = '<'
        elif c['dir'] == '<':
            c['x'] = c['x'] - 1
            next = board[c['y']][c['x']]
            if next == '\\':
                c['dir'] = '^'
            elif next == '/':
                c['dir'] = 'v'
            elif next == '+':
                if c['next'] == 'l':
                    c['next'] = 's'
                    c['dir'] = 'v'
                elif c['next'] == 's':
                    c['next'] = 'r'
                    c['dir'] = '<'
                elif c['next'] == 'r':
                    c['next'] = 'l'
                    c['dir'] = '^'
        elif c['dir'] == '^':
            c['y'] = c['y'] - 1
            next = board[c['y']][c['x']]
            if next == '\\':
                c['dir'] = '<'
            elif next == '/':
                c['dir'] = '>'
            elif next == '+':
                if c['next'] == 'l':
                    c['next'] = 's'
                    c['dir'] = '<'
                elif c['next'] == 's':
                    c['next'] = 'r'
                    c['dir'] = '^'
                elif c['next'] == 'r':
                    c['next'] = 'l'
                    c['dir'] = '>'

        for x in carts:
            if c['id'] != x['id'] and c['x'] == x['x'] and c['y'] == x['y']:
                #print "CRASH",c['x'],c['y']
                if firstCrash:
                    print 'Part1 {},{}'.format(c['x'],c['y'])
                    firstCrash = False
                carts.remove(c)
                carts.remove(x)
                break

    tick += 1
