#infile = "testinput.txt"
infile = "input.txt"

with open(infile) as f:
    data = f.read().split("\n")

data = [list(d) for d in data]

nrows = len(data)
ncols = len(data[0])
print(f"rows:{nrows}")
print(f"cols:{ncols}")

for c in range(ncols-1):
    for r in range(nrows-1):
        if data[r][c] == "^":
            start_pos = (r, c)

print(f"start position: {start_pos}")

directions = ["N", "E", "S", "W"]

move_dir = {"N": (-1, 0),
            "S": (1, 0),
            "E": (0, 1),
            "W": (0, -1)}



def run(data, start_pos, nrows, ncols):
    direction = 0
    visited = [(start_pos, direction)]
    r, c = start_pos
    while True:
        old = (r, c)
        r += move_dir[directions[direction]][0]
        c += move_dir[directions[direction]][1]
        # if the guard has left the map, stop
        if r < 0 or r >= nrows or c < 0 or c >= ncols:
            break
        if data[r][c] != "#":
            if ((r, c), direction) in visited:
                return "loop"
            else:
                visited.append(((r,c), direction))

        elif data[r][c] == "#":
            r, c = old
            direction += 1
            direction = direction % 4
            #print(f"current position: ({r, c})")
            #print(f"turning {directions[direction]}")
    return visited

loops = []

visited = run(data, start_pos, nrows, ncols)

# place obstacles
for v in visited:
    row, col = v[0]
    if data[row][col] != "#":
        data_mod = [d.copy() for d in data]
        if col % 50 == 0 and row % 10 == 0:
            print(f"modifying ({row, col})")
        data_mod[row][col] = "#"
        if run(data_mod, start_pos, nrows, ncols) == "loop":
            print(f"found loop at ({row},{col})")
            loops.append((row, col))

loops = list(set(loops))
print(loops)
print(len(loops))

# row, col = [6,3]
# row, col = [7,6]
# row, col = [7,7]
# row, col = [8,1]
# row, col = [8,3]
# row, col = [9,7]