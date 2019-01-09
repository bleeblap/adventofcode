#!/usr/bin/env python

import sys
import copy
from collections import deque

infile = open('15.in').read()
board = []
lines = infile.split('\n')
for y in range(len(lines)):
    row = []
    for x in range(len(lines[y])):
        c = lines[y][x]
        if c in 'EG':
            row.append({'c':c,'hp':200,'ap':3,'x':x,'y':y})
        else:
            row.append({'c':c,'x':x,'y':y})
    board.append(row)

def dump(board):
    for row in board:
        out = ''
        endhp = ''
        for col in row:
            out += col['c']
            if col['c'] in 'GE':
                endhp += ' {0}({1})'.format(col['c'],col['hp'])
        print out + endhp

def boardToGraph(board):
    height = len(board)
    width = len(board[0])
    graph = {(i, j): [] for j in range(width) for i in range(height) if board[i][j]['c'] == '.'}
    for row, col in graph.keys():
        if row < height - 1 and board[row + 1][col]['c'] == '.':
            graph[(row, col)].append(("S", (row + 1, col)))
            graph[(row + 1, col)].append(("N", (row, col)))
        if col < width - 1 and board[row][col + 1]['c'] == '.':
            graph[(row, col)].append(("E", (row, col + 1)))
            graph[(row, col + 1)].append(("W", (row, col)))
    return graph

def shortPathToPos(board, unit, x, y):
    start = (unit['y'],unit['x'])
    goal = (x,y)
    queue = deque([("", start)])
    visited = set()
    type = board[unit['y']][unit['x']]['c']
    board[unit['y']][unit['x']]['c'] = '.' # Make graph think start is empty so its added to graph
    graph = boardToGraph(board)
    board[unit['y']][unit['x']]['c'] = type # Revert
    result = []
    while queue:
        path, current = queue.popleft()
        if current == goal:
            # Find all other paths at this depth
            result.append(path)
            continue
        if current in visited:
            continue
        visited.add(current)
        readingOrder = {}
        if len(result)>0:
            return result
        for direction, neighbour in graph[current]:
            readingOrder[direction] = neighbour
        for c in 'NWES': # READING ORDER!
            if c in readingOrder:
                queue.append((path + c, readingOrder[c]))
    return result

def move(board, unit):
    posInRange = []
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x]['c'] in 'GE' and unit['c'] != board[y][x]['c']:
                if board[y][x-1]['c'] == '.': posInRange.append((y,x-1))
                if board[y][x+1]['c'] == '.': posInRange.append((y,x+1))
                if board[y-1][x]['c'] == '.': posInRange.append((y-1,x))
                if board[y+1][x]['c'] == '.': posInRange.append((y+1,x))
    #print 'posInRange',posInRange
    if len(posInRange) == 0:
        return # No targets with open adjacent square
    inRangeWithDistAndPath = []
    for tx,ty in posInRange:
        path = shortPathToPos(board,unit,tx,ty)
        if len(path) > 0:
            inRangeWithDistAndPath.append((tx,ty,len(path[0]),path))
    #print 'inRangeWithDistAndPath',inRangeWithDistAndPath
    if len(inRangeWithDistAndPath) == 0:
        return # No path to adjacent square
    minPathLen = min([z[2] for z in inRangeWithDistAndPath])
    minPaths = [z for z in inRangeWithDistAndPath if z[2] == minPathLen]
    #print 'minPath',minPathLen,minPaths
    targetPathDest = sorted(minPaths, key=lambda k:(k[0],k[1]))[0]
    #print 'targetPathDest',targetPathDest
    targetPath = sorted(targetPathDest[3], key=lambda k:'NWES'.index(k[0]))[0]
    #print 'targetPath',targetPath
    dir = targetPath[0]
    #print unit, targetPath, dir
    y,x = unit['y'],unit['x']
    if dir == 'N':
        board[y-1][x] = board[y][x]
        board[y][x] = {'c':'.','x':x,'y':y}
        board[y-1][x]['y'] -= 1
        unit['y'] -= 1
    elif dir == 'W':
        board[y][x-1] = board[y][x]
        board[y][x] = {'c':'.','x':x,'y':y}
        board[y][x-1]['x'] -= 1
        unit['x'] -= 1
    elif dir == 'E':
        board[y][x+1] = board[y][x]
        board[y][x] = {'c':'.','x':x,'y':y}
        board[y][x+1]['x'] += 1
        unit['x'] += 1
    elif dir == 'S':
        board[y+1][x] = board[y][x]
        board[y][x] = {'c':'.','x':x,'y':y}
        board[y+1][x]['y'] += 1
        unit['y'] += 1

