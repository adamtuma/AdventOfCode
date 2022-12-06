### PART 1 ###

txt_file = open('2022/day6_input.txt', 'r')
input = txt_file.readlines()[0]
txt_file.close()

solution = "FALSE"
n = 0
        
while solution == "FALSE":
    k = 0
    string = input[n:n+4]
    for char in string:
        if string.count(char) == 1:
            k += 1
    if k == 4:
        solution = string
        position = n + 4
    n += 1

print(f"Answer for part one is: {position}")

### PART 2 ###

solution = "FALSE"
n = 0
        
while solution == "FALSE":
    k = 0
    string = input[n:n+14]
    for char in string:
        if string.count(char) == 1:
            k += 1
    if k == 14:
        solution = string
        position = n + 14
    n += 1

print(f"Answer for part two is: {position}")



