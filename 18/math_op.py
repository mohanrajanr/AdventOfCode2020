file = open('18.txt')

expressions = list()

for line in file.readlines():
    expressions.append(list(line.strip()))

print(expressions)

# Part 1
# def process_stack(stack):
#     print("Stack:{}".format(stack))
#     init = int(stack[0])
#
#     index = 1
#     while index < len(stack) - 1:
#         op = stack[index]
#         val = stack[index+1]
#
#         if op == '+':
#             init += int(val)
#         else:
#             init *= int(val)
#
#         index += 2
#     return init
#
# def process_express(express_list):
#
#     clean_list = [char for char in express_list if char != ' ']
#     print("Going to Process:{}".format(clean_list))
#
#     index = 0
#     occur = -1
#     start_exp = list()
#     stack = []
#     while index < len(clean_list):
#         char = clean_list[index]
#         index += 1
#
#         if char == '(':
#             start_exp.append(list())
#             occur += 1
#             continue
#
#         if char == ')':
#             sub_list = start_exp.pop()
#             occur -= 1
#             val = process_express(sub_list)
#
#             if not start_exp:
#                 stack.append(val)
#             else:
#                 start_exp[occur].append(val)
#             continue
#
#         if not start_exp:
#             stack.append(char)
#         else:
#             start_exp[occur].append(char)
#
#     return_val = process_stack(stack)
#     print("Processed:{} ST:{} {}".format(clean_list, stack, return_val))
#     return return_val
#
#
# total_value = 0
# for express in expressions:
#     total_value += process_express(express)
#
# print(total_value)


# Part 2
def process_stack2(stack):
    print("Stack:{}".format(stack))

    init = int(stack[0])
    index = 1
    mul_stack = []
    while index < len(stack) - 1:
        op = stack[index]
        val = int(stack[index+1])

        if op == '+':
            init += val
        else:
            mul_stack.append(init)
            mul_stack.append(op)
            init = val

        index += 2

    mul_stack.append(init)
    print(mul_stack)

    init2 = int(mul_stack[0])
    index = 1
    while index < len(mul_stack) - 1:
        op = mul_stack[index]
        val = int(mul_stack[index + 1])
        init2 *= val
        index += 2

    return init2


def process_express2(express_list):

    clean_list = [char for char in express_list if char != ' ']
    print("Going to Process:{}".format(clean_list))

    index = 0
    occur = -1
    start_exp = list()
    stack = []
    while index < len(clean_list):
        char = clean_list[index]
        index += 1

        if char == '(':
            start_exp.append(list())
            occur += 1
            continue

        if char == ')':
            sub_list = start_exp.pop()
            occur -= 1
            val = process_express2(sub_list)

            if not start_exp:
                stack.append(val)
            else:
                start_exp[occur].append(val)
            continue

        if not start_exp:
            stack.append(char)
        else:
            start_exp[occur].append(char)

    return_val = process_stack2(stack)
    print("Processed:{} ST:{} {}".format(clean_list, stack, return_val))
    return return_val


total_value = 0
for express in expressions:
    total_value += process_express2(express)

print(total_value)
