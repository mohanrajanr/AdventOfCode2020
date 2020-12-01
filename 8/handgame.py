
file = open('8.txt')

instructions = list()
for line in file.readlines():
    stripped = line.strip()
    instructions.append(stripped)

# Part 1
acc_val = 0
visited_locations = set()
start_index = 0
while start_index not in visited_locations:
    visited_locations.add(start_index)

    inst = instructions[start_index]
    command = inst[:3]
    exec = inst[3:].strip()

    if command == 'nop':
        start_index += 1
        continue

    elif command == 'acc':
        if exec[0] == '+':
            acc_val += int(exec[1:])
        else:
            acc_val -= int(exec[1:])
        start_index += 1

    elif command == 'jmp':
        if exec[0] == '+':
            start_index += int(exec[1:])
        else:
            start_index -= int(exec[1:])

print(acc_val)


# Part 2
def get_acc_value(insts):

    acc_val = 0
    visited_locations = set()
    start_index = 0

    while start_index < len(insts):
        if start_index in visited_locations:
            return 0

        visited_locations.add(start_index)

        inst = insts[start_index]
        command = inst[:3]
        exec = inst[3:].strip()

        if command == 'nop':
            start_index += 1
            continue

        elif command == 'acc':
            if exec[0] == '+':
                acc_val += int(exec[1:])
            else:
                acc_val -= int(exec[1:])
            start_index += 1

        elif command == 'jmp':
            if exec[0] == '+':
                start_index += int(exec[1:])
            else:
                start_index -= int(exec[1:])

    return acc_val

possible_locations_nop = [index for index in range(len(instructions)) if instructions[index][:3] == 'nop']
possible_locations_jmp = [index for index in range(len(instructions)) if instructions[index][:3] == 'jmp']

for position in possible_locations_nop:

    # Set the Modified Value
    inst = instructions[position]
    instructions[position] = "{}{}".format("jmp", inst[3:])

    # Whatever is not printed 0 is the answer
    val_check = get_acc_value(instructions)
    if val_check != 0:
        print(val_check)
        break

    # Rechanging the value back to original
    instructions[position] = inst

for position in possible_locations_jmp:

    # Set the Modified Value
    inst = instructions[position]
    instructions[position] = "{}{}".format("nop", inst[3:])

    # Whatever is not printed 0 is the answer
    val_check = get_acc_value(instructions)
    if val_check != 0:
        print(val_check)
        break

    # Rechanging the value back to original
    instructions[position] = inst
