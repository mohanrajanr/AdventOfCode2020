import collections

file = open('15.txt')

numbers = list()
sets = list()
for test_set in file.readlines():
    numbers = list(map(int, test_set.split(',')))
    sets.append(numbers)

# for each test case
# Part 1 - 2020 & Part 2 - 30000001
for numbers in sets:
    last_occurance = collections.defaultdict(list)

    for ind, num in enumerate(numbers, 1):
        last_occurance[num].append(ind)

    index = len(numbers) + 1
    last_val = numbers[-1]

    while index < 30000001:

        curr_list = last_occurance[last_val]

        if len(curr_list) < 2:
            last_occurance[0].append(index)
            last_val = 0

        else:

            prev, latest = curr_list[-2], curr_list[-1]
            last_val = latest - prev
            last_occurance[last_val].append(index)

        print("Index:{} LastVal:{}".format(index, last_val))
        index += 1

    print("Test:{} Val:{}".format(numbers, last_val))
