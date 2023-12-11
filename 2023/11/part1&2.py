import itertools


def get_empty_rows(data):
    empty_rows = []
    for i, d in enumerate(data):
        if not "#" in d:
            empty_rows.append(i)
    return empty_rows


def get_empty_cols(data):
    empty_cols = []
    for c in range(len(data[0])):
        empty = True
        for r in range(len(data)):
            if data[r][c] == "#":
                empty = False
                break
        if empty:
            empty_cols.append(c)
    return empty_cols


def manhattan(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])


def expand(galaxy, empty_rows, empty_cols, factor):
    gr_old, gc_old = galaxy
    gr_new, gc_new = galaxy
    for c in empty_cols:
        if c < gc_old:
            gc_new += (factor - 1)
    for r in empty_rows:
        if r < gr_old:
            gr_new += (factor - 1)
    return (gr_new, gc_new)


with open("input.txt") as file:
    data = file.read().split("\n")

galaxies = []
for r in range(len(data)):
    for c in range(len(data[r])):
        if data[r][c] == "#":
            galaxies.append((r,c))

empty_cols = get_empty_cols(data)
empty_rows = get_empty_rows(data)


# part 1
new_galaxies1 = [expand(g, empty_rows, empty_cols, 2) for g in galaxies]
combos = list(itertools.combinations(new_galaxies1, 2))
total = sum([manhattan(c[0], c[1]) for c in combos])
assert total == 9403026


# part 2
new_galaxies2 = [expand(g, empty_rows, empty_cols, 1000000) for g in galaxies]
combos = list(itertools.combinations(new_galaxies2, 2))
total = sum([manhattan(c[0], c[1]) for c in combos])
assert total == 543018317006
