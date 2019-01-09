import sys

input = open('2.in','rb').read()

dup = 0
trip = 0
for line in input.split('\n'):
    found = {}
    for x in line:
        if x in found:
            found[x] += 1
        else:
            found[x] = 1
    for k in found:
        if found[k] == 2:
            dup += 1
            break
    for k in found:
        if found[k] == 3:
            trip += 1
            break
print 'Part1',dup*trip

lines = input.split('\n')
for x in range(len(lines)):
    for y in range(x+1, len(lines)):
        diffchars = 0
        for z in range(len(lines[x])):
            if lines[x][z] != lines[y][z]:
                diffchars += 1
        if diffchars == 1:
            part2 = ''.join([lines[x][c] for c in range(len(lines[x])) if lines[x][c] == lines[y][c]])
            print 'Part2',part2
            sys.exit(0)
