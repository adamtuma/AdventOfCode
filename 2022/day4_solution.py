### PART 1 ###

txt_file = open('2022/day4_input.txt', 'r')
data = [line.strip() for line in txt_file]
txt_file.close()

data = [line.replace(",", "-") for line in data]
data = [line.split("-") for line in data]

counter = 0

for pair in data:
    set_1 = set(range(int(pair[0]),int(pair[1])+1))
    set_2 = set(range(int(pair[2]),int(pair[3])+1))
    if set_1.issubset(set_2):
        counter += 1
    elif set_2.issubset(set_1):
        counter += 1

print(f"Answer for part one is: {counter}")

### PART 2 ###

counter2 = 0

for pair in data:
    set_1 = set(range(int(pair[0]),int(pair[1])+1))
    set_2 = set(range(int(pair[2]),int(pair[3])+1))
    if len(set_1.intersection(set_2)) > 0:
        counter2 += 1

print(f"Answer for part two is: {counter2}")