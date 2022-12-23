from AoC_tools.aoc22 import Point, Vector, Grid, read_input, start, end

def add_line(v1, v2, points):
    dif = v2 - v1
    if dif.x > 0:
        for i in range(dif.x+1):
            p = Point(v1.x + i, v1.y + 0)
            points.append(p)
    elif dif.x < 0:
        for i in range(0, dif.x-1, -1):
            p = Point(v1.x + i, v1.y + 0)
            points.append(p)
    elif dif.y > 0:
        for i in range(dif.y+1):
            p = Point(v1.x + 0, v1.y + i)
            points.append(p)
    elif dif.y < 0:
        for i in range(0, dif.y-1, -1):
            p = Point(v1.x + 0, v1.y + i)
            points.append(p)
    return points

def make_cave(data):
    points = []
    for line in data:
        line = line.split(" -> ")
        line = [x.split(",") for x in line]
        line = [list(map(int, x)) for x in line]
        for i in range(len(line) - 1):
            v1 = Vector(*line[i])
            v2 = Vector(*line[i+1])
            points = add_line(v1, v2, points)
    grid = Grid.from_list(points)
    for p in points:
        grid.points[p.pos] = p
        grid.values[p.pos] = '#'
    return grid

def drop_sand(grid, bottom):
    x, y = (500, 0)
    while True:
        # once the sand has reached the bottom, it comes to a halt
        if y >= bottom:
            return Point(x, y)
        # try to move down
        # if y+1 == grid.y_max, return
        elif (x, y+1) not in grid.points.keys():
            y += 1
        # else, try to move down left
        elif (x-1, y+1) not in grid.points.keys():
            y += 1
            x -= 1
        # else, try to move down right
        elif (x+1, y+1) not in grid.points.keys():
            y += 1
            x += 1
        else:
            return Point(x, y)


s = start()

data = read_input("input.txt")
cave = make_cave(data)
i = 0
bottom = cave.y_max + 1

while True:
    newpoint = drop_sand(cave, bottom)
    if newpoint.pos != (500, 0):
        cave.points[newpoint.pos] = newpoint
        cave.values[newpoint.pos] = 'o'
        i += 1
    # once the new sand stays in start position, stop.
    elif newpoint.pos == (500, 0):
        cave.points[newpoint.pos] = newpoint
        cave.values[newpoint.pos] = 'o'
        break

assert i + 1 == 26375

e = end(s)