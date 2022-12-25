from AoC_tools.aoc22 import *


class Blizzard(object):

    def __init__(self, direction, x, y):
        self.direction = direction
        self.x = x
        self.y = y

    def __str__(self):
        return (f"Direction: {self.direction}, Position: {(self.x, self.y)}")

    def find_pos(self, i):
        if self.direction == ">":
            return (self.x + i) % (x_max + 1), self.y
        elif self.direction == "<":
            return (self.x - i) % (x_max + 1), self.y
        elif self.direction == "^":
            return self.x, (self.y - i) % (y_max + 1)
        elif self.direction == "v":
            return self.x, (self.y + i) % (y_max + 1)

def get_blizzard_state(minute, blizzards, x_max, y_max):
    """returns the positions of all blizzards at a specified time point"""
    blizzard_state = dict()
    for x in range(x_max + 1):
        for y in range(y_max + 1):
            blizzard_state[(x, y)] = "."
    for b in blizzards:
        blizzard_state[b.find_pos(minute)] = b.direction
    return blizzard_state

def get_options(point, blizzard_state, x_max, y_max):
    """determines where expedition can go depending on the state of the blizzards at that time"""
    directions = [point, point.N, point.S, point.E, point.W]
    nb = []
    for p in directions:
        if x_min <= p.x <= x_max and y_min <= p.y <= y_max and blizzard_state[p.pos] not in [">", "v", "<", "^"]:
            nb.append(p)
    return nb

def get_shortest_path(blizzard_data):
    # start position
    e_pos = (0, -1)
    # position just before end
    goal = (x_max, y_max)
    # first option available is start position
    positions = set([e_pos])
    i = 1
    while True:
        if i % 50 == 0:
            print(i)
        # get current state of the blizzards
        bd = get_blizzard_state(i, blizzard_data, x_max, y_max)
        # we collect the new options in a set so we don't duplicate anything
        new_positions = set()
        # to be able to display, make a grid with the current blizzard situation (optional)
        #current_grid = Grid.from_dict(bd)
        #current_grid.display()
        # for the current options:
        for pos in positions:
            if pos == goal:
                print(f"reached goal in {i} minutes")
                return i
            # for this option, investigate which options there are
            options = get_options(Point(*pos), bd, x_max, y_max)
            # als er wel opties zijn, voeg deze allemaal toe als nieuwe posities
            for o in options:
                new_positions.add(o.pos)
                #current_grid.add_points(list(new_positions), "E")
            if len(options) == 0 and pos == (0, -1):
                new_positions = [pos]
        print(f"in minute {i}, optional positions are {new_positions}")
        # if i % 50 == 0:
        #current_grid.display()
        positions = new_positions
        i += 1


data = read_input("input.txt")
data = data[1:-1]
# data = [list(d.replace("#", "")) for d in data]
# grid = Grid.read(data)
# grid.display()

y_min, y_max = grid.y_min, grid.y_max
x_min, x_max = grid.x_min, grid.x_max

# bepaal beginposities van de blizzards
blizzard_data = []
for key, value in grid.values.items():
    if value in [">", "v", "<", "^"]:
        blizzard_data.append(Blizzard(value, *key))

result = get_shortest_path(blizzard_data)
assert result == 255

