from itertools import permutations

with open("input.txt") as file:
    data = file.read().split("\n")

data = [d.split() for d in data]

# list all the cities
cities = set()
for d in data:
    cities.add(d[0])
    cities.add(d[2])

# make a list of all possible routes
routes = list(permutations(cities, len(cities)))

# make a dictionary with distances between each pair of cities
distances = dict()
for d in data:
    distances[(d[0], d[2])] = int(d[4])
    distances[(d[2], d[0])] = int(d[4])

# calculate the distance for each route
def get_distance(route):
    distance = 0
    for i in range(len(route) - 1):
        distance += distances[(route[i], route[i + 1])]
    return distance

route_distances = dict()
for r in routes:
    route_distances[r] = get_distance(r)

# print the results for satisfying visualization
for key, value in route_distances.items():
    print(key, value)

# part 1: shortest route
assert min(route_distances.values()) == 207

# part 2: longest route
assert max(route_distances.values()) == 804