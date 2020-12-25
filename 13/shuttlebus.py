import math
file = open('13.txt')

# earliest_time = int(file.readline())
# bus_ids = [int(val.strip()) for val in file.readline().split(',') if val != 'x']
#
# print(earliest_time)
# print(bus_ids)
#
# # Part 1
# min_val = float('inf')
# min_num = -1
# for bid in bus_ids:
#     val = math.ceil(earliest_time/bid) * bid
#     if val < min_val:
#         min_num = bid
#         min_val = val
# print(min_num)
# print((min_val - earliest_time) * min_num)


# Part 2
_ = int(file.readline())
bus_id_offset = [(index, int(val.strip())) for (index, val) in enumerate(file.readline().split(',')) if val != 'x']

print(bus_id_offset)

# max_val = max([x[0] for x in bus_id_offset])
# init_timestamp = [x[1] for x in bus_id_offset if x[0] == max_val][0]
# timestamp = max_val
#
# while True:
#
#     all_match = True
#     for (bid, offset) in bus_id_offset:
#
#         if bid == max_val:
#             continue
#
#         if ((timestamp - offset) % bid) != 0:
#             all_match = False
#
#     if all_match:
#         print(timestamp)
#         break
#
#     timestamp += max_val

# min_val = [x[0] for x in bus_id_offset if x[1] == 0][0]
# timestamp = math.floor(100000000000000 / min_val) * min_val
#
# while True:
#
#     all_match = True
#     for (bid, offset) in bus_id_offset:
#
#         if ((timestamp + offset) % bid) != 0:
#             all_match = False
#
#     if all_match:
#         print(timestamp)
#         break
#
#     timestamp += min_val
#     print(timestamp)
#
# print(timestamp)

# max_val = max([x[0] for x in bus_id_offset])
# val_offset = [x[1] for x in bus_id_offset if x[0] == max_val][0]
# timestamp = math.floor(100785425009517 / max_val) * max_val
#
# offset_diff = [(x[0], x[1] - val_offset) for x in bus_id_offset]
# offset_diff.sort(key=lambda x: x[0], reverse=True)
# try:
#     while True:
#
#         all_match = True
#         for (bid, offset) in offset_diff:
#
#             if bid == max_val:
#                 continue
#
#             if ((timestamp + offset) % bid) != 0:
#                 all_match = False
#                 break
#
#         if all_match:
#             # print(timestamp)
#             break
#
#         timestamp += max_val
#         # print(timestamp)
# except KeyboardInterrupt:
#     print(timestamp)
#     print("ERROR")
#
# print(timestamp - val_offset)




# CRT Method
# def mod_inverse(a, n):
#     a = a % n
#
#     for x in range(1, n):
#         if (a*x) % n == 1:
#             return x
# N_val = 1
# for b in bus_id_offset:
#     N_val *= b[1]
#
# timestamp = 0
# for (bi, ni) in bus_id_offset:
#
#     Ni = (N_val//ni)
#
#     xi = mod_inverse(Ni, ni)
#
#     timestamp += bi * Ni * xi
#
# print(timestamp % N_val)

# def euclid(a, b):
#     if b == 0:
#         return a, 1, 0
#     d, y, x = euclid(b, a % b)
#     return d, x, y - (a // b) * x
#
# def gcd(a, b):
#     d, _, _ = euclid(a, b)
#     return d
#
# def crt(p1, p2):
#     a, m = p1
#     b, n = p2
#     if a < 0 or b < 0:
#         return (-1, -1)
#
#     d = gcd(m, n)
#     if (a - b) % d != 0:
#         return (-1, -1)
#
#     g, x, y = euclid(m // d, n // d)
#     l = (a - b) // d
#     ret_mod = m // d * n
#     l %= ret_mod
#     ret = b + n * l * y
#     ret %= ret_mod
#
#     return (ret, ret_mod)
#
# ans = bus_id_offset[0]
# for ind, bi in bus_id_offset[1:]:
#     ans = crt(ans, (ind, bi))
#
# print(ans)

start_time = 0
step = 1
while bus_id_offset:
  start_time += step

  # See if any new busses align with this timestamp.
  newfound = [b for (k, b) in bus_id_offset if not (start_time + k) % b]
  if newfound:
    newfound = newfound[0]
    # Remove the bus from the unfound bus list and update the step
    # so future iterations would include this bus, too.
    bus_id_offset = [(a, b) for a, b in bus_id_offset if b != newfound]
    step *= newfound
else:
  print(start_time)
