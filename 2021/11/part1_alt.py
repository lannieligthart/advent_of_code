import AoC_tools.aoc_tools as aoc

octopi = aoc.lines2lol("testinput.txt", numeric=True)

with open('input.txt') as f:
    data = f.read().splitlines()

grid = [[int(x) for x in line] for line in data]
print(grid)
