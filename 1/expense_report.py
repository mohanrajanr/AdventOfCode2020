
# Input
file = open('1.txt')

# HashSet
num_list = set()
for inp_str in file.readlines():
    num_list.add(int(inp_str.strip()))

# Part 1
for num in num_list:
    if 2020 - num in num_list:
        print(num * (2020 - num))
        break

# Part 2
num = list(num_list)
for i in range(len(num_list)):
    for j in range(len(num_list)):
        if i == j:
            continue

        for k in range(len(num_list)):
            if i == k or j == k:
                continue

            if num[i] + num[j] + num[k] == 2020:
                print(num[i] * num[j] * num[k])
                break
