import re

with open("input.txt") as file:
    data = file.read()

directions, map = data.split("\n\n")

network = dict()
for m in map.split("\n"):
    m = re.sub(r"[\(\),=]", "", m).split()
    network[m[0]] = (m[1], m[2])

current = 'AAA'

n = 0
while True:
    if current == 'ZZZ':
        print(n)
        break
    for d in directions:
        n += 1
        if d == 'L':
            current = network[current][0]
        elif d == 'R':
            current = network[current][1]

assert n == 15517