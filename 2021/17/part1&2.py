# ugly brute force solution with boundaries based on trial and error rather than mathematical insight,
# but hey, if it works, it works!

def step(pos, x_vel, y_vel):
    x, y = pos
    # The probe's x position increases by its x velocity.
    x += x_vel
    # The probe's y position increases by its y velocity.
    y += y_vel
    # Due to drag, the probe's x velocity changes by 1 toward the value 0; that is, it decreases by 1 if it is greater
    # than 0, increases by 1 if it is less than 0, or does not change if it is already 0.
    if x_vel > 0:
        x_vel -= 1
    elif x_vel < 0:
        x_vel += 1
    # Due to gravity, the probe's y velocity decreases by 1."""
    y_vel -= 1
    return ((x, y), x_vel, y_vel)

def range_is_between(path_range, target_range):
    # test if the target range is between the min and max values in the path
    if target_range[0] > path_range[0] and target_range[1] < path_range[1]:
        return True

def crossed(path, tx_min, tx_max, ty_min, ty_max):
    """test if a path has traversed a zone defined by a lower and an upper bound"""
    # if route contains x values below and above min and max, or y values idem, it means the path has crossed
    # the zone.
    x_values = []
    y_values = []
    for pos in path:
        x_values.append(pos[0])
        y_values.append(pos[1])
    path_rangex = min(x_values), max(x_values) + 1
    target_rangex = (tx_min, tx_max + 1)
    path_rangey = min(y_values), max(y_values) + 1
    target_rangey = (ty_min, ty_max + 1)
    if range_is_between(path_rangex, target_rangex) or range_is_between(path_rangey, target_rangey):
        return True
    else:
        return False


def run(x_vel, y_vel, tx_min, tx_max, ty_min, ty_max):
    pos = (0 ,0)
    path = [pos]
    while True:
        pos, x_vel, y_vel = step(pos, x_vel, y_vel)
        path.append(pos)
        if pos in target:
            #print("hit target!")
            #print(path)
            yvals = [p[1] for p in path]
            return pos
        if crossed(path, tx_min, tx_max, ty_min, ty_max):
            #print("passed range without hitting target")
            #print(path)
            return None

# testdata
#data = "target area: x=20..30, y=-10..-5".replace("target area: x=", "").replace("y=" ,"")
# real data
data = "target area: x=137..171, y=-98..-73".replace("target area: x=", "").replace("y=" ,"")
data = data.split(", ")
data = [d.split("..") for d in data]

pos = (0, 0)

tx_min = int(data[0][0])
tx_max = int(data[0][1])
ty_min = int(data[1][0])
ty_max = int(data[1][1])

# example data
target = []
for x in range(tx_min, tx_max + 1):
    for y in range(ty_min, ty_max + 1):
        target.append((x, y))

positions = []
for x_vel in range(0,200):
     for y_vel in range(-100, 98):
        result = (run(x_vel, y_vel, tx_min, tx_max, ty_min, ty_max))
        if result is not None:
            positions.append((x_vel, y_vel))

xvals = [p[0] for p in positions]
print("range x values:", min(xvals), max(xvals))
yvals = [p[1] for p in positions]
print("range y values:", min(yvals), max(yvals))
print("number of hits:", len(positions))

maxy = max(yvals)
print(maxy)


#part 1:
assert maxy == 97

# part2:
assert len(positions) == 1546
