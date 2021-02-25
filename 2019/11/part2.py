import sys
sys.path.append("C:/Users/Admin/Documents/Code/advent_of_code/2019/5")
import IntCode as ic

code = ic.parse_code('C:/Users/Admin/Documents/Code/advent_of_code/2019/11/input.txt')
prog = ic.Intcode(code)

# intcode input:
# provide 0 if the robot is over a black panel or 1 if the robot is over a white panel.
# output1:
# 0 means to paint the panel black, and 1 means to paint the panel white.
# output2:
# 0 means it should turn left 90 degrees, and 1 means it should turn right 90 degrees.
# robot turns and moves forward 1 panel.

# if panel == black, input should be 0, if white, input = 1.

#you need to know the number of panels it paints at least once, regardless of color.


class Panel(object):

    def __init__(self, pos, colour='black'):
        self.colour = colour
        self.pos = pos


    def __str__(self):
        return self.colour

class Robot(object):

    orientations = ['N', 'S', 'E', 'W']

    def __init__(self):
        self.orientation = 0
        self.x = 0
        self.y = 0
        # add start panel to covered panels list
        self.covered = {self.pos: Panel(self.pos, colour='white')}

    @property
    def pos(self):
        return (self.x, self.y)

    def turn(self, clockwise):
        if clockwise:
            self.orientation = (self.orientation + 1) % 4
        else:
            self.orientation = (self.orientation - 1) % 4
        # move forward 1 spot
        if self.orientation == 0:
            self.y += 1
        elif self.orientation == 1:
            self.x += 1
        elif self.orientation == 2:
            self.y -= 1
        elif self.orientation == 3:
            self.x -= 1
        # if panel was not covered before, initiate it as black
        if (self.x, self.y) not in self.covered:
            new_panel = Panel((self.x, self.y), colour='black')
            self.covered[(self.x, self.y)] = new_panel

    def __str__(self):
        return f"""
Position: {self.pos}
Orientation: {self.orientations[self.orientation]}
Panels covered: {len(self.covered)}
"""

    def run(self, prog):
        while True:
            if self.covered[self.pos].colour == 'black':
                output1 = prog.run(0, reset=False)
                output2 = prog.run(0, reset=False)

            else:
                output1 = prog.run(1, reset=False)
                output2 = prog.run(1, reset=False)

            # output1:
            # 0 means to paint the panel black, and 1 means to paint the panel white.
            # output2:
            # 0 means it should turn left 90 degrees, and 1 means it should turn right 90 degrees.
            # robot turns and moves forward 1 panel.
            if output1 == 0:
                self.covered[self.pos].colour = 'black'
                print("painted panel black")
            elif output1 == 1:
                self.covered[self.pos].colour = 'white'
                print("painted panel white")
            elif output1 is None:
                return

            if output2 == 0:
                self.turn(clockwise=False)
                print("turned counterclockwise")
            elif output2 == 1:
                self.turn(clockwise=True)
                print("turned clockwise")
            elif output2 is None:
                return
            print("output:", output1, output2)
            print(self)


bot = Robot()
print(bot)

bot.run(prog)

positions = bot.covered.keys()
x_range = [p[0] for p in positions]
y_range = [p[1] for p in positions]

print(min(x_range), max(x_range))
print(min(y_range), max(y_range))

dim_x = max(x_range) + abs(min(x_range))
dim_y = max(y_range) + abs(min(y_range))
print(dim_x, dim_y)


cols = [i for i in range(min(x_range), max(x_range)+1)]
index = [i for i in range(max(y_range), min(y_range)-1, -1)]

print(cols)
print(index)

import pandas as pd
#
grid = pd.DataFrame(columns=cols, index=index)
for col in grid.columns:
    grid[col].values[:] = ' '


for p in positions:
    if bot.covered[p].colour == 'black':
        grid.loc[p[1], p[0]] = ' '
    elif bot.covered[p].colour == 'white':
        grid.loc[p[1], p[0]] = '#'


lol = grid.values.tolist()
for l in lol:
    print("".join(l))