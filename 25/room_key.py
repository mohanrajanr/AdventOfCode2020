# Test Numbers: 5764801, 17807724
# Actu Numbers: 12232269, 19452773
expected_data = [12232269, 19452773]

subject_num = 7


def transform(public_key, loop):
    print("Transforming:{} {}".format(public_key, loop))
    index = 1
    value = 1
    while index <= loop:
        value *= public_key
        value = value % 20201227
        index += 1
    return value


def get_loopsize(expected):
    loopsize = 1
    value = 1
    while True:
        value *= subject_num
        value = value % 20201227

        print(value)

        if value == expected:
            break
        loopsize += 1
    return loopsize

card_size = get_loopsize(expected_data[0])
door_size = get_loopsize(expected_data[1])

print(transform(expected_data[1], card_size))
print(transform(expected_data[0], door_size))

print("Done")