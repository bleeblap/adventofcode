#!/usr/bin/env python3

rooms = open('4.in').read().split('\n')
part1=0
for room in rooms:
	parts = room.split('-')
	sector,checks = parts[-1].split('[')
	sector = int(sector)
	checks = checks.rstrip(']')

	roomchrs = ''.join(parts[0:-1])
	stats = {}
	for c in set(roomchrs):
		if roomchrs.count(c) in stats:
			stats[roomchrs.count(c)] += c
		else:
			stats[roomchrs.count(c)] = c
	check = ''
	while len(check)<6:
		mx = max(stats.keys())
		check += ''.join(sorted(stats[mx]))
		del stats[mx]
	check = check[:5]
	if check == checks:
		part1 += sector

		name = ''
		for p in parts[:-1]:
			for c in p:
				name += chr((((ord(c)-ord('a'))+sector)%26)+ord('a'))
			name += ' '
		#print(room)
		#print(name)
		if 'northpole' in name:
			print('part2',sector)

print('part1',part1)
