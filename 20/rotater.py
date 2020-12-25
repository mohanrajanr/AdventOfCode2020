import enum
class enumVal(enum.Enum):
    I = '#'
    O = '.'


# org_array = [['.', '.', '#', '#', '.', '#', '.', '.', '#', '.'], ['#', '#', '.', '.', '#', '.', '.', '.', '.', '.'], ['#', '.', '.', '.', '#', '#', '.', '.', '#', '.'], ['#', '#', '#', '#', '.', '#', '.', '.', '.', '#'], ['#', '#', '.', '#', '#', '.', '#', '#', '#', '.'], ['#', '#', '.', '.', '.', '#', '.', '#', '#', '#'], ['.', '#', '.', '#', '.', '#', '.', '.', '#', '#'], ['.', '.', '#', '.', '.', '.', '.', '#', '.', '.'], ['#', '#', '#', '.', '.', '.', '#', '.', '#', '.'], ['.', '.', '#', '#', '#', '.', '.', '#', '#', '#']]
# array = [[enumVal(val).name for val in i] for i in org_array]

array = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

for arr in array:
    print(arr)


def rotate_array_right(array):
    rotated_array = []

    for index in range(len(array)):
        rotated_array.append([arr[index] for arr in array])

    return rotated_array[::-1]
#
# print("\n")
#
# for arr in rotate_array_right(array):
#     print(arr)

def flip_array_bottom(array):
    return array[::-1]

# print("\n")
#
# for arr in flip_array_bottom(array):
#     print(arr)


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

print("Possib:\n")