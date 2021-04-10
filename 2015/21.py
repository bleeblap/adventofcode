from itertools import combinations
from copy import copy

weapons = {
	'Dagger': {'cost':8, 'damage':4, 'armor':0},
	'Shortsword': {'cost':10, 'damage':5, 'armor':0},
	'Warhammer': {'cost':25, 'damage':6, 'armor':0},
	'Longsword': {'cost':40, 'damage':7, 'armor':0},
	'Greataxe': {'cost':74, 'damage':8, 'armor':0}
}

armor = {
	'Leather': {'cost':13, 'damage':0, 'armor':1},
	'Chainmail': {'cost':31, 'damage':0, 'armor':2},
	'Splintmail': {'cost':53, 'damage':0, 'armor':3},
	'Bandedmail': {'cost':75, 'damage':0, 'armor':4},
	'Platemail': {'cost':102, 'damage':0, 'armor':5},
	'None': {'cost':0, 'damage':0, 'armor':0}
}

rings = {
	'Damage +1': {'cost':25, 'damage':1, 'armor':0},
	'Damage +2': {'cost':50, 'damage':2, 'armor':0},
	'Damage +3': {'cost':100, 'damage':3, 'armor':0},
	'Defense +1': {'cost':20, 'damage':0, 'armor':1},
	'Defense +2': {'cost':40, 'damage':0, 'armor':2},
	'Defense +3': {'cost':80, 'damage':0, 'armor':3},
}

boss = {'hp': 109, 'damage': 8, 'armor': 2}
player = {'hp': 100, 'damage': 0, 'armor': 0}

def sim(player, boss):
	php = player['hp']
	bhp = boss['hp']
	while php > 0 and bhp > 0:
		bhp -= max(player['damage']-boss['armor'], 1)
		if bhp > 0:
			php -= max(boss['damage']-player['armor'], 1)
	#print php,bhp,player
	return php>0

mincost = 999999
maxcost = 0
for w in weapons:
	for a in armor:
		p = copy(player)
		p['damage'] = weapons[w]['damage']
		p['armor'] = armor[a]['armor']
		cost = weapons[w]['cost'] + armor[a]['cost']

		# No Rings
		if sim(p, boss) and cost<mincost:
			mincost = cost
		if not sim(p, boss) and cost>maxcost:
			maxcost = cost

		# One Ring
		for r in rings:
			p1 = copy(p)
			p1['damage'] += rings[r]['damage']
			p1['armor'] += rings[r]['armor']
			c1 = cost + rings[r]['cost']
			if sim(p1, boss) and c1<mincost:
				mincost = c1
			if not sim(p1, boss) and c1>maxcost:
				maxcost = c1

		# Two Rings
		for rs in combinations(rings, 2):
			p2 = copy(p)
			c2 = cost
			for r in rs:
				p2['damage'] += rings[r]['damage']
				p2['armor'] += rings[r]['armor']
				c2 += rings[r]['cost']
			if sim(p2, boss) and c2<mincost:
				mincost = c2
			if not sim(p2, boss) and c2>maxcost:
				maxcost = c2

print 'Part1',mincost
print 'Part2',maxcost