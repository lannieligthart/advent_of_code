with open('C:/Users/Admin/Documents/Code/advent_of_code/2019/3/testinput1.txt') as f:
    data1 = f.read().split("\n")

with open('C:/Users/Admin/Documents/Code/advent_of_code/2019/3/testinput2.txt') as f:
    data2 = f.read().split("\n")

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

def get_min_steps(overlap, positions1, positions2):
    # for all positions that overlap, get the number of steps for each wire track to reach it
    steps1 = []
    steps2 = []
    for o in overlap:
        for i in range(len(positions1)):
            if o == positions1[i]:
                steps1.append(i+1)
        for i in range(len(positions2)):
            if o == positions2[i]:
                steps2.append(i+1)
    summed_steps = [steps1[i] + steps2[i] for i in range(len(steps1))]
    return min(summed_steps)


def get_shortest_cross_dist(data):
    path1 = data[0].split(",")
    path2 = data[1].split(",")
    positions1 = track_wire(path1)
    positions2 = track_wire(path2)
    overlap = list(set(positions1) & set(positions2))
    shortest_dist = get_min_steps(overlap, positions1, positions2)
    return shortest_dist


assert get_shortest_cross_dist(data1) == 610
assert get_shortest_cross_dist(data2) == 410
assert get_shortest_cross_dist(data) == 12934

print(get_shortest_cross_dist(data))


