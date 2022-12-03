f = open('input.txt', 'r')
lines = f.readlines()

sums = []

sum = 0
for line in lines:
    if line != '\n':
        calories = int(line)
        sum += calories
    else:
        sums.append(sum)
        sum = 0

sums.sort()

print(f'Most calories is {sums[-1]}')
print(f'The top three Elves are carrying {sums[-1] + sums[-2] + sums[-3]}')
