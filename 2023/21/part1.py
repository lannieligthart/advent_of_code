from AoC_tools import aoc23 as aoc
from AoC_tools import aoc22 as aoc22
import functools

start = aoc22.start()

with open("input.txt") as file:
    data = file.read()

grid = aoc.Matrix.read(data)
for key, value in grid.values.items():
    if value == 'S':
        start_pos = key
grid.pos = (start_pos)

@functools.cache
def get_nb(pos):
    r, c = pos
    result = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
    return [r for r in result if r in grid.values.keys()]

points = [(start_pos)]
new_nb = set()
rounds = 64
for i in range(rounds):
    nb = []
    while len(points) > 0:
        nb.extend(get_nb(points.pop()))
    for n in nb:
        if grid.values[n] != "#":
            new_nb.add(n)
    points = new_nb
    if i == rounds - 1:
        result = len(new_nb)
    new_nb = set()

assert result == 3748

end = aoc22.end(start)