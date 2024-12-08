from AoC_tools import aoc24 as aoc
import itertools

s = aoc.start()
infile = "testinput.txt"
infile = "input.txt"

with open(infile) as f:
    data = f.read().split("\n")

data = [list(d) for d in data]

def find_antinodes(pos1:tuple, pos2:tuple, nrows:int, ncols:int):
    r1, c1 = pos1
    r2, c2 = pos2
    dr, dc = (r1-r2, c1-c2)
    antinodes = []
    r, c = (r1 + dr, c1 + dc)
    if 0 <= r < nrows and 0 <= c < ncols:
        antinodes.append((r, c))
    r, c = (r2 - dr, c2 - dc)
    if 0 <= r < nrows and 0 <= c < ncols:
        antinodes.append((r, c))
    return antinodes

def find_all_antennas_of_a_type(data, char):
    """takes a type of antenna and returns all their positions"""
    positions = []
    for r in range(len(data)):
        for c in range(len(data[0])):
            if data[r][c] == char:
                positions.append((r,c))
    return positions

def find_all_types_of_antenna(data):
    types = set()
    for r in range(len(data)):
        for c in range(len(data[0])):
            if data[r][c] != ".":
                types.add(data[r][c])
    return types

# find all types of antennas on the grid

antinodes = set()
types = find_all_types_of_antenna(data)

for t in types:
    # get positions
    positions = find_all_antennas_of_a_type(data, t)
    # get all possible pairs
    pairs = list(itertools.combinations(positions, 2))
    # for all pairs, add antinodes
    ant_list = []
    for p in pairs:
        ant_list.extend(find_antinodes(p[0], p[1], nrows=len(data), ncols=len(data[0])))
    for a in ant_list:
        antinodes.add(a)

result = len(antinodes)

aoc.check_result(infile, result, 14, 341, s)
