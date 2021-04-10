#!/usr/bin/env python

import sys
import re
from collections import deque

infile = open('20.in','r').read()
#infile = '^ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))$'
#infile = '^WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))$'

def index_close_paren(pattern):
    level = 0
    for pos in range(len(pattern)):
        if pattern[pos] == '(':
            level += 1
        elif pattern[pos] == ')' and level == 0:
            return pos
        elif pattern[pos] == ')':
            level -= 1
    raise ValueError(pattern)

def dump(board):
    for y in range(len(board)):
        line = ''
        for x in range(len(board[y])):
            line += board[y][x]
        print line

def fill_around_pos(pos):
    global board
    board[pos[1]-1][pos[0]-1] = '#'
    board[pos[1]-1][pos[0]+1] = '#'
    board[pos[1]+1][pos[0]-1] = '#'
    board[pos[1]+1][pos[0]+1] = '#'
    if board[pos[1]-1][pos[0]] == ' ': board[pos[1]-1][pos[0]] = '?'
    if board[pos[1]+1][pos[0]] == ' ': board[pos[1]+1][pos[0]] = '?' 
    if board[pos[1]][pos[0]-1] == ' ': board[pos[1]][pos[0]-1] = '?' 
    if board[pos[1]][pos[0]+1] == ' ': board[pos[1]][pos[0]+1] = '?' 

def move_basic(direction, pos):
    global board
    fill_around_pos(pos)
    #print 'MB',pos,direction

    if direction == 'E':
        board[pos[1]][pos[0]+1] = '|'
        board[pos[1]][pos[0]+2] = '.'
        fill_around_pos((pos[0]+2,pos[1]))
        return (pos[0]+2,pos[1])
    elif direction == 'N':
        board[pos[1]-1][pos[0]] = '-'
        board[pos[1]-2][pos[0]] = '.'
        fill_around_pos((pos[0],pos[1]-2))
        return (pos[0],pos[1]-2)
    elif direction == 'W':
        board[pos[1]][pos[0]-1] = '|'
        board[pos[1]][pos[0]-2] = '.'
        fill_around_pos((pos[0]-2,pos[1]))
        return (pos[0]-2,pos[1])
    elif direction == 'S':
        board[pos[1]+1][pos[0]] = '-'
        board[pos[1]+2][pos[0]] = '.'
        fill_around_pos((pos[0],pos[1]+2))
        return (pos[0],pos[1]+2)
    else:
        raise ValueError(dir)

# Instead of worrying about dynamically growing it, hardcode max and adjust if exception
GRID_SIZE = 200
board = [[' ' for y in range(2*GRID_SIZE)] for x in range(2*GRID_SIZE)]
board[GRID_SIZE][GRID_SIZE] = 'X'

def explore_paths(pattern, pos):
    #print 'EP',pos, pattern
    global board
    if len(pattern) == 0:
        return

    # Simple case no groups or splits, just moving through
    if '|' not in pattern and '(' not in pattern:   
        pos = move_basic(pattern[0], pos)
        explore_paths(pattern[1:], pos)
        return

    # find all | at right level
    level = 0
    splits = []
    for c in range(len(pattern)):
        if pattern[c] == '(':
            level += 1
        elif pattern[c] == ')':
            level -= 1
        if pattern[c] == '|' and level == 0:
            splits.append(c)
    if len(splits) > 0:
        explore_paths(pattern[:splits[0]], pos)
        for x in range(len(splits)-1):
            explore_paths(pattern[splits[x]+1:splits[x+1]], pos)
        explore_paths(pattern[splits[-1]+1:], pos)
    else:
        # No splits at this level, call all groups
        c = 0
        while c < len(pattern):
            if pattern[c] == '(':
                close = index_close_paren(pattern[c+1:])
                explore_paths(pattern[c+1:c+close+1], pos)
                c += close+2
            elif pattern[c] in 'ESWN':
                pos = move_basic(pattern[c], pos)
                c += 1
            else:
                raise ValueError(pattern,c)
        return 

def fin_walls(board):
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == '?':
                board[y][x] = '#'

def boardToGraph(board):
    height = len(board)
    width = len(board[0])
    graph = {(i, j): [] for j in range(width) for i in range(height) if board[i][j] in 'X.'}
    for row, col in graph.keys():
        if row < height - 1 and board[row + 1][col] == '-':
            graph[(row, col)].append(("S", (row + 2, col)))
            graph[(row + 2, col)].append(("N", (row, col)))
        if col < width - 1 and board[row][col + 1] == '|':
            graph[(row, col)].append(("E", (row, col + 2)))
            graph[(row, col + 2)].append(("W", (row, col)))
    return graph

def find_path_bfs(graph, start, goal):
    queue = deque([("", start)])
    visited = set()
    while queue:
        path, current = queue.popleft()
        if current == goal:
            return path
        if current in visited:
            continue
        visited.add(current)
        for direction, neighbour in graph[current]:
            queue.append((path + direction, neighbour))
    return None

if infile[0] != '^' or infile[-1] != '$':
    print 'Invalid infile'

explore_paths(infile[1:-1], (GRID_SIZE,GRID_SIZE))
fin_walls(board)
#dump(board)

graph = boardToGraph(board)
paths = {}
for k in graph.keys():
    paths[k] = len(find_path_bfs(graph, (GRID_SIZE,GRID_SIZE),k))
    #print k,paths[k]

print 'Part1',max(paths.values())
print 'Part2',len([x for x in paths.values() if x >= 1000])
