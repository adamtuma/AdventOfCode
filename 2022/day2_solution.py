### PART 1 ###

txt_file = open('2022/day2_input.txt', 'r')
data = [line.strip() for line in txt_file]
txt_file.close()

results = {
    "A X": 4,
    "A Y": 8,
    "A Z": 3,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 7,
    "C Y": 2,
    "C Z": 6
}

score = 0

for i in data:
    round = results.get(i)
    score += round

print(f"Answer for part one is: {score}")

### PART 2 ###

results2 = {
    "A X": 3,
    "A Y": 4,
    "A Z": 8,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 2,
    "C Y": 6,
    "C Z": 7
}

score2 = 0

for i in data:
    round = results2.get(i)
    score2 += round

print(f"Answer for part two is: {score2}")