#!/usr/bin/env python3

lines = '''..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#'''.split('\n')
lines = open('3.in').read().split('\n')

REP = 100
board = [line*REP for line in lines]

trees = 0
part2 = [0,0,0,0,0]
for x in range(len(board)):
	if board[x][x] == '#':
		part2[0] += 1
	if board[x][x*3] == '#':
		trees += 1
		part2[1] += 1
	if board[x][x*5] == '#':
		part2[2] += 1
	if board[x][x*7] == '#':
		part2[3] += 1
	if x%2==0 and board[x][x//2] == '#':
		part2[4] += 1


print('part1',trees)
print('part2',part2[0]*part2[1]*part2[2]*part2[3]*part2[4])
