with open('input.txt') as f:
    instructions = f.read().split("\n")

print(instructions)

class Ferry(object):

    def __init__(self, direction):
        self.east = 0
        self.north = 0
        self.directions = ['N', 'E', 'S', 'W']
        if direction in self.directions:
            self.direction = direction
        else:
            raise ValueError("not a valid direction")

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

    def move(self, instruction):
        amount = int(instruction[1])
        if instruction[0] == 'F':
            direction = self.direction
        else:
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

    def navigate(self, input_line):
        instruction = self.read_nav(input_line)
        if input_line[0] in ['L', 'R']:
            self.turn(instruction)
        elif instruction[0] in ['F', 'N', 'E', 'S', 'W']:
            self.move(instruction)
        position = (self.east, self.north)
        return position

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


f = Ferry('E')
for i in instructions:
    print(f.navigate(i))

print(f.position)
print(f.manhattan_distance)

assert f.manhattan_distance == 1186

