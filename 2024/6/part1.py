from AoC_tools import aoc24 as aoc

s = aoc.start()

#infile = "testinput.txt"
infile = "input.txt"

with open(infile) as f:
    data = f.readlines()

nrows = len(data)
ncols = len(data[0])

for c in range(ncols-1):
    for r in range(nrows-1):
        if data[r][c] == "^":
            start_pos = (r, c)

directions = ["N", "E", "S", "W"]
move_dir = {"N": (-1, 0), "S": (1, 0), "E": (0, 1), "W": (0, -1)}

visited = [start_pos]
direction = 0

r, c = start_pos

while True:
    old = (r, c)
    r += move_dir[directions[direction]][0]
    c += move_dir[directions[direction]][1]
    # if the guard has left the map, stop
    if r < 0 or r >= len(data) or c < 0 or c >= len(data[0]):
        break
    if data[r][c] != "#":
        visited.append((r,c))
    elif data[r][c] == "#":
        # we can't go here so reset position to the previous one
        r, c = old
        # turn right, and note we have only 4 possible directions
        direction += 1
        direction = direction % 4
        print(f"current position: ({r, c})")
        print(f"turning {directions[direction]}")

visited = list(set(visited))
print(visited)
print(len(visited))


#4434 klopt niet
#4433 is het juiste antwoord?
if infile == "testinput.txt":
    assert len(visited) == 41

if infile == "input.txt":
    assert len(visited) == 4433

aoc.end(s)
