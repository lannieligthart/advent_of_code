from AoC_tools import aoc24 as aoc

s = aoc.start()

#infile = "testinput.txt"
infile = "input.txt"

with open(infile) as f:
    data = f.read().split("\n")

data = [list(d) for d in data]

nrows = len(data)
ncols = len(data[0])

for c in range(ncols-1):
    for r in range(nrows-1):
        if data[r][c] == "^":
            start_pos = (r, c)

directions = ["N", "E", "S", "W"]

move_dir = {"N": (-1, 0), "S": (1, 0), "E": (0, 1), "W": (0, -1)}

def run(data, start_pos, nrows, ncols, first_run=False):
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
                # only in the first run, record all non-turning positions
                if first_run:
                    visited.append(((r,c), direction))

        elif data[r][c] == "#":
            r, c = old
            # in all runs, record the turning positions
            visited.append(((r,c), direction))
            direction += 1
            direction = direction % 4
    return visited

loops = set()

# at first run, record all positions we know where we should place obstacles
visited = run(data, start_pos, nrows, ncols, first_run=True)

# place obstacles
for v in visited:
    row, col = v[0]
    if data[row][col] != "#":
        data_mod = [d.copy() for d in data]
        data_mod[row][col] = "#"
        if run(data_mod, start_pos, nrows, ncols) == "loop":
            print(f"found loop at ({row},{col})")
            loops.add((row, col))

if infile == "input.txt":
    assert len(loops) == 1516
if infile == "testinput.txt":
    assert len(loops) == 6

aoc.end(s)