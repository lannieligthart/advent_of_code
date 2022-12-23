from AoC_tools.aoc22 import read_input, Grid, start, end


class State(object):

    def __init__(self, grid):
        self.facing = None
        self.position = None
        self.grid = grid
        self.facings = [">", "v", "<", "^"]

    def turn(self, direction):
        """takes a direction and a facing and returns the new facing"""
        if direction == "R":
            self.facing = (self.facing + 1) % 4
        elif direction == "L":
            self.facing = (self.facing - 1) % 4
        self.grid.add(self.position, self.facings[self.facing])

    def step(self):
        c, r = self.position
        old_position = (c, r)

        while True:
            # 0 = E, 1 = S, 2 = W, 3 = N
            if self.facing == 0:
                c += 1
            elif self.facing == 2:
                c -= 1
            elif self.facing == 3:
                r -= 1
            elif self.facing == 1:
                r += 1
            # check new position
            # als y nu groter is dan y_max wordt y = y_min
            if r > self.grid.y_max:
                r = self.grid.y_min
            elif r < self.grid.y_min:
                r = self.grid.y_max
            # same for x
            if c > self.grid.x_max:
                c = self.grid.x_min
            elif c < self.grid.x_min:
                c = self.grid.x_max
            # if current position is not on the map (i.e. value == " "), repeat
            # if it is in on the map, but it's a wall, return old position
            if self.grid.values[(c, r)] == "#":
                #print(f"Hit a wall at {(c, r)}, stayed at {old_position}")
                return old_position
            # if it's on the map and it's not a wall, return current position
            elif self.grid.values[(c, r)] in [".", ">", "^", "<", "v"]:
                self.grid.add((c, r), self.facings[self.facing])
                return (c, r)

    def move(self, steps):
        for i in range(steps):
            old_position = self.position
            self.position = self.step()
            if self.position == old_position:
                break

st = start()

data = read_input("input.txt", "\n\n", strip=False)
instructions = data[1]
data = data[0].split("\n")
data = list(map(list, data))
# bepaal maximale lengte en voeg padding toe waar nodig zodat alle rijen even lang zijn
maxlen = max([len(d) for d in data])
for i in range(len(data)):
    delta = maxlen - len(data[i])
    for d in range(delta):
        data[i].append(' ')

route = []
n = ''
for char in instructions:
    if char.isdigit():
        n += char
    else:
        route.append(int(n))
        direction = char
        route.append(char)
        n = ''
route.append(int(n))

# 0 = E, 1 = S, 2 = W, 3 = N

grid = Grid()
grid = Grid.read(data)
grid.display()
state = State(grid)
state.facing = 0
state.position = (data[0].index("."), 0)
state.grid.add(state.position, "X")

for i, r in enumerate(route):
    if isinstance(r, int):
        state.move(r)
    elif isinstance(r, str):
        state.turn(r)
    if i % 500 == 0:
        print(i)

final_col = state.position[0] + 1
final_row = state.position[1] + 1

print(f"position: {state.position}")
print(f"facing: {state.facing}")
result = final_row * 1000 + final_col * 4 + state.facing

assert result == 43466

end = end(st)
