f = open('input.txt', 'r')
lines = f.readlines()

elfs = []
sums = []

buffer = []
sum = 0
for line in lines:
    if line != '\n':
        calories = int(line)
        buffer.append(calories)
        sum += calories
    else:
        elfs.append(buffer)
        sums.append(sum)
        elfs = []
        sum = 0

sums.sort()

print(f'Most calories is {sums[-1]}')

print(elfs)
print(sums)