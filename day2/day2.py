lines = open('day2.in', 'r').read().strip()

colours = {
'blue': 14,
'red': 	12,
'green': 13
}
ans = 0
for i, line in enumerate(lines.split('\n')):
    possible = True
    rounds = line.split(':')[1].split(';')
    for round in rounds:
        colour_nums = round.split(',')
        for colour_num in colour_nums:
            num, col = colour_num.strip().split(' ')
            if colours[col] < int(num):
                possible = False
    if possible:
        ans += (i+1)
print(ans)

p2 = 0
for i, line in enumerate(lines.split('\n')):
    colours = {}
    possible = True
    rounds = line.split(':')[1].split(';')
    for round in rounds:
        colour_nums = round.split(',')
        for colour_num in colour_nums:
            num, col = colour_num.strip().split(' ')
            colours[col] = max(colours.get(col,-1), int(num))
    prod = 1
    for v in colours.values():
        prod *= v
    p2 += prod
print(p2)
