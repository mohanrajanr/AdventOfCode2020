from collections import Counter

file = open('6.txt')

converter = {'F': '0', 'B': '1', 'L': '0', 'R': '1'}

input_lines = []
st = []
for line in file.readlines():
    stripped = line.strip()

    if not stripped:
        input_lines.append(st)
        st = []
    else:
        st.append(stripped)

input_lines.append(st)

print(input_lines)

# Part 1
max_c = 0
for li in input_lines:
    tot = []
    for word in li:
        tot += word

    c = Counter(tot)
    print(c)
    max_c += len(c.keys())

print(max_c)

# Part 2
max_c = 0
for li in input_lines:
    tot = []
    for word in li:
        tot += word

    c = Counter(tot)
    len_l = len(li)

    for k, v in c.items():
        if v >= len_l:
            max_c += 1

print(max_c)
