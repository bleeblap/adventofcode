#!/usr/bin/env python3

lines = '''light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.'''.split('\n')
lines = '''shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.'''.split('\n')
lines = open('7.in').read().split('\n')

rules = {}
for line in lines:
	src = line[0:line.find(' bag')]
	rules[src] = {}
	for dst in line.split(' contain ')[1].split(', '):
		if 'no other' in dst:
			n = 0
			d = None
		else:
			n = int(dst.split(' ')[0])
			d = dst[dst.find(' ')+1:dst.find(' bag')]
		rules[src][d] = n

def recur(cur, rules):
	res = set()
	if len(rules[cur]) == 1 and None in rules[cur]:
		return res
	else:
		for k in rules[cur]:
			res.add(k)
			res |= recur(k, rules)
	return res

def recur2(cur, rules):
	if len(rules[cur]) == 1 and None in rules[cur]:
		return 0
	else:
		count = 0
		for k in rules[cur]:
			count += rules[cur][k]
			count += rules[cur][k]*recur2(k, rules)
	return count

part1 = sum(['shiny gold' in recur(src, rules) for src in rules])
print('part1', part1)
print('part2', recur2('shiny gold', rules))
