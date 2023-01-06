### PART 1 ###

txt_file = open('2022/day10_input.txt', 'r')
data = [line.split() for line in txt_file]
txt_file.close()

X = 1
cycle = 0
cycles = [20,60,100,140,180,220]
sum_strengths = 0

def check_cycle(cycle,cycles,X):
    if cycle in cycles:
        multiplier = X*cycle
    else:
        multiplier = 0
    return multiplier

for command in data:
    if command[0] == "noop":
        cycle +=1
        sum_strengths += check_cycle(cycle, cycles, X)
    else:
        cycle += 1
        sum_strengths += check_cycle(cycle, cycles, X)
        cycle += 1
        sum_strengths += check_cycle(cycle, cycles, X)
        X += int(command[1])

print(f"Answer for part one is: {sum_strengths}")

### PART 2 ###

string = 240*"."
sprite_pos = [0,1,2]
cycle = 0
line = 0

def replacer(index, string):
    string = string[:index] + "#" + string[index + 1:]
    return string

def add_cycle(cycle, line, sprite_pos):
    cycle += 1
    if cycle%40 == 0:
        line += 1
        for n,i  in enumerate(sprite_pos):
            sprite_pos[n] = i + 40
    return cycle, line

for command in data:
    if command[0] == "noop":
        if cycle in sprite_pos:
            string = replacer(cycle, string)
        cycle, line = add_cycle(cycle, line, sprite_pos)
    else:
        if cycle in sprite_pos:
            string = replacer(cycle, string)
        cycle, line = add_cycle(cycle, line, sprite_pos)
        if cycle in sprite_pos:
            string = replacer(cycle, string)
        for n,i  in enumerate(sprite_pos):
            sprite_pos[n] = i + int(command[1])
        cycle, line = add_cycle(cycle, line, sprite_pos)

for i in range(0,240,40):
    print(string[i:i+39])


    
