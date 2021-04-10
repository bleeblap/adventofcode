#!/usr/bin/env python

import sys

input = open('6.in','r').read()

MAX_DISTANCE = 10000

board = [[{'id':None,'d':None} for x in range(500)] for y in range(500)]

coords = []
id = 1
for coord in input.split('\n'):
    x = int(coord.split(',')[0])
    y = int(coord.split(',')[1])
    coords.append([id,x,y])
    id += 1

# Fill up board with closest IDs
for x in range(500):
    for y in range(500):
        close_distance = 99999
        close_id = None
        cur_tie = False
        total_dist = 0
        for coord in coords:
            dist = abs(coord[1]-x) + abs(coord[2]-y)
            total_dist += dist
            #print coord[0],coord[1],x,coord[1],y,dist,total_dist
            if dist < close_distance:
                close_distance = dist
                close_id = coord[0]
                cur_tie = False
            elif dist == close_distance:
                cur_tie = True
        #print cur_tie, close_id, close_distance, total_dist
        board[x][y]['d'] = total_dist
        if not cur_tie:
            board[x][y]['id'] = close_id

#import json
#print json.dumps(board,indent=2)

# If an ID is in the first or last row or column it is infinite
infinlist = []
for x in range(500):
    if board[0][x]['id'] not in infinlist:
        infinlist.append(board[0][x]['id'])
    if board[499][x]['id'] not in infinlist:
        infinlist.append(board[499][x]['id'])
    if board[x][0]['id'] not in infinlist:
        infinlist.append(board[x][0]['id'])
    if board[x][499]['id'] not in infinlist:
        infinlist.append(board[x][499]['id'])

#print 'Infinlist:',infinlist

counts = {}
num_in_box = 0
for x in range(500):
    for y in range(500):
        if board[x][y]['d'] < 10000:
            num_in_box += 1
        if board[x][y]['id'] in infinlist:
            continue
        if board[x][y]['id'] not in counts:
            counts[board[x][y]['id']] = 1
        else:
            counts[board[x][y]['id']] += 1


print 'Part 1',max(counts.values())
print 'Part 2',num_in_box


