import AoC_tools.aoc_tools as aoc
import math

data = aoc.lines2list("input.txt")
for i in range(len(data)):
    data[i] = list(data[i])
print(data)

grid = aoc.Grid.make(data)
grid.display()

class Point():

    def __init__(self, pos, value):
        self.x = pos[0]
        self.y = pos[1]
        self.value = int(value)

    def __str__(self):
        return f"({self.x}, {self.y}): {self.value}"

    @property
    def position(self):
        return (self.x, self.y)

    @property
    def N(self):
        return (self.x - 1, self.y)

    @property
    def S(self):
        return (self.x + 1, self.y)

    @property
    def W(self):
        return (self.x, self.y - 1)

    @property
    def E(self):
        return (self.x, self.y + 1)

    def get_neighbours(self, grid):
        neighbours = []
        #print("neighbours:")
        try:
            neighbour_S = Point(self.S, grid.positions[self.S])
            #print("South: ", neighbour_S)
            neighbours.append(neighbour_S)
        except KeyError as e:
            pass
        try:
            neighbour_E = Point(self.E, grid.positions[self.E])
            #print("East: ", neighbour_E)
            neighbours.append(neighbour_E)
        except KeyError as e:
            pass
        try:
            neighbour_N = Point(self.N, grid.positions[self.N])
            #print("North: ", neighbour_N)
            neighbours.append(neighbour_N)
        except KeyError as e:
            pass
        try:
            neighbour_W = Point(self.W, grid.positions[self.W])
            #print("West: ", neighbour_W)
            neighbours.append(neighbour_W)
        except KeyError as e:
            pass
        return neighbours

total = 0
low_points = []

for p in grid.positions:
    val = grid.positions[p]
    point = Point(p, grid.positions[p])
    point_value = point.value
    nb = point.get_neighbours(grid)
    neighbour_values = [n.value for n in nb]
    if all(value > point_value for value in neighbour_values):
        total += point.value + 1
        low_points.append(point)


#print(total)
#assert total == 530
aoc.lprint(low_points)

def define_basin(low_point):
    basin = []
    checked = []

    # add low point to basin
    basin.append(low_point.position)

    while len(basin) > len(checked):
        for pos in basin:
            if pos not in checked:
                point = Point(pos, grid.positions[pos])
                #print("Checking point" + str(point))
                nb = point.get_neighbours()
                for n in nb:
                    if n.value < 9 and n.position not in basin:
                        basin.append(n.position)
                checked.append(pos)
    print("basin: ", basin)
    return basin


basins = []
basin_lengths = []
for lp in low_points:
    print("getting basin for low point", lp.position)
    basin = define_basin(lp)
    basin_lengths.append(len(basin))

basin_lengths.sort()
basin_lengths = basin_lengths[-3:]

answer = math.prod(basin_lengths)

assert answer == 1019494


