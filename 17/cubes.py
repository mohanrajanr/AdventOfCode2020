import collections

file = open('17.txt')

initial_cube = list()

for line in file.readlines():
    initial_cube.append(list(line.strip()))

print(initial_cube)

dimensions = collections.defaultdict(lambda: '.')

# Part 1
for x in range(len(initial_cube)):
    for y in range(len(initial_cube[x])):
        dimensions[(x, y, 0)] = initial_cube[x][y]


def get_neighbours(coordinate):
    (x, y, z) = coordinate

    coordinates = set()
    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                if i == 0 and j == 0 and k == 0:
                    continue

                coordinates.add((x+i, y+j, z+k))

    return coordinates

for index in range(6):

    new_dimension = collections.defaultdict(lambda: '.')

    coords = set()
    for key in dimensions.keys():
        neigh = get_neighbours(key)

        coords = coords | neigh

    for (x, y, z) in coords:

        neighbour = get_neighbours((x, y, z))
        active = 0
        for neigh in neighbour:
            if dimensions[neigh] == '#':
                active += 1

        # print(active)
        # print(dimensions[(x, y, z)])
        if dimensions[(x, y, z)] == '#':
            if active == 2 or active == 3:
                new_dimension[(x, y, z)] = '#'
            else:
                new_dimension[(x, y, z)] = '.'
        else:
            if active == 3:
                new_dimension[(x, y, z)] = '#'
            else:
                new_dimension[(x, y, z)] = '.'

    # print(dimensions)
    # print(new_dimension)
    dimensions = new_dimension

active = 0
for dimen in dimensions.values():
    if dimen == '#':
        active +=1

print(active)


# Part 2
dimensions = collections.defaultdict(lambda: '.')
for x in range(len(initial_cube)):
    for y in range(len(initial_cube[x])):
        dimensions[(x, y, 0, 0)] = initial_cube[x][y]


def get_neighbours(coordinate):
    (x, y, z, w) = coordinate

    coordinates = set()
    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                for l in range(-1, 2):
                    if i == 0 and j == 0 and k == 0 and l == 0:
                        continue

                    coordinates.add((x+i, y+j, z+k, w+l))

    return coordinates

for index in range(6):

    new_dimension = collections.defaultdict(lambda: '.')

    coords = set()
    for key in dimensions.keys():
        neigh = get_neighbours(key)

        coords = coords | neigh

    for (x, y, z, w) in coords:

        neighbour = get_neighbours((x, y, z, w))
        active = 0
        for neigh in neighbour:
            if dimensions[neigh] == '#':
                active += 1

        if dimensions[(x, y, z, w)] == '#':
            if active == 2 or active == 3:
                new_dimension[(x, y, z, w)] = '#'
            else:
                new_dimension[(x, y, z, w)] = '.'
        else:
            if active == 3:
                new_dimension[(x, y, z, w)] = '#'
            else:
                new_dimension[(x, y, z, w)] = '.'

    # print(dimensions)
    # print(new_dimension)
    dimensions = new_dimension

active = 0
for dimen in dimensions.values():
    if dimen == '#':
        active +=1

print(active)