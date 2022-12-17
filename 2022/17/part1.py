import AoC_tools.aoc22 as aoc
from AoC_tools.aoc22 import Point

class Shape(object):

    def __init__(self, points, left, bottom):
        self.points = points
        self.left = left
        self.bottom = bottom

    @property
    def right(self):
        x_list = [p.x for p in self.points]
        return max(x_list)

    @property
    def top(self):
        y_list = [p.y for p in self.points]
        return max(y_list)

    def move_left(self):
        self.left -= 1
        self.points = [Point(p.x - 1, p.y) for p in self.points]

    def move_right(self):
        self.left += 1
        self.points = [Point(p.x + 1, p.y) for p in self.points]

    def move_down(self):
        self.bottom -= 1
        self.points = [Point(p.x, p.y - 1) for p in self.points]

    def move_up(self):
        self.bottom += 1
        self.points = [Point(p.x, p.y + 1) for p in self.points]

    def check_fit(self, grid):
        fit = True
        if self.right > 6 or self.left < 0 or self.bottom < 0:
            fit = False
        # if all the above criteria are met, check that the positions of the points are not yet occupied
        else:
            for p in self.points:
                # als het punt al bestaat past het niet
                if p.pos in grid.points.keys():
                    fit = False
        return fit

def minus(l, b):
    points = [Point(l, b), Point(l + 1, b), Point(l + 2, b), Point(l + 3, b)]
    return Shape(points, l, b)

def plus(l, b):
    points = [Point(l, b + 1), Point(l + 1, b), Point(l + 1, b + 1), Point(l + 1, b + 2), Point(l + 2, b + 1)]
    return Shape(points, l, b)

def lshape(l, b):
    points = [Point(l, b), Point(l + 1, b), Point(l + 2, b), Point(l + 2, b + 1), Point(l + 2, b + 2)]
    return Shape(points, l, b)

def pipe(l, b):
    points = [Point(l, b), Point(l, b + 1), Point(l, b + 2), Point(l, b + 3)]
    return Shape(points, l, b)

def square(l, b):
    points = [Point(l, b), Point(l + 1, b), Point(l, b + 1), Point(l + 1, b + 1)]
    return Shape(points, l, b)


class Game(object):

    def __init__(self, data):
        self.data = data
        self.idx = 0
        self.grid = aoc.Grid()
        self.rocks = 0

    def drop_shape(self, shape):
        while True:
            direction = self.data[self.idx]
            if direction == ">":
                shape.move_right()
            elif direction == "<":
                shape.move_left()
            self.idx += 1
            if self.idx > len(data):
                print("resetting pattern")
            self.idx = self.idx % len(data)

            # if the new location doesn't fit, reset position
            if not shape.check_fit(self.grid):
                if direction == ">":
                    shape.move_left()
                elif direction == "<":
                    shape.move_right()
            shape.move_down()
            # if the shape can't move down, move back up and fix it on the grid
            if not shape.check_fit(self.grid):
                shape.move_up()
                self.grid.add_points(shape.points)
                return

data = aoc.read_input("input.txt")[0]
game = Game(data)

for rock in range(0, 2022):
    rock_type = rock % 5
    if rock_type == 0:
        try:
            shape = minus(2, game.grid.y_max + 4)
        except ValueError:
            shape = minus(2, 3)
    elif rock_type == 1:
        shape = plus(2, game.grid.y_max + 4)
    elif rock_type == 2:
        shape = lshape(2, game.grid.y_max + 4)
    elif rock_type == 3:
        shape = pipe(2, game.grid.y_max + 4)
    elif rock_type == 4:
        shape = square(2, game.grid.y_max + 4)
    game.drop_shape(shape)

print(game.grid.y_max + 1)

assert game.grid.y_max + 1 == 3106

