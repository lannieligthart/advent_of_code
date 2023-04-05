
with open("input.txt") as file:
    data = file.read()


class Santa(object):

    def __init__(self):
        self.x = 0
        self.y = 0
        self.visited = {(0, 0)}

    def update(self, direction):
        if direction == ">":
            self.x += 1
        elif direction == "<":
            self.x -= 1
        elif direction == "^":
            self.y += 1
        elif direction == "v":
            self.y -= 1
        self.visited.add((self.x, self.y))


s = Santa()
r = Santa()

for i, char in enumerate(data):
    # even turns: robo goes
    if i % 2 == 0:
        r.update(char)
    # odd turns: Santa goes
    if i % 2 == 1:
        s.update(char)

visited = s.visited.union(r.visited)

assert len(visited) == 2360
