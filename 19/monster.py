import collections

file = open('19.txt')

# rules = dict()
# possible_rules = collections.defaultdict(list)
# messages = list()
#
# rules_finished = False
# for line in file.readlines():
#     stripped = line.strip()
#
#     if not stripped:
#         rules_finished = True
#         continue
#
#     if rules_finished:
#         messages.append(stripped)
#
#     else:
#         colon = stripped.split(":")
#
#         if '"' in colon[1]:
#             stripp = colon[1].replace('"', '').strip()
#             # possible_rules[int(colon[0].strip())].append(stripp)
#             rules[int(colon[0].strip())] = stripp
#             continue
#
#         pipe = colon[1].split("|")
#         rules[int(colon[0].strip())] = []
#         for e_p in pipe:
#             splitted = [int(var) for var in e_p.split(" ") if var != '']
#             rules[int(colon[0].strip())].append(splitted)
#
# print(rules)
# print(possible_rules)

# # Part 1
# def find_possibles(index, mega_list):
#     if index in possible_rules:
#         return possible_rules[index]
#
#     combinations = []
#     for sub_list in mega_list:
#
#         poss_stack = ['']
#         new_stack = []
#         for value in sub_list:
#
#             value_possibles = find_possibles(value, rules[value])
#
#             # print("Val:{} Pos:{}".format(value, value_possibles))
#
#             while len(poss_stack):
#                 strin = poss_stack.pop()
#                 for poss in value_possibles:
#                     new_stack.append(str(strin+poss))
#
#             poss_stack = new_stack
#             new_stack = []
#
#             # print("Val:{} Stack:{}".format(value, poss_stack))
#         combinations.extend(poss_stack)
#
#     possible_rules[index] = combinations
#     return combinations
#
#
# possible_rules[0] = find_possibles(0, rules[0])
#
# valid_mess = 0
# for mess in messages:
#     if mess in possible_rules[0]:
#         valid_mess +=1
#
# print(valid_mess)

# Part 2 - Match Ruler

# def match_rule(expr, stack):
#     if len(stack) > len(expr):
#         return False
#     elif len(stack) == 0 or len(expr) == 0:
#         return len(stack) == 0 and len(expr) == 0
#
#     c = stack.pop()
#     if isinstance(c, str):
#         if expr[0] == c:
#             return match_rule(expr[1:], stack.copy())
#     else:
#         for rule in rules[c]:
#             if match_rule(expr, stack + list(reversed(rule))):
#                 return True
#     return False
#
# def count_messages(rules, messages):
#     total = 0
#     for message in messages:
#         if match_rule(message, list(reversed(rules[0][0]))):
#             total += 1
#     return total

def match(string, stack):
    if len(stack) > len(string):
        return False
    elif len(stack) == 0 or len(string) == 0:
        return len(stack) == 0 and len(string) == 0

    c = stack.pop()
    if isinstance(c, str):
        if string[0] == c:
            return match(string[1:], stack.copy())
    else:
        for rule in rules[c]:
            if match(string, stack + list(reversed(rule))):
                return True
    return False


def valid_messages():
    total = 0
    for message in messages:
        if match(message, list(reversed(rules[0][0]))):
            total += 1
    return total


with open('19.txt') as file:
    rules_raw, messages = tuple(map(lambda x: x.splitlines(), file.read().split('\n\n')))

rules = {}
for rule_raw in rules_raw:
    num, contents = rule_raw.split(': ')
    if contents[0] == '"':
        rules[int(num)] = contents[1]
    else:
        rules[int(num)] = list(map(lambda x: list(map(int, x.split(' '))), contents.split(' | ')))

print("Part 1:", valid_messages())
rules[8] = [[42], [42, 8]]
rules[11] = [[42, 31], [42, 11, 31]]
print("Part 2:", valid_messages())