lines = open('day4.in').read().strip().split('\n')

from collections import defaultdict
p1 = 0
p2 = defaultdict(int)
for i, line in enumerate(lines):
	p2[i] += 1
	winning, given = line.split('|')
	winning = set(winning.split(':')[1].split())
	given = set(given.split())
	c = 0
	num_of_common = len(winning & given)
	if num_of_common > 0:
		p1 += 2**(num_of_common-1)
	for j in range(i+1,i+1+num_of_common):
		p2[j] +=  p2[i]
print(p1)		
print(sum(p2.values()))
