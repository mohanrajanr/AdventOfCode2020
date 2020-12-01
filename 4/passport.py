
file = open('4.txt')

input_passports = list()

pass_string = ''
for line in file.readlines():
    stripped = line.strip()

    if not stripped:
        input_passports.append(pass_string)
        pass_string = ''
        continue

    pass_string += " {}".format(stripped)

# last passport
input_passports.append(pass_string)

valid_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']

# Part 1
valid_pass = 0
for passport in input_passports:
    splits = passport.split(' ')

    validity = {key: False for key in valid_fields}

    for key_value in splits:

        if not key_value.strip():
            continue

        key, value = key_value.split(":")

        validity[key] = True

    is_applicable = True
    for key, applicable in validity.items():

        if key == 'cid':
            continue

        if not applicable:
            is_applicable = False
            break

    if is_applicable:
        valid_pass += 1

print(valid_pass)

# Part 2
def validate_byr(value_given):
    if 1920 <= int(value_given) <= 2002:
        return True
    return False


def validate_iyr(value_given):
    if 2010 <= int(value_given) <= 2020:
        return True
    return False


def validate_eyr(value_given):
    if 2020 <= int(value_given) <= 2030:
        return True
    return False


def validate_hgt(value_given):
    hght = value_given[-2:]

    if hght == 'cm' and 150 <= int(value_given[:-2]) <= 193:
        return True
    elif hght == 'in' and 59 <= int(value_given[:-2]) <= 76:
        return True

    return False


def validate_hcl(value_given):
    if len(value_given) != 7:
        return False
    if value_given[0] != '#':
        return False

    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    aplha = ['a', 'b', 'c', 'd', 'e', 'f']
    num_alpha = nums + aplha
    for ind in range(1, len(value_given)):
        if value_given[ind] not in num_alpha:
            return False

    return True


def validate_ecl(value_given):
    valid_vals = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if value_given not in valid_vals:
        return False
    return True


def validate_pid(value_given):
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    if len(value_given) != 9:
        return False

    for v in value_given:
        if v not in nums:
            return False

    return True


valid_pass = 0
for passport in input_passports:
    splits = passport.split(' ')

    validity = {key: False for key in valid_fields}

    for key_value in splits:

        if not key_value.strip():
            continue

        key, value = key_value.split(":")

        if key == 'cid':
            continue

        # Call respective Validator
        if locals()['validate_{}'.format(key)](value):
            validity[key] = True

    is_applicable = True
    for key, applicable in validity.items():

        if key == 'cid':
            continue

        if not applicable:
            is_applicable = False
            break

    if is_applicable:
        valid_pass += 1

print(valid_pass)