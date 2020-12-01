
file = open('5.txt')

converter = {'F': '0', 'B': '1', 'L': '0', 'R': '1'}

input_lines = []
for line in file.readlines():
    stripped = line.strip()

    string = ''
    for v in stripped:
        string += converter[v]

    input_lines.append(string)


# Part 1:
seat_max = -1
for line in input_lines:
    row = line[:7]
    col = line[7:]

    seat_max = max(seat_max, int(row, 2) * 8 + int(col, 2))

print(seat_max)

# Part 2:
seat_nums = list()
for line in input_lines:
    row = line[:7]
    col = line[7:]

    seat_nums.append(int(row, 2) * 8 + int(col, 2))

seat_nums.sort()
start_val = seat_nums[0]
for ind in range(1, len(seat_nums)-1):
    if seat_nums[ind] == start_val + 2:
        print(seat_nums[ind] - 1)
        break
    start_val = seat_nums[ind]
