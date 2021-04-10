#!/usr/bin/env python

import sys
import copy
import re


infile = open('24.in','r').read()

infile2 = '''Immune System:
17 units each with 5390 hit points (weak to radiation, bludgeoning) with an attack that does 4507 fire damage at initiative 2
989 units each with 1274 hit points (immune to fire; weak to bludgeoning, slashing) with an attack that does 25 slashing damage at initiative 3

Infection:
801 units each with 4706 hit points (weak to radiation) with an attack that does 116 bludgeoning damage at initiative 1
4485 units each with 2961 hit points (immune to radiation; weak to fire, cold) with an attack that does 12 slashing damage at initiative 4'''

def parseline(line):
	unit = {}
	unit['num'], unit['hp'], unit['attack_power'], unit['initiative'] = map(int, [x for x in re.findall('-?\d+',line)])
	if '(' in line:
		attrs = line.split('(')[1].split(')')[0].split('; ')
		for a in attrs:
			t = a.split(' ')[0]
			unit[t] = []
			for x in a.split(' ')[2:]:
				unit[t].append(x.rstrip(','))
	unit['attack_type'] = re.findall('(\w+) damage', line)[0]
	return unit

i = 1
masterimmune = []
for line in infile.split('Infection:')[0].split('\n')[1:-2]:
	u = parseline(line)
	u['type'] = 'Immune'
	u['id'] = i
	i += 1
	masterimmune.append(u)
i = 1
masterinfection = []
for line in infile.split('Infection:')[1].split('\n')[1:]:
	u = parseline(line)
	u['type'] = 'Infection'
	u['id'] = i
	i += 1
	masterinfection.append(u)

def est_damage(u, t):
	assert u['type'] != t['type']
	plan_damage = u['attack_power']*u['num']
	if 'weak' in t and u['attack_type'] in t['weak']:
		plan_damage *= 2
	if 'immune' in t and u['attack_type'] in t['immune']:
		plan_damage = 0
	return plan_damage


def sim(boost=0, debug=True, part2=False):
	immune = copy.deepcopy(masterimmune)
	infection = copy.deepcopy(masterinfection)
	for i in immune:
		i['attack_power'] += boost

	forever = 0
	while len(immune) > 0 and len(infection) > 0 and forever < 100000: 
		forever += 1
		if debug:
			print 'Immune System:'
			for i in sorted(immune, key=lambda k:k['id']):
				print 'Group {0} contains {1} units'.format(i['id'],i['num'])
			print 'Infection:'
			for i in sorted(infection, key=lambda k:k['id']):
				print 'Group {0} contains {1} units'.format(i['id'],i['num'])
			print ''

		# Infection Target Selection
		already_targted = []
		for u in sorted(infection, key=lambda k:(-k['num']*k['attack_power'],-k['initiative'])):
			#print 'Infection_',u['id'], u['num'], u['hp'], u['initiative'], u['attack_type']
			pot_dam = []
			for t in immune:
				if t['id'] in already_targted:
					continue
				pot_dam.append(est_damage(u, t))
				if debug:
					print 'Infection group {0} would deal defending group {1} {2} damage'.format(u['id'],t['id'],pot_dam[-1])
			if len(pot_dam) == 0:
				u['target'] = None
				continue
			m = max(pot_dam)
			if m == 0:
				u['target'] = None
				continue
			pottar = [x for x in immune if est_damage(u,x) == m and x['id'] not in already_targted]
			if len(pottar) > 1:
				pottar = sorted(pottar,key=lambda k:(-k['num']*k['attack_power'],-k['initiative']))
			#for x in pottar:
			#	print x['id'],x['num'],x['attack_power'],x['num']*x['attack_power']
			u['target'] = pottar[0]['id']
			already_targted.append(pottar[0]['id'])

		# Immune Target Selection
		already_targted = []
		for u in sorted(immune, key=lambda k:(-k['num']*k['attack_power'],-k['initiative'])):
			#print 'System_',u['id'], u['num'], u['hp'], u['initiative'], u['attack_type']
			pot_dam = []
			for t in infection:
				if t['id'] in already_targted:
					continue
				pot_dam.append(est_damage(u, t))
				if debug:
					print 'Immune group {0} would deal defending group {1} {2} damage'.format(u['id'],t['id'],pot_dam[-1])
			if len(pot_dam) == 0:
				u['target'] = None
				continue
			m = max(pot_dam)
			if m == 0:
				u['target'] = None
				continue
			pottar = [x for x in infection if est_damage(u,x) == m and x['id'] not in already_targted]
			if len(pottar) > 1:
				pottar = sorted(pottar,key=lambda k:(-k['num']*k['attack_power'],-k['initiative']))
			u['target'] = pottar[0]['id']
			already_targted.append(pottar[0]['id'])
		if debug: print ''

		# Attack Phase
		temp = copy.deepcopy(infection)
		temp.extend(copy.deepcopy(immune))
		temp = sorted(temp, key=lambda k:(-k['initiative']))
		for t in temp:
			defender = None
			attacker = None
			if t['type'] == 'Infection' and 'target' in t and t['target'] != None:
				defender = [x for x in immune if x['id'] == t['target']][0]
				attacker = [x for x in infection if x['id'] == t['id']][0]
			elif t['type'] == 'Immune' and 'target' in t and t['target'] != None:
				defender = [x for x in infection if x['id'] == t['target']][0]
				attacker = [x for x in immune if x['id'] == t['id']][0]

			if defender != None:
				#if attacker['id'] == 6 and defender['id'] == 9:
				#	print 'attacker',attacker
				#	print 'defender',defender
				dead = min(est_damage(attacker, defender)/defender['hp'], defender['num'])
				defender['num'] -= dead
				if debug:
					print '{0} group {1} attacks defending group {2}, killing {3} units'.format(
								t['type'], t['id'], defender['id'], dead)
		if debug: print ''

		# Make sure to remove all dead units
		immune = [i for i in immune if i['num'] > 0]
		infection = [i for i in infection if i['num'] > 0]

	if forever == 100000:
		#print 'TIE LOOP?'
		return None

	if part2:
		if len(immune) == 0:
			return None
		return sum(x['num'] for x in immune)
	else:
		p1 = 0
		if len(immune) == 0:
			p1 = sum(x['num'] for x in infection)
		if len(infection) == 0:
			p1 = sum(x['num'] for x in immune)
		return p1
	

print 'Part1',sim(debug=False) # 16006
for boost in range(1,10000):
	foo = sim(debug=False, part2=True, boost=boost)
	if foo != None:
		print 'Part2',foo # 6221
		break
