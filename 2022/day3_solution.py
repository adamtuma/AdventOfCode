### PART 1 ###
import string

txt_file = open('2022/day3_input.txt', 'r')
data = [line.strip() for line in txt_file]
txt_file.close()

first_halves = []
second_halves = []

for i in data:
    x = len(i)//2
    first_halves.append(i[:x])
    second_halves.append(i[x:])

both_compartments = []

for n in range(0,len(data)):
    x = set(first_halves[n])
    y = set(second_halves[n])
    both_compartments.append(list(x&y)[0])

priorities = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

sum_priorities = 0

for j in both_compartments:
    sum_priorities += (priorities.index(j)+1)

print(f"Answer for part one is: {sum_priorities}")

### PART 2 ###

groups_letter = []
sum_priorities2 = 0

for n in range(0,len(data))[::3]:
    x = set(data[n])
    y = set(data[n+1])
    z = set(data[n+2])
    groups_letter.append(list(x&y&z)[0])

for k in groups_letter:
    sum_priorities2 += (priorities.index(k)+1)

print(f"Answer for part two is: {sum_priorities2}")
