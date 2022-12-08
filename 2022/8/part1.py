from AoC_tools import aoc22 as aoc

def is_visible(point):
    # all neighbours in at least one direction should be lower in order for the tree to be visible
    any_visible = False
    neighbours = grid.nb_4dir(point)
    for direction in neighbours:
        all_lower = True
        for nb in direction:
            if grid.values[nb.pos] >= grid.values[point.pos]:
                all_lower = False
        if all_lower:
            any_visible = True
    return any_visible

start_time = aoc.start()
data = aoc.read_input("input.txt")
data = list(map(list, data))

grid = aoc.Grid.read(data)

visible = 0
invisible = 0

for point in grid.points.values():
    if point.x == 0 or point.x == grid.x_max:
        visible += 1
    elif point.y == 0 or point.y == grid.y_max:
        visible += 1
    else:
        if is_visible(point):
            visible += 1

assert visible == 1827

aoc.end(start_time)
