file = open('11.txt')

seating = list()
for line in file.readlines():
    seating.append(line.replace('L', '#').strip())

# print(seating)

# Part 1
# next_seating = []
# change_happened = True
#
# curr_dims = [(1, 1), (0, 1), (-1, 1), (-1, 0), (1, 0), (-1, -1), (0, -1), (1, -1)]
#
# while True:
#
#     for index in range(len(seating)):
#
#         curr_seating = seating[index]
#         for index2 in range(len(curr_seating)):
#
#             if seating[index][index2] == '.':
#                 continue
#
#             occupied = 0
#             empty = 0
#
#             for (x, y) in curr_dims:
#                 if 0 <= index + x < len(seating) and 0 <= index2 + y < len(curr_seating):
#
#                     if seating[index + x][index2 + y] == '#':
#                         occupied += 1
#                     else:
#                         empty += 1
#                 else:
#                     empty += 1
#
#             if seating[index][index2] == 'L':
#                 if occupied == 0:
#                     curr_seating = curr_seating[:index2] + '#' + curr_seating[index2+1:]
#             elif seating[index][index2] == '#':
#                 if occupied > 3:
#                     curr_seating = curr_seating[:index2] + 'L' + curr_seating[index2+1:]
#
#         next_seating.append(curr_seating)
#
#     # print("Output")
#     # for seat in next_seating:
#     #     print(seat)
#     # print("\n")
#
#     if next_seating == seating:
#         break
#
#     seating = next_seating
#     next_seating = []
#
# occu_count = 0
# for seat in seating:
#     occu_count += seat.count('#')
#
# print(occu_count)


# Part 2
next_seating = []
change_happened = True

curr_dims = [(1, 1), (0, 1), (-1, 1), (-1, 0), (1, 0), (-1, -1), (0, -1), (1, -1)]

while True:

    for index in range(len(seating)):

        curr_seating = seating[index]
        for index2 in range(len(curr_seating)):

            if seating[index][index2] == '.':
                continue

            occupied = 0
            empty = 0

            for (x, y) in curr_dims:

                temp_index, temp_index2 = index, index2

                change_made = False
                while 0 <= temp_index + x < len(seating) and 0 <= temp_index2 + y < len(curr_seating):

                    if seating[temp_index + x][temp_index2 + y] == '.':
                        temp_index += x
                        temp_index2 += y
                        continue

                    if seating[temp_index + x][temp_index2 + y] == '#':
                        occupied += 1
                    else:
                        empty += 1
                    change_made = True
                    break

                if not change_made:
                    empty += 1

            # Seat allocator does not change
            if seating[index][index2] == 'L':
                if occupied == 0:
                    curr_seating = curr_seating[:index2] + '#' + curr_seating[index2+1:]
            elif seating[index][index2] == '#':
                if occupied > 4:
                    curr_seating = curr_seating[:index2] + 'L' + curr_seating[index2+1:]

        next_seating.append(curr_seating)

    # print("Output")
    # for seat in next_seating:
    #     print(seat)
    # print("\n")

    if next_seating == seating:
        break

    seating = next_seating
    next_seating = []

occu_count = 0
for seat in seating:
    occu_count += seat.count('#')

print(occu_count)