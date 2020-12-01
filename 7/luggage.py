import collections

file = open('7.txt')

baggage = collections.defaultdict(dict)

for line in file.readlines():
    stripped = line.strip()

    contain_split = stripped.split('contain')

    input_key = contain_split[0].replace('bags', '').strip()

    input_vals = contain_split[1].split(',')

    for val in input_vals:
        val_stripped = val.strip()
        amount = val_stripped[0]
        name = val_stripped[1:].replace('bags', '').replace('bag', '').replace('.', '').strip()

        if name == 'o other':
            continue

        baggage[input_key][name] = int(amount)

# print(baggage)

# Part 1
available_bags = 0
input_bags = ['shiny gold']
already_processed = ['shiny_gold']
while input_bags:
    bag = input_bags.pop()
    for key, name_d in baggage.items():
        if bag in name_d.keys() and key not in already_processed:
            available_bags += 1
            input_bags.append(key)
            already_processed.append(key)

print(available_bags)

memoized = dict()
def find_num_bags(bag_name):
    if bag_name in memoized:
        return memoized[bag_name]

    if bag_name not in baggage:
        memoized[bag_name] = 1
        return 1

    total_val = 1
    for name, count in baggage[bag_name].items():
        total_val += find_num_bags(name) * int(count)
    memoized[bag_name] = total_val
    return total_val


print(find_num_bags('shiny gold') - 1)
