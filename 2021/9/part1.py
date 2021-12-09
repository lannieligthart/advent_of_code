import AoC_tools.aoc_tools as aoc

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

sum = 0

for p in grid.positions:
    val = grid.positions[p]
    point = Point(p, grid.positions[p])
    print("Point:")
    point_value = point.value
    neighbour_values = []
    print("neighbours:")
    try:
        neighbour_S = Point(point.S, grid.positions[point.S])
        print("South: ", neighbour_S)
        neighbour_values.append(neighbour_S.value)
    except KeyError as e:
        pass
    try:
        neighbour_E = Point(point.E, grid.positions[point.E])
        print("East: ", neighbour_E)
        neighbour_values.append(neighbour_E.value)
    except KeyError as e:
        pass
    try:
        neighbour_N = Point(point.N, grid.positions[point.N])
        print("North: ", neighbour_N)
        neighbour_values.append(neighbour_N.value)
    except KeyError as e:
        pass
    try:
        neighbour_W = Point(point.W, grid.positions[point.W])
        print("West: ", neighbour_W)
        neighbour_values.append(neighbour_W.value)
    except KeyError as e:
        pass
    if all(value > point_value for value in neighbour_values):
        sum += point.value + 1

print(sum)
assert sum == 530