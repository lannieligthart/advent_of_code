
from AoC_tools.aoc22 import read_input

class Cube(object):

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_neigbours(self, points):
        potential_nb = [Cube(self.x + 1, self.y, self.z), Cube(self.x - 1, self.y, self.z),
                        Cube(self.x, self.y + 1, self.z), Cube(self.x, self.y - 1, self.z),
                        Cube(self.x, self.y, self.z + 1), Cube(self.x, self.y, self.z - 1)]
        nb = []
        for p in points:
            for n in potential_nb:
                if n.x == p.x and n.y == p.y and n.z == p.z:
                    nb.append(n)
        return nb

data = read_input("input.txt", "\n", ",")
data = [list(map(int, d)) for d in data]

droplet = []
for d in data:
    droplet.append(Cube(*d))

exposed_sides = 0

for point in droplet:
    exposed_sides += 6 - len(point.get_neigbours(droplet))

assert exposed_sides == 3530
