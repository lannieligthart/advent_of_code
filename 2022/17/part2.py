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

    def __str__(self):
        return f"""Left: {self.left}\nRight: {self.right}\nTop: {self.top}\nBottom: {self.bottom}"""

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
        self.next_move = self.data[self.idx]
        self.grid = aoc.Grid()
        self.rocks = 0
        self.moves_down = []
        self.increments = []

    def drop_shape(self, shape):
        moves_down = 0
        while True:
            direction = self.data[self.idx]
            if direction == ">":
                shape.move_right()
            elif direction == "<":
                shape.move_left()
            self.idx += 1
            self.idx = self.idx % len(data)
            # if the new location doesn't fit, reset position
            if not shape.check_fit(self.grid):
                if direction == ">":
                    shape.move_left()
                elif direction == "<":
                    shape.move_right()
            shape.move_down()
            moves_down += 1
            # if the shape can't move down, move back up and fix it on the grid
            if not shape.check_fit(self.grid):
                shape.move_up()
                moves_down -= 1
                self.grid.add_points(shape.points)
                self.moves_down.append(moves_down)
                return

data = aoc.read_input("input.txt")[0]
game = Game(data)

# we need to find 3 periods:
# N shapes (5)
# directions (40 for test, 10091 for real input)
# increments in height (1400 for test, 1735 for real input)

#period1 = 5
#period2 = len(data)

def run(game, n):
    # increments = [0]
    # height = 0
    old_height = 0
    for round in range(0, n):
        rock_type = round % 5
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
        # old_height = height
        # height = game.grid.y_max + 1
        # increment = height - old_height
        # increments.append(increment)
        if round % 1735 == 0:
            game.increments.append(game.grid.y_max - old_height)
            old_height = game.grid.y_max
        elif round % (1735*2 + 140) == 0: # 140 is offset at the end; use round 140 after the first fully completed cycle to determine the increment
            game.remainder_increment = game.grid.y_max - old_height
    print(game.moves_down)
    #print(game.increments)

run(game, 7000)
# use downward moves to identify when the periods of falling figures and grid shape come together.
# 19 moves down is a pretty rare but recurring event which shows a period where in cycles of 3, the 19 is preceded by 3, 3, 5.
# every 3rd time the 19 occurs is therefore a period in the downward moves.
indices = []
for i in range(len(game.moves_down)):
    if game.moves_down[i] == 19:
        indices.append(i)
for i in range(len(indices)-3):
    print(indices[i+3] - indices[i])
period3 = indices[3] - indices[0]

#print(period1, period2, period3)

# how much height is added in each period of 1735?
print(game.increments)
height_per_period = game.increments[-1]
assert height_per_period == 2667

# the offset is the height added in the first, incomplete cycle.
offset = game.increments[1] - game.increments[2]

# total rocks to be dropped
n_rocks = 1000000000000

# floor divide n_rocks by 1735
n_cycles = n_rocks // period3
remainder = n_rocks % period3

result = n_cycles * height_per_period + offset + game.remainder_increment
print(result)
assert result == 1537175792495

# 1537175792495= (576368876 * 2667) + 203
# 203 is 217 - 14
# -14 is offset at the beginning
# 217 is the offset at the end (i.e. height gained during the remainder of n_rocks % period3)