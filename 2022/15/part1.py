import AoC_tools.aoc22 as aoc

class range_2d(object):

    def __init__(self, point, md):
        self.x_min = (point.x - md) - 1
        self.x_max = (point.x + md) + 1
        self.y_min = (point.y - md) - 1
        self.y_max = (point.y + md) + 1
        self.md = md
        self.x = point.x
        self.y = point.y

    def __str__(self):
        return f"X range: {self.x_min}, {self.x_max}\nY range: {self.y_min}, {self.y_max}\n"

    def get_y_range(self, y_value):
        if y_value >= self.y_min and y_value <= self.y_max:
            a = abs(y_value - self.y)
            b = self.md - a
            return self.x - b, self.x + b

def mhd(self, other):
    """manhattan distance"""
    return abs(self.x - other.x) + abs(self.y - other.y)

def merge_ranges(r1, r2):
    # If there is overlap (if not, return nothing):
    if r1[1] >= r2[0]-1:
        # determine min and max of both ranges
        x = min(r1[0], r2[0])
        y = max(r1[1], r2[1])
        return (x, y)

def merge(ranges):
    r1 = ranges[0]
    r2 = ranges[1]
    result = merge_ranges(r1, r2)
    if result is not None:
        ranges.pop(1)
        ranges.pop(0)
        ranges.append(result)
        ranges.sort(key=lambda y: y[0])

data = aoc.read_input("input.txt")
data = [d.replace("Sensor at x=", "") for d in data]
data = [d.replace(", y=", ",") for d in data]
data = [d.replace(": closest beacon is at x=", ",") for d in data]
data = [d.replace(", y=", ",") for d in data]
data = [d.split(",") for d in data]
data = [list(map(int, d)) for d in data]

grid = aoc.Grid()

detected = []

for d in data:
    s = aoc.Point(d[0], d[1])
    b = aoc.Point(d[2], d[3])
    grid.add(s, "S")
    grid.add(b, "B")
    md = mhd(s, b)
    detected.append(range_2d(s, md))

ranges = []
for d in detected:
    r = d.get_y_range(2000000)
    if r is not None:
        ranges.append(r)
ranges.sort(key=lambda y: y[0])
while len(ranges) > 1:
    merge(ranges)

result = abs(ranges[0][0]) + abs(ranges[0][1])
print(result)

assert result == 5176944




