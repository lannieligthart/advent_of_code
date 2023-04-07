import AoC_tools.aoc_tools as aoc

data = aoc.read_input("input.txt", "\n")

n = 0
for line in data:
    x = int(line)
    n += x

assert n == 490
