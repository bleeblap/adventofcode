#!/usr/bin/env python3

from copy import copy

tape = '''nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6'''.split('\n')
tape = open('8.in').readlines()

def sim(tape):
	pc = 0
	acc = 0
	history = set()
	while True:
		if pc in history:
			return False,acc
		history.add(pc)
		if pc >= len(tape):
			return True,acc
		ins, op = tape[pc].split(' ')
		#print(pc,ins,op)
		if ins == 'acc':
			acc += int(op)
			pc += 1
		elif ins == 'jmp':
			pc += int(op)
		elif ins == 'nop':
			pc += 1
_,p1 = sim(tape)
print('part1',p1)

for i in range(len(tape)):
	test = copy(tape)
	ins, op = tape[i].split(' ')
	if ins == 'acc':
		continue
	elif ins == 'jmp':
		test[i] = 'nop ' + op
	elif ins == 'nop':
		test[i] = 'jmp ' + op
	halt,acc = sim(test)
	if halt:
		print('part2',acc)
		break
