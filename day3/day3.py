lines = open('day3.in', 'r').read().strip().replace('\n','.\n').split('\n')

p1 = 0
from collections import defaultdict
stars = defaultdict(set)
for i in range(len(lines)):
	curr_stars = []
	c = ''
	valid = False
	for j in range(len(lines[i])):
		if not lines[i][j].isdigit() and c != '':
			if valid:
				for (dx, dy) in curr_stars:
					stars[(dx,dy)].add(c)
				curr_stars = []
				p1 += int(c)
				c = ''		 
				valid = False
			else:
				c = ''
		elif lines[i][j].isdigit():
			c += lines[i][j]
			for (dx,dy) in [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]:
				new_dx = i + dx
				new_dy = j + dy
				if new_dx >= 0 and new_dx < len(lines) and new_dy >= 0 and new_dy < len(lines[i]):
					if not lines[new_dx][new_dy].isdigit() and lines[new_dx][new_dy] != '.':
						valid = True
					if lines[new_dx][new_dy] == '*':
						curr_stars.append((new_dx,new_dy))
p2 = 0
for (_,v) in stars.items():
	if len(v) == 2:
		p2 += int(v.pop()) * int(v.pop())
print(p1)
print(p2)
		
		
