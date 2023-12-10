import re

with open("input.txt") as file:
    data = file.read().split("\n")

class Reindeer(object):

    def __init__(self, name, speed, fly_time, rest_time):
        self.name = name
        self.speed = speed
        self.fly_time = fly_time
        self.rest_time = rest_time
        self.time = 0
        self.distance = 0
        self.points = 0

    def get_distance(self, seconds):
        cycle = self.fly_time + self.rest_time
        n_cycles = seconds // cycle
        remainder = seconds % cycle

        # distance traveled:
        distance1 = n_cycles * self.fly_time * self.speed
        if remainder < self.fly_time:
            distance2 = remainder * self.speed
        else:
            distance2 = self.fly_time * self.speed
        self.distance = distance1 + distance2

    def add_points(self, points):
        self.points += points

rd = dict()

for d in data:
    name = d.split()[0]
    numbers = re.findall("[0-9]+", d)
    speed, fly_time, rest_time = list(map(int, numbers))
    rd[name] = Reindeer(name, speed, fly_time, rest_time)

for i in range(1, 2504):  # start counting after the first second.
    max_distance = 0
    for r in rd.values():
        # calculate current distance
        r.get_distance(i)
        if r.distance > max_distance:
            max_distance = r.distance

    # The reindeer who is in the lead gets one point each second.
    # if they are tied, both get a point.
    for r in rd.values():
        if r.distance == max_distance:
            r.points += 1

results = [r.points for r in rd.values()]

assert max(results) == 1256

