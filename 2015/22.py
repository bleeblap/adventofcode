from copy import copy
from heapq import heappush, heappop

HARD_MODE = True

spells = {
	'magic missile': {'mana':53, 'damage':4},
	'drain': {'mana':73, 'damage':2, 'heal':2},
	'shield': {'mana':113, 'effect':'shield', 'duration':6},
	'poison': {'mana':173, 'effect':'poison', 'duration':6},
	'recharge': {'mana':229, 'effect':'recharge', 'duration':5}
}

player = {'hp': 50, 'mana': 500}
#player = {'hp': 10, 'mana': 250}
boss = {'hp': 58, 'damage': 9}
#boss = {'hp': 13, 'damage': 8}

def sim(player, boss, p2=False):
	pq = []
	heappush(pq,(0,player,boss,{'shield':0,'poison':0,'recharge':0}))

	while True:
		total,p,b,ef = heappop(pq)
		#print total,p,b,ef
		
		if b['hp'] <= 0:
			return total

		if p2:
			p['hp'] -= 1
			if p['hp'] == 0:
				continue

		# Apply current effects at start of player turn
		if ef['shield'] > 0:
			ef['shield'] -= 1
		if ef['poison'] > 0:
			b['hp'] -= 3
			ef['poison'] -= 1
		if ef['recharge'] > 0:
			p['mana'] += 101
			ef['recharge'] -= 1

		for k,s in spells.items():
			pc = copy(p)
			bc = copy(b)
			efc = copy(ef)
			if pc['mana'] < s['mana']:
				continue # Not enough mana, invalid spell
			pc['mana'] -= s['mana']
			if 'effect' in s:
				if efc[s['effect']] > 0:
					continue # Effect already active, invalid spell
				efc[s['effect']] = s['duration']
			else: # Immediate spells
				if 'damage' in s:
					bc['hp'] -= s['damage'] 
				if 'heal' in s:
					pc['hp'] += s['heal'] 

			# Boss turn, apply effects again
			if efc['poison'] > 0:
				bc['hp'] -= 3
				efc['poison'] -= 1
			if efc['recharge'] > 0:
				pc['mana'] += 101
				efc['recharge'] -= 1

			if bc['hp'] > 0:
				# Calc damage depending on shield
				if efc['shield'] > 0:
					pc['hp'] -= max(1, bc['damage']-7)
					efc['shield'] -= 1
				else:
					pc['hp'] -= bc['damage']
			
			if pc['hp'] <= 0:
				continue # Player dead abandon path
			
			heappush(pq,(total+s['mana'],pc,bc,efc))

print 'part1',sim(player,boss)
print 'part2',sim(player,boss,True)