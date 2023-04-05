
with open("input.txt") as file:
    data = file.read()

x = 0
y = 0
visited = set()
visited.add((x, y))

for char in data:
    if char == ">":
        x += 1
    elif char == "<":
        x -= 1
    elif char == "^":
        y += 1
    elif char == "v":
        y -= 1
    visited.add((x, y))

assert len(visited) == 2592
