from AoC_tools import aoc22 as aoc
with open("input.txt") as file:
    data = file.read().split("\n")

r = 0
c = 0
visited = [(r, c)]
for d in data:
    d = d.split()
    drc, dist, col = d
    dist = int(dist)
    for i in range(dist):
        if drc == "R":
            c += 1
        elif drc == "L":
            c -= 1
        elif drc == "U":
            r -= 1
        elif drc == "D":
            r += 1
        visited.append((r, c))

#bepaal de min en max van visited
r_min = min([v[0] for v in visited])
c_min = min([v[1] for v in visited])
c_max = max([v[1] for v in visited])

# avoid issues with negative indices by adjusting the y axis
visited = [(v[0] - r_min, v[1] - c_min) for v in visited ]

grid = aoc.Grid.from_list(visited)
grid.transpose()

# add points to the empty positions
for x in range(grid.x_min, grid.x_max + 1):
    for y in range(grid.y_min, grid.y_max + 1):
        if (x, y) not in grid.points:
            grid.add_points([(x, y)], ".")

def make_grid_from_dict(dictionary):
    # (c, r) (x, y
    x_min = min([k[0] for k in dictionary.keys()])
    x_max = max([k[0] for k in dictionary.keys()])
    y_min = min([k[1] for k in dictionary.keys()])
    y_max = max([k[1] for k in dictionary.keys()])
    # fill all spots with "."
    matrix = [["." for _ in range(y_min, y_max + 1)] for _ in range(x_min, x_max + 1)]
    # add the existing values
    for key, value in dictionary.items():
        x, y = key
        matrix[x][y] = value
    return matrix

values = grid.values
matrix = make_grid_from_dict(values)
matrix = aoc.transpose(matrix)

# add margin
matrix.append(["." for x in range(c_max + 1)])
matrix.insert(0, ["." for x in range(c_max + 1)])
for row in matrix:
    row.insert(0, ".")
for row in matrix:
    row.append(".")


def on_grid(matrix, pos):
    r, c = pos
    max_row = len(matrix) - 1
    max_col = len(matrix[0]) - 1
    if r >= 0 and r <= max_row and c >= 0 and c <= max_col:
        return True
    else:
        return False


def flood_fill(data, r, c):
    """takes a matrix and a start position, returns filled up matrix"""
    done = set()
    queue = [(r, c)]
    while len(queue) > 0:
        r, c = queue.pop(0)
        if data[r][c] != "#" and (r, c) not in done:
            data[r][c] = "X"
            done.add((r, c))
        nb = aoc.get_nb((r, c))
        # if these neigbours are on the grid, not in done, and not a "#" convert them and add their neighbours to the queue
        for n in nb:
            if on_grid(data, n) and data[r][c] != "#" and n not in queue and n not in done:
                queue.append(n)
    return data

result = flood_fill(matrix, 0, 0)

xcount = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == "X":
            xcount += 1

surface = len(matrix) * len(matrix[0])
assert (surface - xcount) == 40761
