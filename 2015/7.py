#!/usr/bin/env python

import sys
import copy

infile = open('7.in','r').read()
infile2 = '''123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i'''

wire_states = {}
operations = []
for line in infile.split('\n'):
	instr = {}
	instr['outw'] = line.split('-> ')[1]
	op = line.split('->')[0]
	if op.count(' ') == 1:
		instr['opcode'] = 'SET'
		try:
			instr['imm1'] = int(op.split(' ')[0])
		except:
			instr['w1'] = op.split(' ')[0]
	elif op.count(' ') == 2:
		assert op.split(' ')[0] == 'NOT'
		instr['opcode'] = 'NOT'
		instr['w1'] = op.split(' ')[1]
	elif op.count(' ') == 3:
		instr['opcode'] = op.split(' ')[1]
		try:
			instr['imm1'] = int(op.split(' ')[0])
		except:
			instr['w1'] = op.split(' ')[0]
		try:
			instr['imm2'] = int(op.split(' ')[2])
		except:
			instr['w2'] = op.split(' ')[2]
	else:
		assert(op)

	if 'outw' in instr: wire_states[instr['outw']] = None
	if 'w1' in instr: wire_states[instr['w1']] = None
	if 'w2' in instr: wire_states[instr['w2']] = None
	#print line, instr
	operations.append(instr)

def SET(wire_states, op):
	if 'imm1' in op:
		return op['imm1']
	else:
		return wire_states[op['w1']]	

def LSHIFT(wire_states, op):
	if 'imm1' in op and 'imm2' in op:
		return op['imm1'] << op['imm2']
	elif 'imm1' in op and 'w2' in op:
		return op['imm1'] << wire_states[op['w2']]
	elif 'w1' in op and 'imm2' in op:
		return wire_states[op['w1']] << op['imm2']
	elif 'w1' in op and 'w2' in op:
		return wire_states[op['w1']] << wire_states[op['w2']]
	else:
		assert('RSHIFT',op)

def RSHIFT(wire_states, op):
	if 'imm1' in op and 'imm2' in op:
		return op['imm1'] >> op['imm2']
	elif 'imm1' in op and 'w2' in op:
		return op['imm1'] >> wire_states[op['w2']]
	elif 'w1' in op and 'imm2' in op:
		return wire_states[op['w1']] >> op['imm2']
	elif 'w1' in op and 'w2' in op:
		return wire_states[op['w1']] >> wire_states[op['w2']]
	else:
		assert('RSHIFT',op)

def AND(wire_states, op):
	if 'imm1' in op and 'imm2' in op:
		return op['imm1'] & op['imm2']
	elif 'imm1' in op and 'w2' in op:
		return op['imm1'] & wire_states[op['w2']]
	elif 'w1' in op and 'imm2' in op:
		return wire_states[op['w1']] & op['imm2']
	elif 'w1' in op and 'w2' in op:
		return wire_states[op['w1']] & wire_states[op['w2']]
	else:
		assert('RSHIFT',op)

def OR(wire_states, op):
	if 'imm1' in op and 'imm2' in op:
		return op['imm1'] | op['imm2']
	elif 'imm1' in op and 'w2' in op:
		return op['imm1'] | wire_states[op['w2']]
	elif 'w1' in op and 'imm2' in op:
		return wire_states[op['w1']] | op['imm2']
	elif 'w1' in op and 'w2' in op:
		return wire_states[op['w1']] | wire_states[op['w2']]
	else:
		assert('RSHIFT',op)

def NOT(wire_states, op):
	return ~wire_states[op['w1']]

opscopy = copy.deepcopy(operations)
wirecopy = copy.deepcopy(wire_states)
while len(operations) > 0:
	for op in operations:
		if ('w1' in op and wire_states[op['w1']] == None) or ('w2' in op and wire_states[op['w2']] == None):
			continue # Not ready to execute this instruction yet
		#print 'DO',op
		wire_states[op['outw']] = (globals()[op['opcode']](wire_states, op) & 0xFFFF)
		operations.remove(op)
		break

print 'Part1',wire_states['a']

p1 = wire_states['a']
operations = opscopy
wire_states = wirecopy
wire_states['b'] = p1
while len(operations) > 0:
	for op in operations:
		if ('w1' in op and wire_states[op['w1']] == None) or ('w2' in op and wire_states[op['w2']] == None):
			continue # Not ready to execute this instruction yet
		wire_states[op['outw']] = (globals()[op['opcode']](wire_states, op) & 0xFFFF)
		operations.remove(op)
		break
print 'Part2',wire_states['a']
