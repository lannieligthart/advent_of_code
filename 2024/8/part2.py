from AoC_tools import aoc24 as aoc
import itertools

s = aoc.start()
infile = "testinput.txt"
infile = "input.txt"

with open(infile) as f:
    data = f.read().split("\n")

data = [list(d) for d in data]

def find_antinodes(pos1:tuple, pos2:tuple, nrows:int, ncols:int):
    # determine deltas
    dr, dc = (pos1[0]-pos2[0], pos1[1]-pos2[1])
    antinodes = []
    # I'll just scan an arbitrary range that is undoubtedly enough to cover the whole grid.
    # Taking one of the positions as the starting point is sufficient as we need to include
    # the antennas themselves too.
    for x in range(-100, 100):
        r, c = (pos1[0] + x*dr, pos1[1] + x*dc)
        if 0 <= r < nrows and 0 <= c < ncols:
            antinodes.append((r,c))
    antinodes = list(set(antinodes))
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
    ant_list = set(ant_list)
    for a in ant_list:
        antinodes.add(a)

result = len(antinodes)

aoc.check_result(infile, result, 34, 1134, s)
