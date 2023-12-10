with open("input.txt") as file:
    data = file.read().split("\n")
    data = [tuple(map(int, d.split(", "))) for d in data]

x = [d[0] for d in data]
y = [d[1] for d in data]

data = {(d): i for i, d in enumerate(data)}

def manhattan(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def total_distance(ref_pos, coordinates):
    total = 0
    for pos in coordinates:
        total += manhattan(ref_pos, pos)
    return total

distances = []
for i in range(min(x), max(x) + 1):
    for j in range(min(y), max(y)+ 1):
        dist = total_distance((i, j), data.keys())
        if dist < 10000:
            distances.append(dist)

assert len(distances) == 38380
