### PART 1 ###

txt_file = open('2022/day5_input.txt', 'r')
data = txt_file.readlines()
txt_file.close()

# preparing stacks data
stacks_data = data[0:8]
stacks_data.reverse()
stacks = [[],[],[],[],[],[],[],[],[]]

for row in stacks_data:
    for n in range(1,34,4): #taking every 4th value which correspond to the letter
        if row[n] == " ": 
            pass
        else:
            stacks[n//4].append(row[n])

stacks2 = stacks #copy for 2nd part

# preparing moves data
moves_data = data[10:]
moves = []

for row in moves_data:
    round = [int(row.split()[1]),int(row.split()[3]),int(row.split()[5])]
    moves.append(round)

# function which makes one move
def one_move(starting_stack, move_list):
    stacks = starting_stack
    amount = move_list[0]
    origin = move_list[1]-1
    to = move_list[2]-1
    for n in range(1,amount+1):
        stacks[to].append(stacks[origin][-n])
    stacks[origin] = stacks[origin][:-amount]
    return stacks


for move in moves:
    stacks = one_move(stacks,move)

answer1 = ""
for stack in stacks:
    answer1 += stack[-1]

print(f"Answer for part one is: {answer1}")

### PART 2 ###

def one_move_2(starting_stack, move_list):
    stacks = starting_stack
    amount = move_list[0]
    origin = move_list[1]-1
    to = move_list[2]-1
    stacks[to]= stacks[to] + stacks[origin][-amount:]
    stacks[origin] = stacks[origin][:-amount]
    return stacks


for move in moves:
    stacks2 = one_move_2(stacks2,move)

answer2 = ""
for stack in stacks2:
    answer2 += stack[-1]

print(f"Answer for part two is: {answer2}")