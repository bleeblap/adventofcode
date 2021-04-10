infile = open('23.in').read()

def hlf(state, r):
	state[r] = state[r]/2

def tpl(state, r):
	state[r] = state[r]*3

def inc(state, r):
	state[r] = state[r]+1

def jmp(state, r):
	state['pc'] = state['pc'] + (int(r)-1)

def jie(state, r, c):
	if not state[r]%2:
		state['pc'] = state['pc'] + (int(c)-1)

def jio(state, r, c):
	if state[r]==1:
		state['pc'] = state['pc'] + (int(c)-1)

instrs = {
	'hlf': hlf,
	'tpl': tpl,
	'inc': inc,
	'jmp': jmp,
	'jie': jie,
	'jio': jio
}

cmds = infile.split('\n')

def run_sim(state):
	while state['pc'] >= 0 and state['pc'] < len(cmds):
		#print cmds[state['pc']]
		if ',' in cmds[state['pc']]:
			cmd,a1,a2 = [a.rstrip(',') for a in cmds[state['pc']].split(' ')]
			instrs[cmd](state,a1,a2)
		else:
			cmd,a1 = cmds[state['pc']].split(' ')
			instrs[cmd](state, a1)
		state['pc'] += 1

	return state['b']

state = {'a':0,'b':0,'pc':0}
print 'part1',run_sim(state)

state = {'a':1,'b':0,'pc':0}
print 'part2',run_sim(state)