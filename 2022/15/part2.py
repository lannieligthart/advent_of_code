import AoC_tools.aoc22 as aoc

class range_2d(object):

    def __init__(self, point, md):
        self.x_min = (point.x - md)
        self.x_max = (point.x + md)
        self.y_min = (point.y - md)
        self.y_max = (point.y + md)
        self.md = md
        self.x = point.x
        self.y = point.y

    def __str__(self):
        return f"Position: ({self.x}, {self.y})\nX range: {self.x_min}, {self.x_max}\nY range: {self.y_min}, {self.y_max}\n"

    def get_y_range(self, y_value, lower, upper):
        if y_value >= self.y_min and y_value <= self.y_max:
            a = abs(y_value - self.y)
            b = abs(a - self.md)
            x_min = self.x - b
            x_max = self.x + b
            if x_min < lower:
                x_min = lower
            elif x_min > upper:
                x_min = upper
            if x_max < lower:
                x_max = lower
            elif x_max > upper:
                x_max = upper
            return x_min, x_max

def mhd(self, other):
    """manhattan distance"""
    return abs(self.x - other.x) + abs(self.y - other.y)

def merge_ranges(r1, r2):
    # If there is overlap:
    if r1[1] >= r2[0]-1:
        # determine min and max of both ranges
        x = min(r1[0], r2[0])
        y = max(r1[1], r2[1])
        return (x, y)

def merge(ranges):
    start_pos = 0
    while len(ranges) > start_pos + 1:
        if start_pos == len(ranges):
            break
        r1 = ranges[start_pos]
        r2 = ranges[start_pos + 1]
        result = merge_ranges(r1, r2)
        if result is not None:
            ranges.pop(start_pos + 1)
            ranges.pop(start_pos)
            ranges.append(result)
            ranges.sort(key=lambda y: y[0])
        else:
            start_pos += 1
    return ranges

start_time = aoc.start()

limit = 4000000
#limit = 20

# parse the data
data = aoc.read_input("input.txt")
#data = aoc.read_input("testinput.txt")
data = [d.replace("Sensor at x=", "") for d in data]
data = [d.replace(", y=", ",") for d in data]
data = [d.replace(": closest beacon is at x=", ",") for d in data]
data = [d.replace(", y=", ",") for d in data]
data = [d.split(",") for d in data]
data = [list(map(int, d)) for d in data]

# create a list of all 2-dimensional ranges detected by the sensors
# and while we're at it, plot the sensors and beacons on a grid
detected = []

for d in data:
    s = aoc.Point(d[0], d[1])
    b = aoc.Point(d[2], d[3])
    md = mhd(s, b)
    detected.append(range_2d(s, md))

for i in range(limit):
    ranges = []
    for d in detected:
        r = d.get_y_range(i, lower=0, upper=limit)
        if r is not None:
            ranges.append(r)
            ranges.sort(key=lambda y: y[0])
    ranges = merge(ranges)
    # if i % 100000 == 0:
    #     print(i)
    if len(ranges) == 2:
        break

result = ((ranges[0][1]+1) * 4000000 + i)
print(result)

#assert result == 56000011
assert result == 13350458933732

aoc.end(start_time)