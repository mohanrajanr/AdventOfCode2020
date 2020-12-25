# 144 tiles in Actual
# 9 Tiles in Test
import enum
import math

class enumVal(enum.Enum):
    X = '#'
    O = '.'

file = open('20.txt')
part1 = open('part1_out')

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


def rotate_array_right(array):
    rotated_array = []

    for index in range(len(array)):
        rotated_array.append([arr[index] for arr in array])

    return rotated_array[::-1]


def flip_array_bottom(array):
    return array[::-1]


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


def prefetch_jigsaw():
    no_lines = 0
    values = []
    for line in part1.readlines():
        no_lines += 1
        main = line.split(":")
        key = main[1][:-2]
        orient = main[2][:-3]
        coords = main[-1][1:-2].split(",")
        values.append((key, orient, coords))

    total_rows = total_cols = int(math.sqrt(no_lines))
    jigsaw = [[(0, 0, []) for i in range(total_rows)] for j in range(total_cols)]

    for key, orient, coords in values:
        option = give_possible_rotations(all_tiles[int(key)])[int(orient)]

        jigsaw[int(coords[0])][int(coords[1])] = (key, orient, option)

    return jigsaw, total_rows, total_cols

jigsaw, total_rows, total_cols = prefetch_jigsaw()

order = [(i, j) for i in range(total_rows) for j in range(total_cols)]
tile_rows = tile_cols = len(list(all_tiles.values())[0])
full_picture = [[0 for i in range(tile_rows*total_rows)] for j in range(tile_cols*total_cols)]
# Part 2
for coord in order:
    key, orient, tile = jigsaw[coord[0]][coord[1]]
    start_x = coord[0] * tile_rows
    start_y = coord[1] * tile_cols

    tile = rotate_array_right(tile)
    tile = flip_array_bottom(tile)

    # print("Writing Key:{} SX:{} SY:{}".format(key, start_x, start_y))
    for i in range(1, tile_rows -1):
        for j in range(1, tile_cols -1):
            full_picture[start_x + i][start_y + j] = tile[i][j]

    # for i in range(total_rows*total_rows):
    #     for j in range(total_cols*total_cols):
    #         full_picture[start_x+i][start_y+j] = tile[i][j]

# print("Full Picture:\n")
# for i in range(tile_rows*total_rows):
#     for j in range(tile_rows*total_rows):
#         print(full_picture[i][j], end=" ")
#     print("\n")

# print("Removing Border")
borderless_pic = list()
for i in range(tile_rows*total_rows):
    new_list = []
    for j in range(tile_rows*total_rows):

        if full_picture[i][j] == 0:
            continue

        new_list.append(full_picture[i][j])
    if new_list:
        borderless_pic.append(new_list)

sea_monster = [
    ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'X', 'A'],
    ['X', 'A', 'A', 'A', 'A', 'X', 'X', 'A', 'A', 'A', 'A', 'X', 'X', 'A', 'A', 'A', 'A', 'X', 'X', 'X'],
    ['A', 'X', 'A', 'A', 'X', 'A', 'A', 'X', 'A', 'A', 'X', 'A', 'A', 'X', 'A', 'A', 'X', 'A', 'A', 'A']
]


def does_match_sea_monster(picture, monster, startx, starty):
    for i in range(len(monster[0])):
        for j in range(len(monster)):
            if monster[j][i] == 'X':
                if picture[startx + j][starty + i] != 'X':
                    return False
    return True

for pic in give_possible_rotations(borderless_pic):

    # print("Borderless:\n")
    # for i in range(len(borderless_pic)):
    #     for j in range(len(borderless_pic[i])):
    #         print(borderless_pic[i][j], end=" ")
    #     print("")

    no_of_monsters = 0
    for i in range(len(pic) - len(sea_monster[0])):

        for j in range(len(pic) - len(sea_monster)):

            if does_match_sea_monster(pic, sea_monster, j, i):
                no_of_monsters += 1

    monster_x_count = sum([val.count('X') for val in sea_monster])
    picture_x_count = sum([val.count('X') for val in pic])

    if no_of_monsters > 0:
        print(picture_x_count - (no_of_monsters * monster_x_count))
        break
    else:
        print("Nope")
