### PART 1 ###

txt_file = open('2022/day9_input.txt', 'r')
data = [line.split() for line in txt_file]
txt_file.close()

start_coordinates = [0,0]
coordinates = []

def middle(number1, number2):
    middle_number = (number1 + number2)/2
    return int(middle_number)

def move(direction, coordinates):
    X = coordinates[0]
    Y = coordinates[1]
    if direction=="R":
        X += 1
    elif direction=="L":
        X -= 1
    elif direction=="U":
        Y += 1
    elif direction=="D":
        Y -= 1
    coordinates = [X,Y]
    return coordinates

def follow(coordinates_head, coordinates_tail):
    X_h = coordinates_head[0]
    Y_h = coordinates_head[1]
    X_t = coordinates_tail[0]
    Y_t = coordinates_tail[1]
    if abs(X_h - X_t) > 1 and abs(Y_h - Y_t)==0:
        X_t = middle(X_h, X_t)
    elif abs(X_h - X_t) > 1 and abs(Y_h - Y_t) > 0:
        X_t = middle(X_h, X_t)
        Y_t = Y_h
    elif abs(Y_h - Y_t) > 1 and abs(X_h - X_t)==0:
        Y_t = middle(Y_h, Y_t)
    elif abs(Y_h - Y_t) > 1 and abs(X_h - X_t) > 0:
        Y_t = middle(Y_h, Y_t)
        X_t = X_h
    coordinates_tail = [X_t, Y_t]
    return coordinates_tail

coordinates_head = [0,0]
coordinates_tail = [0,0]

for i in data:
    direction = i[0]
    moves = i[1]
    for n in range(int(moves)):
        coordinates_head = move(direction, coordinates_head)
        coordinates_tail = follow(coordinates_head, coordinates_tail)
        if coordinates_tail not in coordinates:
            coordinates.append(coordinates_tail)

print(f"Answer for part one is: {len(coordinates)}")

### PART 2 ###

coordinates = []
rope = []
for i in range(10):
    rope.append([0,0])

for i in data:
    direction = i[0]
    moves = i[1]
    for n in range(int(moves)):
        coordinates_head = move(direction, rope[0])
        rope[0] = coordinates_head
        for n, coords in enumerate(rope):
            if n == 9:
                break
            coordinates_n = follow(rope[n], rope[n+1])
            rope[n+1] = coordinates_n
        if rope[9] not in coordinates:
            coordinates.append(rope[9])

print(f"Answer for part two is: {len(coordinates)}")







