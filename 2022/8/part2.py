from AoC_tools import aoc22 as aoc

def get_viewing_distances(point):
    neighbours = grid.nb_4dir(point)
    distances = []
    for direction in neighbours:
        dist = 0
        for nb in direction:
            if grid.values[nb.pos] < grid.values[point.pos]:
                dist += 1
            elif grid.values[nb.pos] >= grid.values[point.pos]:
                dist += 1
                break
        distances.append(dist)
    result = distances[0] * distances[1] * distances[2] * distances[3]
    return result


start_time = aoc.start()

data = aoc.read_input("input.txt")
data = list(map(list, data))

grid = aoc.Grid.read(data)
grid.display()

visible = 0
invisible = 0

vd = [get_viewing_distances(p) for p in grid.points.values()]
assert max(vd) == 335580

aoc.end(start_time)