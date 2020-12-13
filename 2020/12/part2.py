with open('input.txt') as f:
    instructions = f.read().split("\n")

class Waypoint(object):

    def __init__(self, east, north):
        # positions with relative to ship
        self.east = east
        self.north = north

    def swap(self):
        east = self.east
        north = self.north
        self.east = north
        self.north = east

    def rotate(self, instruction):
        print("\ninstruction:", instruction)
        if instruction[0] == 'R':
            amount = instruction[1]
        elif instruction[0] == 'L':
            amount = 360 - instruction[1]

        # to rotate the waypoint 90 degrees
        # sign change east, swap
        if amount == 90:
            self.east = -self.east
            self.swap()
        # to rotate 270 degrees (= -90):
        # sign change north, swap
        if amount == 270:
            self.north = -self.north
            self.swap()
        # to rotate 180 degrees, flip the sign of the coordinates
        elif amount == 180:
            self.east = -self.east
            self.north = -self.north
        print("new waypoint settings:", self.east, self.north)

    def move(self, instruction):
        print("\ninstruction:", instruction)
        amount = int(instruction[1])
        direction = instruction[0]
        # forward: add amount to
        if direction == 'N':
            self.north += amount
        elif direction == 'S':
            self.north -= amount
        elif direction == 'E':
            self.east += amount
        elif direction == 'W':
            self.east -= amount
        print("moving waypoint", amount, direction)
        print("new waypoint settings:", self.east, self.north)

class Ferry(object):

    def __init__(self, waypoint):
        self.east = 0
        self.north = 0
        self.waypoint = waypoint

    @staticmethod
    def read_nav(line):
        if line[0] in ['N', 'E', 'S', 'W', 'R', 'L', 'F']:
            part1 = line[0]
        else:
            raise ValueError("Not a valid instruction!")
        part2 = int(line[1:])
        return[part1, part2]

    def turn(self, instruction):
        # get index of current direction
        for d in range(len(self.directions)):
            if self.direction == self.directions[d]:
                cur_pos = d
        # determine amount of direction change
        amount = int(instruction[1]/90)
        # Then change direction
        # turning right is clockwise so direction + 1
        if instruction[0] == 'R':
            cur_pos += amount
        # left is -1
        elif instruction[0] == 'L':
            cur_pos -= amount
        cur_pos = cur_pos % len(self.directions)
        self.direction = self.directions[cur_pos]

    @property
    def position(self):
        if self.north >= 0:
            dir2 = 'north'
        elif self.north < 0:
            dir2 = 'south'
        if self.east >= 0:
            dir1 = 'east'
        elif self.east < 0:
            dir1 = 'west'
        return dir1 + " " + str(abs(self.east)) + ", " + dir2 + " " + str(abs(self.north))

    @property
    def manhattan_distance(self):
        return abs(self.east) + abs(self.north)

    def rotate_waypoint(self, instruction):
        self.waypoint.rotate(instruction)

    def move_waypoint(self, instruction):
        self.waypoint.move(instruction)

    def forward(self, instruction):
        amount = instruction[1]
        print("\ninstruction:", instruction)
        print("east position:", self.east)
        self.east += self.waypoint.east * amount
        print("new east position:", self.east)
        print("north position:", self.north)
        self.north += self.waypoint.north * amount
        print("new north position:", self.north)
        print("moving to:", self.east, self.north)

    def navigate(self, input_line):
        instruction = self.read_nav(input_line)
        # L/R now means rotate the ship's waypoint the specified number of degrees
        if instruction[0] in ['L', 'R']:
            self.rotate_waypoint(instruction)
        # NESW now means moving the waypoint in the specified direction by the given value
        elif instruction[0] in ['N', 'E', 'S', 'W']:
            self.move_waypoint(instruction)
        # forward now means to move toward the waypoint as many times as the value
        elif instruction[0] == 'F':
            self.forward(instruction)
        position = (self.east, self.north)
        return position

w = Waypoint(10, 1)
f = Ferry(w)
print("start position:", f.east, f.north)
print("waypoint settings:", f.waypoint.east, f.waypoint.north, "\n")

for i in instructions:
    f.navigate(i)
print(f.position)
print(f.manhattan_distance)

assert f.manhattan_distance == 47806

