from AoC_tools import aoc22 as aoc
from collections import Counter

with open("input.txt") as file:
    data = file.read().split("\n")
    data = [tuple(map(int, d.split(", "))) for d in data]

x = [d[0] for d in data]
y = [d[1] for d in data]

data = {(d): i for i, d in enumerate(data)}
grid = aoc.Grid.from_dict(data)
grid.display()

x_range = (min(x), max(x))
y_range = (min(y), max(y))

def manhattan(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def get_closest(pos, coordinates):
    # for a position on the map, return the coordinate closest to it, if there is a single one. Otherwise, return None.
    distances = dict()
    for c in coordinates:
        distances[c] = (manhattan(pos, c))
    # get the smallest distance observed
    lowest = min(distances.values())
    # count how many times each distance was observed
    counts = Counter(distances.values())
    if counts[lowest] == 1:
        closest = min(distances, key=distances.get)
        return data[closest]
    elif counts[lowest] > 1:
        return "."

# take a bit of a margin just in case
margin = 5
# for each point on the defined grid, store the coordinate it is closest to (if a single one, otherwise None).
closest = dict()

for x in range(x_range[0] - margin, x_range[1] + margin):
    for y in range(y_range[0] - margin, y_range[1] + margin):
        # get the coordinate closest to it.
        closest[(x,y)] = get_closest((x, y), data)

grid2 = aoc.Grid.from_dict(closest)
#grid2.display()

# determine which coordinates do not have a match on the outer edges of the grid. Those are not infinite.
x_min = min([pos[0] for pos in closest.keys()])
x_max = max([pos[0] for pos in closest.keys()])
y_min = min([pos[1] for pos in closest.keys()])
y_max = max([pos[1] for pos in closest.keys()])

margins = []
for key, value in grid2.values.items():
    if (key[0] == x_min or key[0] == x_max) or (key[1] == y_min or key[1] == y_max):
        margins.append(value)

finite = set()
for key, value in data.items():
    if value not in margins:
        finite.add(value)

# count how many positions fall withing the finite areas.
finite_items = [value for key, value in closest.items() if value in finite]
counts = dict()
for value in list(finite):
    counts[value] = finite_items.count(value)

assert max(counts.values()) == 3276
