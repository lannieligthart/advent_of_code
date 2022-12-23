from AoC_tools.aoc22 import *
from collections import deque

def get_neighbours(point, grid):
    nb_n = grid.get_neighbours(point=point, n=8, direction="N")
    nb_e = grid.get_neighbours(point=point, n=8, direction="E")
    nb_s = grid.get_neighbours(point=point, n=8, direction="S")
    nb_w = grid.get_neighbours(point=point, n=8, direction="W")
    nb_n = [n for n in nb_n if grid.values[n.pos] == '#']
    nb_e = [n for n in nb_e if grid.values[n.pos] == '#']
    nb_s = [n for n in nb_s if grid.values[n.pos] == '#']
    nb_w = [n for n in nb_w if grid.values[n.pos] == '#']
    return [nb_n, nb_e, nb_s, nb_w]

def propose(point, grid, prio):
    nb_n, nb_e, nb_s, nb_w = nb = get_neighbours(point, grid)
    # start with the first priority direction
    for direction in prio:
        # find the number of neighbours in that direction
        # only if there are any, return them. otherwise, proceed to the next direction.
        len_nb = [len(n) for n in nb]
        # if none of the directions produce any result, None will be returned.
        if max(len_nb) == 0:
            return None
        if direction == "N" and len(nb_n) == 0:
            return point.N.pos
        elif direction == "S" and len(nb_s) == 0:
            return point.S.pos
        elif direction == "E" and len(nb_e) == 0:
            return point.E.pos
        elif direction == "W" and len(nb_w) == 0:
            return point.W.pos

def get_elves(grid):
    elves = []
    for point in grid.points.values():
        if grid.values[point.pos] == "#":
            elves.append(point)
    return elves

data = read_input("input.txt")
data = [list(d) for d in data]
grid = Grid.read(data, nosep=True)

prio = deque(["N", "S", "W", "E"])

def move(grid):
    proposals = dict()
    elves = get_elves(grid)
    for elf in elves:
        proposals[elf.pos] = propose(elf, grid, prio)

    # check which proposals are unique
    count = {}
    for prop in proposals.values():
        if prop in count:
            count[prop] += 1
        else:
            count[prop] = 1

    unique_proposals = [prop for prop in proposals.values() if count[prop] == 1]

    # move elves
    for key, value in proposals.items():
        if value in unique_proposals:
            grid.remove(key)
            grid.add(key, value=".")
            grid.add(value)

    # adjust priorities
    first = prio.popleft()
    prio.append(first)
    return grid.values.values()

round = 1
values = move(grid)

for _ in range(9):
    round += 1
    previous_values = values
    values = move(grid)

elves = get_elves(grid)
elf_positions = [elf.pos for elf in elves]
x_range = [pos[0] for pos in elf_positions]
y_range = [pos[1] for pos in elf_positions]
x_min, x_max = min(x_range), max(x_range)
y_min, y_max = min(y_range), max(y_range)

smaller_grid = dict()

for key, value in grid.values.items():
    if x_min <= key[0] <= x_max and y_min <= key[1] <= y_max:
        smaller_grid[key] = value

small_grid = Grid.from_dict(smaller_grid)

# add values for points that don't have any (outside the range of the original grid)
for x in range(small_grid.x_min, small_grid.x_max + 1):
    for y in range(small_grid.y_min, small_grid.y_max + 1):
        if (x, y) not in small_grid.values.keys():
            small_grid.add((x, y), value=".")

empty_spots = 0
for key, value in small_grid.values.items():
    if value == "." or value == " ":
        empty_spots += 1

assert empty_spots == 4241

