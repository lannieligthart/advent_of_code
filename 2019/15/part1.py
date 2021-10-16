import sys
sys.path.append("C:/Users/Admin/SURFdrive/Code/advent_of_code/2019/15")
sys.path.append("C:/Users/Admin/SURFdrive/Code/advent_of_code/AoC_tools")
import IntCode as ic
from aoc_tools import display_grid

code = ic.parse_code('C:/Users/Admin/SURFdrive/Code/advent_of_code/2019/15/input.txt')
software = ic.Intcode(code)



class RepairDroid(object):

    def __init__(self, software, position=[0, 0]):
        self.position = position
        self.map = {(0,0): "D"}
        self.software = software
        self.previous_position = None
        self.orientation = "N" # start with north facing orientation.

    def move(self, direction):
        # take input
        # run IntCode
        # return new position (same or different depending on IntCode response)
        print("Facing", self.orientation)
        output = self.software.run(input=direction, halt_on_output=True, reset=False)
        # if the droid can move, move it.
        if output == 1 or output == 2:
            self.map[tuple(self.position)] = "."
            self.previous_position = self.position
            # north
            if direction == 1:
                self.position[1] += 1
                self.orientation = "N"
                print("moving north, new position:", self.position)
            # west
            elif direction == 2:
                self.position[0] -= 1
                self.orientation = "W"
                print("moving west, new position:", self.position)
            # south
            elif direction == 3:
                self.position[1] -= 1
                self.orientation = "S"
                print("moving south, new position:", self.position)
            # east
            elif direction == 4:
                self.position[0] += 1
                self.orientation = "E"
                print("moving east, new position:", self.position)
            self.map[tuple(self.position)] = "D"
        # if it can't move, don't move but add the info to the map.
        elif output == 0:
            pos_to_add = self.get_destination(direction)
            self.map[tuple(pos_to_add)] = "#"
        # if the oxygen system has been found, return its position, otherwise None.
        if output == 2:
            print("Found the Oxygen system at position " + self.position + "!")
        return output

    def get_destination(self, direction):
        # north
        if direction == 1:
            dest = self.position.copy()
            dest[1] += 1
        # west
        elif direction == 2:
            dest = self.position.copy()
            dest[0] -= 1
        # south
        elif direction == 3:
            dest = self.position.copy()
            dest[1] -= 1
        # east
        elif direction == 4:
            dest = self.position.copy()
            dest[0] += 1
        return tuple(dest)

    def scan_and_move(self):
        # order of directions
        order_of_directions = [1, 2, 3, 4]
        # which one we try first depends on orientation. We go straight, then right, etc.
        if self.orientation == "N":
            directions = order_of_directions
        elif self.orientation == "W":
            directions = [2, 3, 4, 1]
        elif self.orientation == "S":
            directions = [3, 4, 1, 2]
        elif self.orientation == "E":
            directions = [4, 1, 2, 3]
        attempt = 0
        for d in directions:
            attempt += 1
            cur_pos = self.position.copy()
            # determine destination and only try it if we haven't been there before, or if we've already
            # tried all other options.
            new_pos = self.get_destination(d)
            if new_pos not in self.map and attempt <= 4:
                output = droid.move(d)
                # if output == 0 (can't go there), continue.
                # if output == 1 or output == 2 (moved), exit loop prematurely because we need to start a new scan.
                if output == 1 or output == 2:
                    return output
            elif attempt == 5:
                new_pos = self.previous_position
                self.previous_position = self.position
                self.position = new_pos
                return 0




droid = RepairDroid(software)
output = None

while not output == 2:
    output = droid.scan_and_move()
    print(droid.position)
    lookup = {"#": "#",
              ".": ".",
              "D": "D"}
    display_grid(droid.map, lookup)

# algoritme schrijven voor het zoeken naar de oxygen system.
# check welke zijden al bekend zijn, probeer te bewegen naar de eerstvolgende zijde die nog niet bekend is.
# ga altijd eerst linksaf, tenzij je daar al geweest bent. Dan de eerstvolgende (clockwise).
