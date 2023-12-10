import re
from math import lcm

with open("input.txt") as file:
    data = file.read()

directions, map = data.split("\n\n")

network = dict()
for m in map.split("\n"):
    m = re.sub(r"[\(\),=]", "", m).split()
    network[m[0]] = (m[1], m[2])

def move(current, d):
    if d == 'L':
        return network[current][0]
    elif d == 'R':
        return network[current][1]

def find_first_z(current, directions):
    while True:
        for d in directions:
            current = move(current, d)
            if current.endswith("Z"):
                first_z = current
                return first_z

def find_cycle(current, directions):
    n = 0
    numbers = []
    # find the first occurrence of Z and record the node name
    first_z = find_first_z(current, directions)
    # for a few cycles of getting back to first_z, record how many steps it took to get there.
    # looks like one cycle is actually enough to get the right number so we can use the first two ns to get the cycle.
    while len(numbers) < 2:
        for d in directions:
            n += 1
            current = move(current, d)
            if current == first_z:
                numbers.append(n)
    return numbers[1] - numbers[0]

# start nodes are all the ones that end in A
start_nodes = [key for key in network.keys() if key.endswith("A")]

cycles = []
for node in start_nodes:
    cycles.append(find_cycle(node, directions))

# find the least common multiple for the list of cycles
result = lcm(*cycles)

assert result == 14935034899483