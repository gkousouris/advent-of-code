lines = open('day4.in').read().strip().split('\n')
#lines = open('day4_test.in').read().strip().split('\n')

ans = 0
p2 = {}
for i, line in enumerate(lines):
	p2[i] = p2.get(i,0) + 1
	winning, given = line.split('|')
	winning = set(winning.split(':')[1].split())
	given = given.split()
	curr_card_winnings = 0
	c = 0
	for num in given:
		if num in winning:
			c += 1	
			if curr_card_winnings == 0:
				curr_card_winnings = 1
			else:
				curr_card_winnings *= 2
	for j in range(i+1,i+1+c):
		p2[j] = p2.get(j,0) + p2[i]
	ans += curr_card_winnings
print(ans)		
print(sum(p2.values()))
