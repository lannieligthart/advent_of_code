import AoC_tools.aoc_tools as aoc

data = aoc.read_input("input.txt", sep1="\n")

def extract(line):
    line = line.split(" ")
    pos = list(map(int, line[2].replace(":", "").split(","))) # col, row
    dim = list(map(int, line[3].split("x"))) # cols, rows
    #print(pos, dim)
    # add all positions to a list
    positions = []
    col = pos[0]
    row = pos[1]
    # columns to cover
    for c in range(col, pos[0] + dim[0]):
        for r in range(row, pos[1] + dim[1]):
            positions.append((c, r))
    return list(set(positions))

claims = [extract(line) for line in data]

aoc.lprint(claims)

import itertools

common_positions = set()

for combi in itertools.combinations(claims, 2):
    common = set(combi[0]).intersection(set(combi[1]))
    for x in common:
        common_positions.add(x)

assert len(common_positions) == 97218





