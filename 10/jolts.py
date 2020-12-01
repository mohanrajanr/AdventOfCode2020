file = open('10.txt')

jolt_adapter = list()
for line in file.readlines():
    jolt_adapter.append(int(line.strip()))

# Device Built In
jolt_adapter.append(max(jolt_adapter) + 3)

# Charging Port
jolt_adapter.append(0)

len_adap = len(jolt_adapter)

# Part 1
jolt_adapter.sort()
sum_diff = {1: 0, 2: 0, 3: 0}

for index in range(1, len_adap):
    sum_diff[abs(jolt_adapter[index-1] - jolt_adapter[index])] += 1

print(sum_diff)

# Part 2
possible = dict()

# Last Value
possible[jolt_adapter[len_adap-1]] = 1


def find_possible(index):
    print("Trying for {}".format(index))
    if jolt_adapter[index] in possible:
        return possible[jolt_adapter[index]]

    plus = {1: 0, 2: 0, 3: 0}

    for key in plus.keys():
        if index + 1 < len_adap and jolt_adapter[index] + key == jolt_adapter[index + 1]:
            plus[key] = find_possible(index + 1)
        elif index + 2 < len_adap and jolt_adapter[index] + key == jolt_adapter[index + 2]:
            plus[key] = find_possible(index + 2)
        elif index + 3 < len_adap and jolt_adapter[index] + key == jolt_adapter[index + 3]:
            plus[key] = find_possible(index + 3)

    possible[jolt_adapter[index]] = plus[1] + plus[2] + plus[3]
    return possible[jolt_adapter[index]]

print(find_possible(0))
