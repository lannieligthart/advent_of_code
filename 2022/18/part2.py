
from AoC_tools.aoc22 import read_input, start, end

class Cube(object):

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"""Position: ({self.x}, {self.y}, {self.z})"""

    @property
    def pos(self):
        return (self.x, self.y, self.z)

    def get_neigbours(self):
        nb = [(self.x + 1, self.y, self.z), (self.x - 1, self.y, self.z),
                (self.x, self.y + 1, self.z), (self.x, self.y - 1, self.z),
                (self.x, self.y, self.z + 1), (self.x, self.y, self.z - 1)]
        return nb

def get_outside_space(droplet):
    # bepaal minimale en maximale x, y en z voor de droplet
    all_x = [cube[0] for cube in droplet]
    all_y = [cube[1] for cube in droplet]
    all_z = [cube[2] for cube in droplet]

    # neem ranges met een extra marge er omheen
    x_range = range(min(all_x) - 1, max(all_x) + 2)
    y_range = range(min(all_y) - 1, max(all_y) + 2)
    z_range = range(min(all_z) - 1, max(all_z) + 2)

    start = (x_range[0], y_range[0], z_range[0])
    outside_space = set()
    selected = [start]
    while True:
        old_len = len(outside_space)
        new_cubes = set()
        for s in selected:
            c = Cube(*s)
            nb = c.get_neigbours()
            # bewaar alleen de neighbours die binnen het gedefinieerde gebied vallen en niet bij de droplet horen
            nb = [n for n in nb if n[0] in x_range and n[1] in y_range and n[2] in z_range and n not in droplet]
            # voeg deze aan de outside space toe
            for n in nb:
                new_cubes.add(n)
                outside_space.add(n)
        selected = new_cubes
        new_len = len(outside_space)
        if old_len == new_len:
            return outside_space

s = start()

data = read_input("input.txt", "\n", ",")
data = [list(map(int, d)) for d in data]

droplet = []
for d in data:
    droplet.append(tuple(d))

outside_space = get_outside_space(droplet)

# loop nu door alle punten van de droplet en check of er neighbours in outside_space zitten.
# zo ja, dan is het een external surface.
external_surface = 0

for pos in droplet:
    cube = Cube(*pos)
    nb = cube.get_neigbours()
    for n in nb:
        if n in outside_space:
            external_surface += 1

print(external_surface)
#assert external_surface == 2000

end = end(s)


# Visualize layers of the droplet
# all_x = [d[0] for d in droplet]
#
# for x in range(min(all_x), max(all_x)+1):
#     points = [Point(p[1], p[2]) for p in droplet if p[0] == x]
#     grid = Grid.from_list(points)
#     #grid.display()