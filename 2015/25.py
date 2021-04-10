import re
import sys

trow, tcol = [int(x)-1 for x in re.findall('(\d+)', open('25.in').read())]
cur = 20151125

d = 0
while True:
	d += 1
	for i in range(d,-1,-1):
		row = i
		col = d-i
		cur = (cur*252533)%33554393
		if row == trow and col == tcol:
			print 'part1',cur
			sys.exit(0)