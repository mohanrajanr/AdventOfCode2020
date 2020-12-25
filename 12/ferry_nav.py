file = open('12.txt')

instructions = list()
for line in file.readlines():
    instructions.append(line.strip())

direction_order = ['north', 'east', 'south', 'west']

# # Part 1
# directions = {'north': 0, 'east': 0, 'west': 0, 'south': 0}
# curr_direction = 'east'
#
# for inst in instructions:
#     action = inst[0]
#     val = int(inst[1:])
#
#     if action in ['R', 'L']:
#         val = int(val / 90)
#         index = direction_order.index(curr_direction)
#         fut_index = (index + val) % 4 if action == 'R' else (index - val) % 4
#         curr_direction = direction_order[fut_index]
#
#     elif action == 'F':
#         directions[curr_direction] += val
#     elif action == 'R':
#         directions[curr_direction] -= val
#
#     elif action == 'N':
#         directions['north'] += val
#     elif action == 'W':
#         directions['west'] += val
#     elif action == 'E':
#         directions['east'] += val
#     elif action == 'S':
#         directions['south'] += val
#
# print(directions)
# print(abs(directions['east'] - directions['west']) + abs(directions['north'] - directions['south']))


# Part 2
directions = {'north': 0, 'east': 0, 'west': 0, 'south': 0}
waypoint = {'north': 1, 'east': 10, 'west': 0, 'south': 0}
curr_direction = 'east'

for inst in instructions:
    action = inst[0]
    val = int(inst[1:])

    if action in ['R', 'L']:
        val = int(val / 90)
        while val:
            if action == 'L':
                waypoint['north'], waypoint['east'], \
                waypoint['south'], waypoint['west'] = waypoint['east'], waypoint['south'], \
                                                      waypoint['west'], waypoint['north']
            if action == 'R':
                waypoint['north'], waypoint['east'], \
                waypoint['south'], waypoint['west'] = waypoint['west'], waypoint['north'], \
                                                      waypoint['east'], waypoint['south']
            val -= 1

    elif action == 'F':
        for dir in direction_order:
            directions[dir] += (val * waypoint[dir])
    elif action == 'R':
        for dir in direction_order:
            directions[dir] += (val * waypoint[dir])

    elif action == 'N':
        waypoint['north'] += val
    elif action == 'W':
        waypoint['west'] += val
    elif action == 'E':
        waypoint['east'] += val
    elif action == 'S':
        waypoint['south'] += val

    # print(waypoint)
    # print(directions)

# print(directions)
print(abs(directions['east'] - directions['west']))
print(abs(directions['north'] - directions['south']))
print(abs(directions['east'] - directions['west']) + abs(directions['north'] - directions['south']))
