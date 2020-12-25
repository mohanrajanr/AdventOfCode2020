import collections
import re
file = open('24.txt')

tile_location = []
for line in file.readlines():
    values = re.findall(r"e|w|ne|nw|se|sw", line.strip())
    tile_location.append(values)

diff_vector = {
    'e': (2, 0),
    'w': (-2, 0),
    'ne': (1, 1),
    'nw': (-1, 1),
    'se': (1, -1),
    'sw': (-1, -1)
}

floor = collections.defaultdict(lambda: False)

# Part 1
for tile in tile_location:
    x = y = 0
    for vec in tile:
        x += diff_vector[vec][0]
        y += diff_vector[vec][1]

    floor[(x, y)] = not floor[(x, y)]

print(len([value for value in floor.values() if value]))


def get_neighbours(coords):
    return [(coords[0] + vec[0], coords[1] + vec[1]) for vec in diff_vector.values()]

# Part 2
for day in range(100):

    new_floor = collections.defaultdict(lambda: False)

    coords = set()
    for vector in floor.keys():
        neighbours = get_neighbours(vector)
        coords.update(neighbours)

    for (x, y) in coords:

        color = floor[(x, y)]
        neighbours = get_neighbours((x, y))

        black_tiles_adj = [value for value in neighbours if floor[value]]

        if color:
            # Black
            if len(black_tiles_adj) == 0 or len(black_tiles_adj) > 2:
                new_floor[(x, y)] = False
            else:
                new_floor[(x, y)] = True
        else:
            # White
            if len(black_tiles_adj) == 2:
                new_floor[(x, y)] = True
            else:
                new_floor[(x, y)] = False

    floor = new_floor
    print("Day {}: {}".format(day+1, len([value for value in floor.values() if value])))
