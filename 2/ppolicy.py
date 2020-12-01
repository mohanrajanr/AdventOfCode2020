
# Input
file = open('2.txt')

input_lines = list()
for line in file.readlines():
    word = line.strip()
    splitline = word.split(":")
    input_lines.append((splitline[0], splitline[1]))


# Part 1
valid_pass = 0
for (policy, password) in input_lines:
    spl = policy.split(" ")
    letter = spl[1]
    minc = int(spl[0].split("-")[0])
    maxc = int(spl[0].split("-")[1])

    if minc <= password.count(letter) <= maxc:
        valid_pass += 1

print(valid_pass)


# Part q2
valid_pass = 0
for (policy, password) in input_lines:
    spl = policy.split(" ")
    letter = spl[1]
    pos1 = int(spl[0].split("-")[0])
    pos2 = int(spl[0].split("-")[1])
    password = password.strip()

    if password[pos1 - 1] == letter and password[pos2 - 1] == letter:
        pass
    elif password[pos1-1] == letter or password[pos2-1] == letter:
        print("{} {} {}".format(password[pos1-1], password[pos2-1], letter))
        valid_pass += 1

print(valid_pass)
