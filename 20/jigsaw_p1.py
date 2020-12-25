# 144 tiles in Actual
# 9 Tiles in Test
import enum
import math
import sys

# sys.stdout = open('output.txt', 'w')


class enumVal(enum.Enum):
    X = '#'
    O = '.'


file = open('test_20.txt')

all_tiles = dict()
curr_tile = None
for line in file.readlines():
    stripped = line.strip()

    if not stripped:
        continue

    if 'Tile' in stripped:
        curr_tile = int(stripped[5:-1])
        all_tiles[curr_tile] = []
    else:
        all_tiles[curr_tile].append(list([enumVal(val).name for val in stripped]))


total_rows = total_cols = int(math.sqrt(len(all_tiles.keys())))
jigsaw = [[(0, 0, []) for i in range(total_rows)] for j in range(total_cols)]

order = [(i, j) for i in range(total_rows) for j in range(total_cols)]


def rotate_array_right(array):
    rotated_array = []

    for index in range(len(array)):
        rotated_array.append([arr[index] for arr in array])

    return rotated_array[::-1]


def flip_array_bottom(array):
    return array[::-1]


def get_neigh(coord, max_len):
    x, y = coord[0], coord[1]

    poss = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]

    coords = []
    for (i, j) in poss:
        if i >= max_len or j >= max_len or i < 0 or j < 0:
            continue
        coords.append((i, j))

    return coords


def give_possible_rotations(array):
    array_possibilities = [array]
    rotated = array
    for i in range(3):
        rotated = rotate_array_right(rotated)
        array_possibilities.append(rotated)

    rotated = flip_array_bottom(array)
    array_possibilities.append(rotated)
    for i in range(3):
        rotated = rotate_array_right(rotated)
        array_possibilities.append(rotated)

    return array_possibilities


def is_safe(jigsaw, key, tile, curr_coord):
    curr_order = order[curr_coord]
    neighbours = get_neigh(curr_order, len(jigsaw))

    match_neighbours = 0

    tile_first_row = tuple(tile[0])
    tile_first_col = tuple([t[0] for t in tile])
    tile_last_row = tuple(tile[-1])
    tile_last_col = tuple([t[-1] for t in tile])

    for neighbour in neighbours:
        (neigh_key, neigh_orient, neigh_tile) = jigsaw[neighbour[0]][neighbour[1]]

        if neigh_key == 0:
            match_neighbours += 1
            continue

        neigh_first_row = tuple(neigh_tile[0])
        neigh_first_col = tuple([t[0] for t in neigh_tile])
        neigh_last_row = tuple(neigh_tile[-1])
        neigh_last_col = tuple([t[-1] for t in neigh_tile])

        if curr_order[0] < neighbour[0]:
            # Neighbour is in Right
            if tile_last_col == neigh_first_col:
                match_neighbours += 1

        elif neighbour[0] < curr_order[0]:
            # Neighbour is in left
            if tile_first_col == neigh_last_col:
                match_neighbours += 1

        else:

            if curr_order[1] < neighbour[1]:
                # Neighbour is in Bottom
                if tile_last_row == neigh_first_row:
                    match_neighbours += 1
            else:

                # Neighbour is in top
                if tile_first_row == neigh_last_row:
                    match_neighbours += 1

    if match_neighbours == len(neighbours):
        # print("Neighbour Matches:{}".format(key))
        return True

    # If It doesnt pass any of the neighbours. Return False
    return False


def do_backtracking(jigsaw, available_keys, curr_coord):
    # print("Backtracking with Keys:{} Curr:{}".format(available_keys, curr_coord))

    if len(available_keys) == 0:
        return True

    if curr_coord >= len(order):
        return False

    curr_order = order[curr_coord]

    for key in available_keys:

        shallow_keys = available_keys.copy()
        shallow_keys.pop(shallow_keys.index(key))

        tile = all_tiles[key]
        for index, option in enumerate(give_possible_rotations(tile)):

            # print("Key Trying:{} C:{} I:{}".format(key, curr_coord, index))

            if is_safe(jigsaw, key, option, curr_coord):

                # print("Key Safe:{} C:{} I:{}".format(key, curr_coord, index))
                jigsaw[curr_order[0]][curr_order[1]] = (key, index, option)

                if do_backtracking(jigsaw, shallow_keys, curr_coord+1):
                    print("Passed:{} C:{}".format(key, curr_coord))
                    return True

                jigsaw[curr_order[0]][curr_order[1]] = (0, 0, 0)

        # print("Key Invalid:{} C:{}".format(key, curr_coord))
    return False


if not do_backtracking(jigsaw, list(all_tiles.keys()), 0):
    print("Not Found")

print("Found Solution:\n")
for coord in order:
    key, orient, tile = jigsaw[coord[0]][coord[1]]
    print("Key:{} O:{} At:{}".format(key, orient, coord))

corner_sum = jigsaw[0][0][0] * jigsaw[-1][0][0] * jigsaw[0][-1][0] * jigsaw[-1][-1][0]
print("Sum :{}".format(corner_sum))