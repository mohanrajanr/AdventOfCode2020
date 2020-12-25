import collections

file = open('14.txt')

instructions = list()
for line in file.readlines():
    instructions.append(line.strip())

memory_address = collections.defaultdict(int)
mask = instructions[0].split(" = ")[1].strip()
len_mask = len(mask)

# # Part 1
# for inst in instructions[1:]:
#     splitted = inst.split(" = ")
#
#     if splitted[0].strip()[:4] == 'mask':
#         mask = splitted[1].strip()
#         continue
#
#     mem_address = int(splitted[0].strip()[4:-1])
#     value = int(splitted[1].strip())
#     bit_val = bin(value)[2:]
#
#     # Computation
#     string_val = []
#     len_bit_val = len(bit_val)
#     for ind in range(len_mask):
#         if mask[len_mask-1 - ind] == 'X':
#             string_val.append(bit_val[len_bit_val-1-ind] if ind < len_bit_val else '0')
#         else:
#             string_val.append(mask[len_mask-1 - ind])
#
#     mem_string = ''
#     for stri in reversed(string_val):
#         mem_string += stri
#
#     print("MASK:{} BIT_VAL:{} S:{}".format(mask, bit_val, mem_string))
#     memory_address[mem_address] = int(mem_string, 2)
#
# total_val = 0
# for value in memory_address.values():
#     total_val += value
#
# print(total_val)


# Part 2
import copy
for inst in instructions[1:]:
    splitted = inst.split(" = ")

    if splitted[0].strip()[:4] == 'mask':
        mask = splitted[1].strip()
        print("Changing Mask:{}".format(mask))
        continue

    mem_address = int(splitted[0].strip()[4:-1])
    value = int(splitted[1].strip())
    bit_val = bin(mem_address)[2:]

    # Computation
    string_val = []
    len_bit_val = len(bit_val)
    for ind in range(len_mask):
        if mask[len_mask-1-ind] == 'X':
            string_val.append('X')
        else:
            string_val.append('1' if mask[len_mask-1-ind] == '1' or (ind <= len_bit_val -1 and bit_val[len_bit_val-1-ind] == '1') else '0')

    should_conv  = [string_val]
    possible_combs = []
    while should_conv:
        possible_val = should_conv.pop()
        is_converted = False

        for ind in range(len(possible_val)-1, -1, -1):
            if possible_val[ind] != 'X':
                continue
            is_converted = True
            possible_val[ind] = '0'
            should_conv.append(copy.deepcopy(possible_val))
            possible_val[ind] = '1'
            should_conv.append(copy.deepcopy(possible_val))
            break

        if not is_converted:
            possible_combs.append(copy.deepcopy(possible_val))

    for possible_val in possible_combs:
        mem_string = ''
        for stri in reversed(possible_val):
            mem_string += stri

        print("MASK:{} MEM:{} BIT_VAL:{} S:{} VAL:{}".format(mask, mem_address, bit_val, mem_string, int(mem_string, 2)))
        memory_address[int(mem_string, 2)] = value

total_val = 0
for values in memory_address.values():
    total_val += values

print(total_val)