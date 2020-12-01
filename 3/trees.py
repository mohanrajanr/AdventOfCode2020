
file = open('3.txt')

tree_array = list()
rotation_size = 0
for line in file.readlines():
    stripped = line.strip()
    tree_array.append(stripped)
    rotation_size = len(stripped)

# Part 1
num_trees = 0
start_index = 0
step = 1
for ind in range(1, len(tree_array), step):
    line = tree_array[ind]

    if line[(start_index + 3) % rotation_size] == '#':
        num_trees += 1

    start_index += 3

print(num_trees)

# Part 2
combinations = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
final_result = 1
for (adder, step) in combinations:
    start_index = 0
    num_trees = 0
    for ind in range(0, len(tree_array), step):
        if ind == 0:
            continue

        line = tree_array[ind]

        if line[(start_index + adder) % rotation_size] == '#':
            num_trees += 1

        start_index += adder

    print(num_trees)
    final_result *= num_trees

print(final_result)
