import AoC_tools.aoc22 as aoc

data = aoc.read_input("input.txt")

data = [list(d) for d in data]
for y in range(len(data)):
    for x in range(len(data[y])):
        if data[y][x] == 'S':
            start_x, start_y = x, y
        elif data[y][x] == 'E':
            end_x, end_y = x, y

print(f"start: {start_x}, {start_y}\nend: {end_x}, {end_y}")

data[start_y][start_x] = 'a'
data[end_y][end_x] = 'z'
data = [[ord(letter)-97 for letter in d] for d in data]

elevations = aoc.Grid.read(data)

not_visited = list(elevations.values.keys())
visited = []
distances = {(start_x, start_y): elevations.get_value((start_x, start_y))}

while len(not_visited) > 0:
    # check if any of the non-visited points have a distance.
    options = [p for p in not_visited if p in distances.keys()]
    if len(options) == 0:
        break
    # pick a point that is not in visited and has a distance
    for pos in options:
        if pos in distances:
            # get neighbours of current point
            nb = elevations.get_neighbours(aoc.Point(*pos), 4)
            # for each neighbour, determine the distance
            for n in nb:
                # you can climb at most 1, but descend any amount.
                delta = elevations.get_value(pos) - elevations.get_value(n.pos)
                if delta >= -1:
                    dist = distances[pos] + 1
                    if n.pos not in distances:
                        distances[n.pos] = dist
            not_visited.remove(pos)
            visited.append(pos)

assert distances[(end_x, end_y)] == 468