
file = open('9.txt')

values = list()
for line in file.readlines():
    values.append(int(line.strip()))

# Part 1
preamble = 25
difflist = values[:preamble]
diff_set = set(difflist)

missing_val = 0
for index in range(preamble, len(values)):
    val = values[index]
    print("Processing:{}".format(val))

    found_val = False
    for i2 in diff_set:
        if val - i2 != i2 and val - i2 in diff_set:
            print("{} is present".format(val-i2))
            diff_set.add(val)
            difflist.append(val)
            diff_set.remove(difflist.pop(0))
            found_val = True
            break

    if not found_val:
        print(val)
        missing_val = val
        break

# Part 2
# We already have missing_val, diffset and difflist for our help.
i, j = 0, 1
sum = values[i]
while i < j:
    if sum + values[j] < missing_val:
        sum += values[j]
        j += 1
    elif sum + values[j] > missing_val:
        sum -= values[i]
        i += 1
    else:
        print(max(values[i:j+1]) + min(values[i:j+1]))
        break
