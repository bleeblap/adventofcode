#!/usr/bin/env python

import sys

serial = 7315

grid = []
for x in range(300):
    row = []
    for y in range(300):
        power = (((x+10)*y) + serial)*(x+10)
        try:
            power = int(str(power)[-3:-2])
        except:
            power = 0
        row.append(power-5)
    grid.append(row)
#print grid

maxpow = 0
max_x = 0
max_y = 0
for size in range(25):
    print size
    for x in range(0,300-size):
        for y in range(0,300-size):
            pow = 0
            for dx in range(size):
                for dy in range(size):
                        pow += grid[x+dx][y+dy]
            if pow > maxpow:
                maxpow = pow
                max_x = x
                max_y = y
                max_size = size

print 'Part2 {0},{1},{2}'.format(max_x,max_y,max_size)
