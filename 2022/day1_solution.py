### PART 1 ###

txt_file = open('day1_input.txt', 'r')
data = [line.strip() for line in txt_file]
txt_file.close()

calories = []
i_kcal = 0

for i in data:
    if i == "":
        calories.append(i_kcal)
        i_kcal = 0 
    else:
       i_kcal += int(i)

    
kcal_max = max(calories)

print(f"Answer for part one is: {kcal_max}")

### PART 2 ###

calories.sort(reverse = True)

print(f"Answer for part two is: {sum(calories[0:3])}")