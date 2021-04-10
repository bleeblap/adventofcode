from functools import reduce

innum = 29000000

# https://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python
def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

cur = 1
p1 = True
p2 = True
while p1 or p2:
	fac = factors(cur)
	if p1 and sum(fac)*10 > innum:
		print 'Part1',cur
		p1 = False
	if p2 and sum(filter(lambda y: y*50>=cur, fac))*11 > innum:
		print 'Part2',cur
		p2 = False
	cur += 1