import collections

file = open('16.txt')

identifiers = collections.defaultdict(list)
my_ticket = list()
nearby_tickets = list()

your_ticket_done = False
for line in file.readlines():
    stripped = line.strip()

    if not stripped:
        continue

    splitted = stripped.split(":")

    if len(splitted) < 2:
        if not your_ticket_done:
            my_ticket = [int(val) for val in splitted[0].split(",") if val]
            your_ticket_done = True
        else:
            nearby_tickets.append([int(val) for val in splitted[0].split(",") if val])
        continue

    if splitted[1]:
        # Identifier
        or_range = splitted[1].split(' or ')

        for s in or_range:
            hypen = s.split("-")
            identifiers[splitted[0]].append((int(hypen[0]), int(hypen[1])))


# print("Input:")
# print(identifiers)
# print(my_ticket)
# print(nearby_tickets)

def invalid_value(ticket):
    for value in ticket:
        if value == 0:
            return -1

        matching_keys = 0
        for key, lis_range in identifiers.items():
            for ran in lis_range:
                if ran[0] <= value <= ran[1]:
                    matching_keys += 1

        if matching_keys == 0:
            return value

    return 0

# Part 1
invalid_rate = 0
valid_tickets = []
for ticket in nearby_tickets:
    val = invalid_value(ticket)
    # print(val)
    invalid_rate += val

    if val == 0:
        valid_tickets.append(ticket)

print("Part 1:{}".format(invalid_rate))


def valid_keys(value_set, oset):
    original_set = oset
    for value in value_set:

        matching_keys = set()
        for key, lis_range in identifiers.items():
            for ran in lis_range:
                if ran[0] <= value <= ran[1]:
                    matching_keys.add(key)
                    break

        original_set = original_set & matching_keys

    return original_set

# Part 2
ticket_row_keys = ['' for i in range(len(my_ticket))]
possible_values = list()


for index in range(len(my_ticket)):

    value_set = [my_ticket[index]]
    value_set.extend([val[index] for val in valid_tickets])

    possible_set = valid_keys(value_set, set(identifiers.keys()))

    possible_values.append(possible_set)

is_changes = True
while is_changes:
    is_changes = False
    for index in range(len(possible_values)):
        sets = possible_values[index]
        if len(sets) == 0:
            continue

        if len(sets) == 1:
            ticket_row_keys[index] = sets.pop()

            for each in possible_values:
                if ticket_row_keys[index] in each:
                    each.remove(ticket_row_keys[index])
            is_changes = True

        else:
            continue

prod_val = 1
for index in range(len(my_ticket)):
    if 'departure' in ticket_row_keys[index]:
        prod_val *= my_ticket[index]

print("Part 2:{}".format(prod_val))