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

    """ to calculate the distance traveled:
    calculate N finished cycles
    N extra seconds < running time or not?
    yes -> add remaining seconds
    no -> add max running time
    
    distance traveled: 
    n_cycles * fly_time * speed
    """
    def get_distance(self, seconds):
        cycle = self.fly_time + self.rest_time
        n_cycles = seconds//cycle
        remainder = seconds % cycle

        # distance traveled:
        distance1 = n_cycles * self.fly_time * self.speed
        if remainder < self.fly_time:
            distance2 = remainder * self.speed
        else:
            distance2 = self.fly_time * self.speed
        return distance1 + distance2

rd = []

for d in data:
    name = d.split()[0]
    numbers = re.findall("[0-9]+", d)
    speed, fly_time, rest_time = list(map(int, numbers))
    rd.append(Reindeer(name, speed, fly_time, rest_time))

results = []
for r in rd:
    results.append(r.get_distance(2503))

assert max(results) == 2660