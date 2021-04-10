from itertools import combinations

infile = open('24.in').read()

nums = [int(a) for a in infile.split('\n')]
nums.reverse()

def sim(nums, target):
	best = 999999999999999999999999999999
	foundx = False

	for x in range(len(nums)):
		for b in combinations(nums, x):
			if sum(b) != target:
				continue
			#print(b)
			foundx = True
			qe = reduce((lambda x,y: x*y), b)
			if qe < best:
				best = qe
		if foundx:
			return best
		
print 'part1',sim(nums,sum(nums)//3)
print 'part2',sim(nums,sum(nums)//4)