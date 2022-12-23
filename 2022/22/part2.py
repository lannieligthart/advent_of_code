from AoC_tools.aoc22 import read_input, Grid

class Side(object):

    def __init__(self, name, grid):
        self.name = name
        self.grid = grid
        self.N = None
        self.E = None
        self.S = None
        self.W = None

class Cube(object):

    def __init__(self, sides):
        self.facing = None
        self.position = None
        self.sides = sides
        self.side = self.sides[1]
        self.facings = [">", "v", "<", "^"]

    @property
    def pos(self):
        offsets = {1: (50, 0),
                   2: (0, 150),
                   3: (0, 100),
                   4: (50, 50),
                   5: (50, 100),
                   6: (100, 0)}
        x, y = self.position
        return x + offsets[self.side.name][0], y + offsets[self.side.name][1]

    def turn(self, direction):
        """takes a direction and a facing and returns the new facing"""
        if direction == "R":
            self.facing = (self.facing + 1) % 4
        elif direction == "L":
            self.facing = (self.facing - 1) % 4

    def transform(self, c, r, dir1, dir2):
        dim = self.side.grid.y_max
        if dir1 == "N" and dir2 == "N":
            c = dim - c
            r = 0
            self.turn("R")
            self.turn("R")
        elif dir1 == "S" and dir2 == "S":
            c = dim - c
            r = dim
            self.turn("R")
            self.turn("R")
        elif dir1 == "E" and dir2 == "E":
            c = dim
            r = dim - r
            self.turn("R")
            self.turn("R")
        elif dir1 == "W" and dir2 == "S":
            c = dim - r
            r = dim
            self.turn("R")
        elif dir1 == "E" and dir2 == "N":
            c = dim - r
            r = 0
            self.turn("R")
        elif dir1 == "E" and dir2 == "S":
            c = r
            r = dim
            self.turn("L")
        elif dir1 == "S" and dir2 == "W":
            r = dim - c
            c = 0
            self.turn("L")
        elif dir1 == "N" and dir2 == "E":
            r = dim - c
            c = dim
            self.turn("L")
        elif dir1 == "W" and dir2 == "N":
            c = r
            r = 0
            self.turn("L")
        elif dir1 == "N" and dir2 == "W":
            r = c
            c = 0
            self.turn("R")
        elif dir1 == "S" and dir2 == "E":
            r = c
            c = dim
            self.turn("R")
        elif dir1 == "W" and dir2 == "W":
            c = 0
            r = dim - r
            self.turn("R")
            self.turn("R")
        elif dir1 == "S" and dir2 == "N":
            c = c
            r = 0
        elif dir1 == "N" and dir2 == "S":
            c = c
            r = dim
        elif dir1 == "E" and dir2 == "W":
            r = r
            c = 0
        elif dir1 == "W" and dir2 == "E":
            r = r
            c = dim
        else:
            print(dir1, dir2, "not covered")
        return c, r


    def step(self):
        c, r = self.position
        old_position = (c, r)
        old_side = self.side
        old_facing = self.facing
        while True:
            # 0 = E, 1 = S, 2 = W, 3 = N
            if self.facing == 0:
                c += 1
            elif self.facing == 2:
                c -= 1
            elif self.facing == 3:
                r -= 1
            elif self.facing == 1:
                r += 1
            # check new position
            # als y nu groter is dan y_max gaan we naar de noorderbuur
            if r > self.side.grid.y_max:
                r = self.side.grid.y_min
                mergeto = self.side.S[1]
                self.side = self.side.S[0]
                c, r = self.transform(c, r, "S", mergeto)
            elif r < self.side.grid.y_min:
                r = self.side.grid.y_max
                mergeto = self.side.N[1]
                self.side = self.side.N[0]
                c, r = self.transform(c, r, "N", mergeto)
            # same for x
            if c > self.side.grid.x_max:
                c = self.side.grid.x_min
                mergeto = self.side.E[1]
                self.side = self.side.E[0]
                c, r = self.transform(c, r, "E", mergeto)
            elif c < self.side.grid.x_min:
                c = self.side.grid.x_max
                mergeto = self.side.W[1]
                self.side = self.side.W[0]
                c, r = self.transform(c, r, "W", mergeto)
            # if current position is not on the map (i.e. value == " "), repeat
            # if it is in on the map, but it's a wall, return old position
            if self.side.grid.values[(c, r)] == "#":
                #print(f"Hit a wall at {(c, r)}, stayed at {old_position}")
                self.side = old_side
                self.facing = old_facing
                return old_position
            # if it's on the map and it's not a wall, return current position
            elif self.side.grid.values[(c, r)] in [".", ">", "^", "<", "v", "X"]:
                self.side.grid.add((c, r), self.facings[self.facing])
                return (c, r)


    def move(self, steps):
        for i in range(steps):
            old_position = self.position
            old_side = self.side
            self.position = self.step()
            if self.position == old_position and self.side == old_side:
                break

# couldn't be bothered with parsing the input so reading in a modified version

data = read_input("input2.txt", "\n\n", strip=False)
instructions = data[6]
data = data[0:6]

sides = dict()

for i, d in enumerate(data):
    sides[i+1] = Side(i+1, Grid.read(d, nosep=True))

sides[1].N = (sides[2], "W")
sides[1].S = (sides[4], "N")
sides[1].E = (sides[6], "W")
sides[1].W = (sides[3], "W")
sides[2].N = (sides[3], "S")
sides[2].S = (sides[6], "N")
sides[2].E = (sides[5], "S")
sides[2].W = (sides[1], "N")
sides[3].N = (sides[4], "W")
sides[3].S = (sides[2], "N")
sides[3].E = (sides[5], "W")
sides[3].W = (sides[1], "W")
sides[4].N = (sides[1], "S")
sides[4].S = (sides[5], "N")
sides[4].E = (sides[6], "S")
sides[4].W = (sides[3], "N")
sides[5].N = (sides[4], "S")
sides[5].S = (sides[2], "E")
sides[5].E = (sides[6], "E")
sides[5].W = (sides[3], "E")
sides[6].N = (sides[2], "S")
sides[6].S = (sides[4], "E")
sides[6].E = (sides[5], "E")
sides[6].W = (sides[1], "E")

route = []
n = ''
for char in instructions:
    if char.isdigit():
        n += char
    else:
        route.append(int(n))
        direction = char
        route.append(char)
        n = ''
route.append(int(n))

# 0 = E, 1 = S, 2 = W, 3 = N

cube = Cube(sides)
cube.facing = 0
cube.position = (data[0].index("."), 0)
cube.side.grid.add(cube.position, "X")

for i, r in enumerate(route):
    if isinstance(r, int):
        cube.move(r)
    elif isinstance(r, str):
        cube.turn(r)
        cube.side.grid.add(cube.position, cube.facings[cube.facing])
    if i % 500 == 0:
        print(i)

final_col = cube.pos[0] + 1
final_row = cube.pos[1] + 1

print(f"side: {cube.side.name}")
print(f"position: {cube.pos}")
print(f"facing: {cube.facing}")

result = final_row * 1000 + final_col * 4 + cube.facing

assert result == 162155