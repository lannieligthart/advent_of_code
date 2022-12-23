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
        if direction == "N" and len(nb_n) == 0: # and grid.includes(point.N):
            return point.N.pos
        elif direction == "S" and len(nb_s) == 0: # and grid.includes(point.S):
            return point.S.pos
        elif direction == "E" and len(nb_e) == 0: # and grid.includes(point.E):
            return point.E.pos
        elif direction == "W" and len(nb_w) == 0: # and grid.includes(point.W):
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

    for key, value in proposals.items():
        if value in unique_proposals:
            grid.remove(key)
            grid.add(key, value=".")
            grid.add(value)

    first = prio.popleft()
    prio.append(first)
    return grid.values

round = 1
positions = move(grid)

while True:
    round += 1
    if round % 100 == 0:
        print(round)
    previous_positions = positions.copy()
    positions = move(grid)
    if positions == previous_positions:
        break

assert round == 1079