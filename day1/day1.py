f = open('day1.in', 'r')

p1 = 0
p2 = 0
for line in f.readlines():
    nums = ['zero','one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine','0','1','2','3','4','5','6','7','8','9']
    
    first_occurences = [line.find(num) for num in nums]
    first_occurences = [num if num >= 0 else 1000 for num in first_occurences]
    last_occurences = [line.rfind(num) for num in nums]

    first_num = first_occurences.index(min(first_occurences)) % 10
    last_num = last_occurences.index(max(last_occurences)) % 10

    numbers = ''.join(filter(str.isnumeric, line))
    p1 += int(numbers[0] + numbers[-1])
    p2 += int(str(first_num) + str(last_num))

print(p1, p2)
