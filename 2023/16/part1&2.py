from collections import deque

with open("input.txt") as file:
    data = file.read().split("\n")

class Path(object):

    def __init__(self, drc, row, col, data):
        self.new_start_points = []
        self.row = row
        self.col = col
        self.drc = drc
        self.data = data

    @property
    def tile(self):
        return self.data[self.row][self.col]

    def update_dir(self):
        """depending on direction and content of the tile encountered, determine what the new direction should be.
        If one direction, just update
        If split, set direction to none and set new paths to follow."""
        turns = {"R": (["R"], ["U", "D"], ["R"], ["D"], ["U"]),
                "L": (["L"], ["D", "U"], ["L"], ["U"], ["D"]),
                "U": (["U"], ["U"], ["L", "R"], ["L"], ["R"]),
                "D": (["D"], ["D"], ["L", "R"], ["R"], ["L"])}
        tiles = [".", "|", "-", "\\", "/"]
        drc = turns[self.drc][tiles.index(self.tile)]
        if len(drc) == 1:
            self.drc = drc[0]
        elif len(drc) > 1:
            self.drc = None
            self.new_start_points = [(drc[i], self.row, self.col) for i in range(len(drc))]

    def move(self):
        r, c = self.row, self.col
        if self.drc == "U":
            r = self.row - 1
        elif self.drc == "D":
            r = self.row + 1
        elif self.drc == "L":
            c = self.col - 1
        elif self.drc == "R":
            c = self.col + 1
        # check if we're still on the grid.
        if r >= 0 and c >= 0 and r < len(self.data[0]) and c < len(self.data):
            self.row = r
            self.col = c
            self.update_dir()
        else:
            self.drc = None


def first_turn(drc, tile):
    turns = {"R": (["R"], ["U", "D"], ["R"], ["D"], ["U"]),
             "L": (["L"], ["U", "D"], ["L"], ["U"], ["D"]),
             "U": (["U"], ["U"], ["L", "R"], ["L"], ["R"]),
             "D": (["D"], ["D"], ["L", "R"], ["R"], ["L"])}
    tiles = [".", "|", "-","\\","/"]
    if drc == "D":
        new_drc = turns["D"][tiles.index(tile)]
    if drc == "U":
        new_drc = turns["U"][tiles.index(tile)]
    if drc == "R":
        new_drc = turns["R"][tiles.index(tile)]
    if drc == "L":
        new_drc = turns["L"][tiles.index(tile)]
    return new_drc


def run(start_point):
    p = Path(*start_point, data)
    while p.drc is not None:
        points[(p.row, p.col)] = "#"
        p.move()
    return p.new_start_points

def try_start_point(drc, row, col):
    start_dir = first_turn(drc, data[row][col])
    start_points = deque()
    for sdrc in start_dir:
        start_points.append((sdrc, row, col))
    tried = set()
    tried.add(start_points[0])
    while len(start_points) > 0:
        s = start_points.popleft()
        new_sp = run(s)
        for s in new_sp:
            if s not in tried:
                start_points.append(s)
                tried.add(s)
    return len(points)


start_points = []
c_max = len(data)
r_max = len(data[0])

# rows left and right
for i in range(len(data)):
    start_points.append(("R", i, 0))
for i in range(len(data)):
    start_points.append(("L", i, c_max - 1))
# top
for i in range(len(data)):
    start_points.append(("D", 0, i))
for i in range(len(data)):
    start_points.append(("L", r_max - 1, i))

# part 1
start_point = ("R", 0, 0)
points = dict()
result = try_start_point(*start_point)
assert result == 7199

# part 2
totals = []
for s in start_points:
    points = dict()
    totals.append(try_start_point(*s))

assert max(totals) == 7438