import AoC_tools.aoc_tools as aoc
import itertools
import functools

data = aoc.read_input("input.txt", sep1="\n")
aoc.lprint(data)

def extract(line):
    line = line.split(" ")
    pos = list(map(int, line[2].replace(":", "").split(","))) # col, row
    dim = list(map(int, line[3].split("x"))) # cols, rows
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

all_pos = functools.reduce(lambda a, b: set(a).union(set(b)), claims)

claims_left = claims.copy()

for combi in itertools.combinations(claims, 2):
    common = set(combi[0]).intersection(set(combi[1]))
    if len(list(common)) > 0:
        try:
            claims_left.remove(combi[0])
        except ValueError:
            pass
        try:
            claims_left.remove(combi[1])
        except ValueError:
            pass

for c in range(len(claims)):
    if claims[c] == claims_left[0]:
        result = c + 1
        break

assert result == 717


