import AoC_tools.aoc_tools as aoc

data = aoc.read_input("input.txt", "\n\n", "\n")
data = list(map(sum, map(aoc.s2n, data)))
data.sort()

assert max(data) == 72602
assert sum(data[-3:]) == 207410