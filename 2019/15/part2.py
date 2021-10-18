import sys
sys.path.append("C:/Users/Admin/SURFdrive/Code/advent_of_code/2019/15")
sys.path.append("C:/Users/Admin/SURFdrive/Code/advent_of_code/AoC_tools")
import IntCode as ic
from aoc_tools import display_grid

class RepairDroid(object):

    def __init__(self, software, position=[0, 0]):
        self.position = position
        self.map = {(0,0): "S"}
        self.software = software
        self.route = [(0,0)]
        self.explored = [(0,0)]
        self.oxygen_pos = None
        self.uturn = None
        self.previous_uturn = None
        self.distances = []


    def get_destination(self, direction):
        # north
        if direction == "N":
            dest = self.position.copy()
            dest[1] += 1
        # east
        elif direction == "E":
            dest = self.position.copy()
            dest[0] += 1
        # south
        elif direction == "S":
            dest = self.position.copy()
            dest[1] -= 1
        # west
        elif direction == "W":
            dest = self.position.copy()
            dest[0] -= 1
        return tuple(dest)

    def move(self, direction):
        # take input
        # run IntCode
        # return new position (same or different depending on IntCode response)
        directions = {
            "N": 1,
            "S": 2,
            "W": 3,
            "E": 4
        }
        output = self.software.run(input=directions[direction], halt_on_output=True, reset=False)
        if output == 1 or output == 2:
            # if droid can move, update self.position.
            # Remove 'D' mark from old position.
            if self.map[tuple(self.position)] not in ["S", "O"]:
                self.map[tuple(self.position)] = "."
            # Update current position.
            # north
            if direction == "N":
                self.position[1] += 1
                #print("moving north, new position:", self.position)
            # east
            elif direction == "E":
                self.position[0] += 1
                #print("moving east, new position:", self.position)
            # south
            elif direction == "S":
                self.position[1] -= 1
                #print("moving south, new position:", self.position)
            # west
            elif direction == "W":
                self.position[0] -= 1
                #print("moving west, new position:", self.position)
            # mark new position on the map.
            self.map[tuple(self.position)] = "D"
            if self.position == (0,0):
                return 99
        return output


    def scan_and_move(self):
        # which one we try first depends on orientation. We go straight, then right, etc.
        directions = ["N", "E", "S", "W"]
        for d in directions:
            # determine destination and only check it out if it's unexplored.
            dest = self.get_destination(d)
            if dest not in self.explored and (dest not in self.map or self.map[dest] != "#"):
                output = self.move(direction=d)
                # add collected info to the map.
                # if inaccessible, add a "#"
                if output == 0:
                    self.map[tuple(dest)] = "#"
                elif output == 1:
                    self.route.append(tuple(dest))
                    self.explored.append(tuple(dest))
                    #display_grid(droid.map)
                    return 1
                elif output == 2:
                    self.route.append(tuple(dest))
                    self.map[tuple(dest)] = "O"
                    self.explored.append(tuple(dest))
                    self.oxygen_pos = dest
                    return 2
        # if no new direction to move was found, go back to previous position.
        #print("no options, moving back to previous position!")
        # based on route, figure out which direction to go back to.
        try:
            current_pos = self.route[-1]
            previous_pos = self.route[-2]
        except IndexError:
            return 99
        dif = [0, 0]
        dif[0] = current_pos[0] - previous_pos[0]
        dif[1] = current_pos[1] - previous_pos[1]
        dif_dir = {
            (1,0): "W",
            (-1,0): "E",
            (0,1): "S",
            (0,-1): "N"
        }
        if self.map[tuple(self.position)] not in ["S", "O"]:
            self.map[tuple(self.position)] = "."
        self.move(dif_dir[tuple(dif)])
        # remove the last element from the route.
        self.route.pop()
        self.map[tuple(self.position)] = "D"


    def oxygenate(self, direction):
        # take input
        # run IntCode
        # return new position (same or different depending on IntCode response)
        directions = {
            "N": 1,
            "S": 2,
            "W": 3,
            "E": 4
        }
        output = self.software.run(input=directions[direction], halt_on_output=True, reset=False)
        if output == 1 or output == 2:
            # if droid can move, update self.position.
            # Remove 'D' mark from old position and replace with "O".
            self.map[tuple(self.position)] = "O"
            # Update current position.
            # north
            if direction == "N":
                self.position[1] += 1
                #print("moving north, new position:", self.position)
            # east
            elif direction == "E":
                self.position[0] += 1
                #print("moving east, new position:", self.position)
            # south
            elif direction == "S":
                self.position[1] -= 1
                #print("moving south, new position:", self.position)
            # west
            elif direction == "W":
                self.position[0] -= 1
                #print("moving west, new position:", self.position)
            # mark new position on the map.
            self.map[tuple(self.position)] = "D"
            if self.position == (-12,-12):
                return 99
        return output


    def scan_and_fill(self):
        # set self.previous_u-turn before making a new move, so we know if the previous move was a u-turn.
        self.previous_uturn = self.uturn
        self.uturn = None
        # which one we try first depends on orientation. We go straight, then right, etc.
        directions = ["N", "E", "S", "W"]
        for d in directions:
            # determine destination and only check it out if it's accessible and unexplored.
            dest = self.get_destination(d)
            if dest not in self.explored and self.map[dest] in [".", "S"]:
                # replace the . by O where the maze has been oxygenated.
                output = self.oxygenate(direction=d)
                if output == 0:
                    print("warning, this direction is not accessible! Droid should not try to go here.")
                elif output == 1:
                    self.route.append(dest)
                    self.explored.append(dest)
                    #display_grid(droid.map)
                    return 1
                elif output == 2:
                    self.route.append(dest)
                    self.map[dest] = "O"
                    self.explored.append(dest)
                    self.oxygen_pos = dest
                    return 2
        # if no new direction to move was found, go back to previous position.
        #print("no options, moving back to previous position!")
        # based on route, figure out which direction to go back to.
        dead_end_pos = self.position
        dead_end_dist = len(self.route)
        try:
            current_pos = self.route[-1]
            previous_pos = self.route[-2]
        except IndexError:
            return 99
        dif = [0, 0]
        dif[0] = current_pos[0] - previous_pos[0]
        dif[1] = current_pos[1] - previous_pos[1]
        dif_dir = {
            (1,0): "W",
            (-1,0): "E",
            (0,1): "S",
            (0,-1): "N"
        }
        if self.map[tuple(self.position)] not in ["S"]:
            self.map[tuple(self.position)] = "O"
        self.move(dif_dir[tuple(dif)])
        # remove the last element from the route.
        self.route.pop()
        self.map[tuple(self.position)] = "D"
        self.uturn = True
        # if the previous move was not a u-turn but this one is, return a -1 code to let the system know
        # we're at a dead end.
        if not self.previous_uturn:
            print("recorded a dead end", dead_end_dist, "steps from oxygen system at", dead_end_pos)
            #display_grid(droid.map)
            self.distances.append(dead_end_dist)
            return -1

code = ic.parse_code('C:/Users/Admin/SURFdrive/Code/advent_of_code/2019/15/input.txt')
software = ic.Intcode(code)

droid = RepairDroid(software)
output = None

while not output == 99:
    output = droid.scan_and_move()
    droid.map[(0, 0)] = "S"

display_grid(droid.map)
print(droid.oxygen_pos)

map = droid.map

# start a new droid
droid2 = RepairDroid(software)

# give it the map we previously established.
droid2.map = map

# first, go to oxygen system.
output = None
while not output == 2:
    output = droid2.scan_and_move()

# then start oxygenating.
output = None
# erase self.explored and start exploring from -12,-12. At every dead end, record distance.
droid2.explored = [(-12,-12)]
droid2.route = []
while not len(droid2.explored) == 799:
    output = droid2.scan_and_fill()
display_grid(droid2.map)
result = max(droid2.distances)

assert result == 278
print(result)