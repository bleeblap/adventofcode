#!/usr/bin/env python

import sys
import copy
import networkx

depth = 11541
#depth = 510
target = (14,778)
#target = (10,10)
PAD = 50

board = [[{'geo':0,'erosion':(depth%20183),'type':(depth%20183)%3}]]

def dump(board):
    for y in range(len(board)):
        line = ''
        for x in range(len(board[y])):
            if y == 0 and x == 0:
                line += 'M'
            elif y == target[1] and x == target[0]:
                line += 'T'
            elif board[y][x]['type'] == 0:
                line += '.'
            elif board[y][x]['type'] == 1:
                line += '='
            elif board[y][x]['type'] == 2:
                line += '|'
        print line

def make_coord(x,y):
    d = {}
    global board, depth, target
    if x == target[0] and y == target[1]:
        d['geo'] = 0
    elif x == 0:
        d['geo'] = y * 48271
    elif y == 0:
        d['geo'] = x * 16807
    else:
        d['geo'] = board[y][x-1]['erosion'] * board[y-1][x]['erosion']
    d['erosion'] = (d['geo']+depth)%20183
    d['type'] = d['erosion'] % 3
    return d

while len(board) < target[1]+PAD:
    board.append([])
    for x in range(len(board[0])):
        board[len(board)-1].append(make_coord(x,len(board)-1))

while len(board[0]) < target[0]+PAD:
    for y in range(len(board)):
        board[y].append(make_coord(len(board[y]),y))

risk = 0
for y in range(target[1]+1):
    for x in range(target[0]+1):
        risk += board[y][x]['type']
print 'Part1',risk

# dump(board)

def valid_tools(ter):
    if ter == 0:
        return ['C','T']
    elif ter == 1:
        return ['C','N']
    elif ter == 2:
        return ['T','N']
    else:
        assert(ter)

def boardToGraph(board):
    # Create two nodes for each spot on the board for x,y,equip
    graph = networkx.Graph()
    for y in range(len(board)):
        for x in range(len(board[y])):
            for c in valid_tools(board[y][x]['type']):
                graph.add_node((x,y,c))

    for row, col, e in graph.nodes():
        # Path to switch equipment
        oe = [x for x in valid_tools(board[col][row]['type']) if x != e][0]
        graph.add_edge((row,col,e), (row,col,oe), weight=7)
        # Paths to move to valid adjacent squares
        if row < len(board[0]) - 1 and e in valid_tools(board[col][row + 1]['type']):
            graph.add_edge((row, col, e), (row + 1, col, e), weight=1)
        if col < len(board) - 1 and e in valid_tools(board[col + 1][row]['type']):
            graph.add_edge((row, col, e), (row, col + 1, e), weight=1)
    return graph

graph = boardToGraph(board)
print 'Part2',networkx.nx.shortest_path_length(graph, (0,0,'T'), (target[0],target[1],'T'), 'weight')

