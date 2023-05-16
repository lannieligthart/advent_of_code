

class Light(object):

    def __init__(self):
        self.state = 0

    def turn_on(self):
        self.state += 1

    def turn_off(self):
        self.state -= 1
        if self.state < 0:
            self.state = 0

    def toggle(self):
        self.state += 2

    def __str__(self):
        return str(self.state)

def count_on(grid):
    n = 0
    for value in grid.values():
        n += value.state
    return n

with open("input.txt") as file:
    instructions = file.read().split("\n")

grid = dict()

# fill the grid with lights (that by default are off after initialisation)
for r in range(1000):
    for c in range(1000):
        grid[(r, c)] = Light()


for i in instructions:
    # determine start and stop coordinates
    start = i.split()[-3]
    stop = i.split()[-1]
    r1, c1 = start.split(",")
    r2, c2 = stop.split(",")
    # for all lights within this range, run the current instruction
    for row in range(int(r1), int(r2) + 1):
        for col in range(int(c1), int(c2) + 1):
            if i.startswith("turn on"):
                grid[(row, col)].turn_on()
            elif i.startswith("turn off"):
                grid[(row, col)].turn_off()
            elif i.startswith("toggle"):
                grid[(row, col)].toggle()

# count how many lights are on
assert count_on(grid) == 14110788
