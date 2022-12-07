### PART 1 ###

txt_file = open('2022/day7_input.txt', 'r')
data = [line.strip() for line in txt_file]
txt_file.close()

directories = {}
dir_path = ""
curr_dir_paths = []
file_memory = []
separator = "/"

for row in data:
    if row[0] == "$":
        if row.split()[1] == "cd":
            if row.split()[2] == "..":
                curr_dir_paths = curr_dir_paths[:-1]
                dir_path = curr_dir_paths[-1]
            else:
                dir_path = dir_path + row.split()[2] + "/" 
                curr_dir_paths.append(dir_path)
        else:
            continue
    elif row.split()[0] == "dir":
        continue
    else:
        file = row.split()[1]
        file_path = dir_path + "/" + file
        if file_path in file_memory:
            continue
        size = int(row.split()[0])
        for dir in curr_dir_paths:
            if dir in directories:
                directories[dir] += size
            else:
                directories[dir] = size
        file_memory.append(file_path)

sum = 0
for dir in directories:
    dir_size = directories[dir]
    if dir_size <= 100000:
        sum += dir_size

print(f"Answer for part one is: {sum}")

### PART 2 ###

sorted_directories = dict(sorted(directories.items(), key=lambda item: item[1]))
space_needed = 30000000 - (70000000 - directories["//"])

for dir in sorted_directories:
    dir_size = sorted_directories[dir]
    if dir_size > space_needed:
        print(f"Answer for part two is: {dir_size}")
        break