def attack(board, unit):
    if 'hp' not in board[unit['y']][unit['x']]:
        return 1 # Dead will get removed after a round
    x = unit['x']
    y = unit['y']
    e = 'G' if unit['c'] == 'E' else 'E'
    inrange = []
    if board[y-1][x]['c'] == e:
        inrange.append(board[y-1][x])
    if board[y][x-1]['c'] == e:
        inrange.append(board[y][x-1])
    if board[y][x+1]['c'] == e:
        inrange.append(board[y][x+1])
    if board[y+1][x]['c'] == e:
        inrange.append(board[y+1][x])
    if len(inrange) == 0:
        return 0 # No attack
    #print 'inrange',inrange
    leasthp = min(c['hp'] for c in inrange)
    uwithleastlp = [c for c in inrange if c['hp'] == leasthp]
    #print 'uwithleastlp',uwithleastlp
    target = sorted(uwithleastlp, key=lambda k:(k['y'],k['x']))[0]
    #print 'Attack',unit,target
    target['hp'] -= unit['ap']
    if target['hp'] <= 0:
        #print 'DEAD',target
        board[target['y']][target['x']] = {'c':'.','x':target['x'],'y':target['y']}
        return target # Dead to remove from list
    return 1 # Normal Attack

def runSim(board,exitOnDeadElf=True,debug=False):
    round = 0
    deadElves = 0
    while True:
        unitorder = []
        # Calc unit order at start and save so it doesn't change within a round
        for y in range(len(board)):
            for x in range(len(board[y])):
                if board[y][x]['c'] in 'GE':
                    unitorder.append(copy.deepcopy(board[y][x]))
        #print unitorder

        allDead = False
        deadThisRound = []
        for unit in unitorder:
            # Make sure this unit didn't die this round
            skipDead = False
            for d in deadThisRound:
                if unit['x'] == d['x'] and unit['y'] == d['y']:
                    #print 'SKPPING DEAD THIS ROUND',unit
                    skipDead = True
                    break
            if skipDead:
                continue
            # Before anything check stop condition
            targetsrem = 0
            for y in range(len(board)):
                for x in range(len(board[y])):
                    if board[y][x]['c'] == ('G' if unit['c'] == 'E' else 'E'):
                        targetsrem += 1
            #print 'targetsrem',targetsrem
            if targetsrem == 0:
                allDead = True
                break

            ares = attack(board, unit)
            if ares == 0:
                #print 'Move',unit
                move(board, unit)
                ares = attack(board, unit)
            if type(ares) is dict:
                if ares['c'] == 'E':
                    deadElves += 1
                    if exitOnDeadElf:
                        #print 'DEAD ELF BREAK'
                        return None
                deadThisRound.append(ares)

        if allDead:
            hpleft = 0
            for y in range(len(board)):
                for x in range(len(board[y])):
                    if board[y][x]['c'] in 'GE':
                        hpleft += board[y][x]['hp']
            if debug:
                dump(board)
            return (round,hpleft)

        round += 1
        if debug:
            print round
            dump(board)

round,hpleft = runSim(copy.deepcopy(board), False)
print 'Part1',round*hpleft #248848

for ap in range(4,100):
    b = copy.deepcopy(board)
    for y in range(len(b)):
        for x in range(len(b[y])):
            if b[y][x]['c'] == 'E':
                b[y][x]['ap'] = ap
    res = runSim(b)
    if res != None:
        print 'Part2',res[0]*res[1]
        break
