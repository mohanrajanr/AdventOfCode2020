# Test Data: 389125467
# Actu Data: 156794823
import sys

sys.stdout = open('output.txt', 'w')

cup_order = 156794823


class Node(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

# Part 1
# def prepare_circular_list():
#     h = Node(-1)
#     rotateNode = h
#     l = 0
#
#     for data in list(str(cup_order)):
#         rotateNode.next = Node(int(data))
#         rotateNode = rotateNode.next
#         l += 1
#
#     rotateNode.next = h.next
#     h = h.next
#
#     print("Circular List Done:")
#     print_nodes(h, l)
#     return h, l
#
#
# def print_nodes(start_node, l):
#     rotateNode = start_node
#
#     i = 0
#     while i < l:
#         print(rotateNode.val, end=" ")
#         rotateNode = rotateNode.next
#         i += 1
#     print("\n")
#
#
# def get_node_link(start_node, expected_val, l):
#     rotate_node = Node(-1)
#     rotate_node.next = start_node
#
#     ind = 0
#     while rotate_node.next:
#         if rotate_node.next.val == expected_val:
#             return rotate_node.next
#
#         if ind == l:
#             print("Val Not Found:{}".format(expected_val))
#             print_nodes(start_node, l)
#             return None
#
#         ind += 1
#         rotate_node = rotate_node.next
#
#
# def get_highest_node(start_node, l):
#     rotate_node = start_node
#     max_val = float('-inf')
#     i = 0
#     while i < l:
#         max_val = max(max_val, rotate_node.val)
#         rotate_node = rotate_node.next
#         i += 1
#     return max_val
#
# head, length = prepare_circular_list()
#
#
# def move_cups():
#
#     curr_val = head.val
#     rotater = head.next
#
#     pickups = []
#     for i in range(3):
#         pickups.append(rotater.val)
#         rotater = rotater.next
#
#     head.next = rotater
#
#     print("Picked Up:{}".format(pickups))
#
#     check_val = curr_val - 1
#     node_link = None
#     while not node_link:
#         if check_val <= 0:
#             check_val = get_highest_node(head, length)
#             node_link = get_node_link(head, check_val, length)
#         else:
#             if check_val in pickups:
#                 check_val -= 1
#             else:
#                 node_link = get_node_link(head, check_val, length)
#
#     print("Next Val:{}".format(check_val))
#
#     next_link = node_link.next
#     while len(pickups):
#         p_val = pickups.pop()
#         next_link = Node(p_val, next_link)
#
#     node_link.next = next_link
#
#     print("Curr Nodes:", end="")
#     print_nodes(head, length)
#
# index = 0
# while index < 100:
#     print("Move Cups:{}".format(index+1))
#     move_cups()
#     head = head.next
#     index += 1
#

# Part 2
max_l = 1000000
max_node_val = 0
node_location = dict()


def prepare_circular_list():
    h = Node(-1)
    rotateNode = h
    l = 0

    global max_node_val

    for data in list(str(cup_order)):
        node_location[int(data)] = Node(int(data))
        rotateNode.next = node_location[int(data)]
        rotateNode = rotateNode.next
        max_node_val = max(max_node_val, int(data))
        l += 1

    while l < max_l:
        node_location[int(max_node_val+1)] = Node(int(max_node_val+1))
        rotateNode.next = node_location[int(max_node_val+1)]
        rotateNode = rotateNode.next
        max_node_val += 1
        l += 1

    rotateNode.next = h.next
    h = h.next

    print("Circular List Done:")
    # print_nodes(h, l)
    return h, l


def print_nodes(start_node, l):
    rotateNode = start_node

    i = 0
    while i < l:
        print(rotateNode.val, end=" ")
        rotateNode = rotateNode.next
        i += 1
    print("\n")


head, length = prepare_circular_list()


def move_cups():

    curr_val = head.val
    rotater = head.next

    pickups = []
    for i in range(3):
        pickups.append(rotater.val)
        rotater = rotater.next

    head.next = rotater

    # print("Picked Up:{}".format(pickups))

    check_val = curr_val - 1
    node_link = None

    while not node_link:
        while check_val in pickups or check_val == 0:
            if not check_val:
                check_val = max_node_val
            else:
                check_val -= 1

        node_link = node_location[check_val]

    # print("Next Val:{}".format(check_val))

    next_link = node_link.next
    while len(pickups):
        p_val = pickups.pop()
        node_location[p_val] = Node(p_val, next_link)
        next_link = node_location[p_val]

    node_link.next = next_link

    # print("Curr Nodes:", end="")
    # print_nodes(head, length)

index = 0
while index < 10000000:
    print("Move Cups:{}".format(index+1))
    move_cups()
    head = head.next
    index += 1

# print_nodes(node_location[1], length)

node_link = node_location[1]
next_cup = node_link.next.val
next_next_cup = node_link.next.next.val
value = next_cup * next_next_cup
print("Cup:{} {} Value:{}".format(next_cup, next_next_cup, value))
