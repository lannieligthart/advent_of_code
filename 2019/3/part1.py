with open('C:/Users/Admin/Documents/Code/advent_of_code/2019/3/input.txt') as f:
    data = f.read().split("\n")

def track_wire(path):
    x = 0
    y = 0
    positions = []
    for step in path:
        direction = step[0]
        n = int(step[1:])
        xdif = 0
        ydif = 0
        if direction == 'R':
            xdif = n
        elif direction == 'L':
            xdif = -n
        elif direction == 'U':
            ydif = n
        elif direction == 'D':
            ydif = -n
        # append all intermediate positions to a list
        # 4 naar rechts:
        if xdif > 0:
            for i in range(xdif):
                x += 1
                positions.append((x,y))
        elif xdif < 0:
            for i in range(-xdif):
                x -= 1
                positions.append((x,y))
        elif ydif > 0:
            for i in range(ydif):
                y += 1
                positions.append((x,y))
        elif ydif < 0:
            for i in range(-ydif):
                y -= 1
                positions.append((x,y))

    return positions

def get_shortest_dist(overlap):
    distances = []
    for i in overlap:
        dist = abs(i[0]) + abs(i[1])
        distances.append(dist)
    return min(distances)


def get_shortest_cross_dist(data):
    path1 = data[0].split(",")
    path2 = data[1].split(",")
    positions1 = track_wire(path1)
    positions2 = track_wire(path2)
    overlap = list(set(positions1) & set(positions2))
    closest = get_shortest_dist(overlap)
    return closest

print(get_shortest_cross_dist(data))

assert (get_shortest_cross_dist(data)) == 308