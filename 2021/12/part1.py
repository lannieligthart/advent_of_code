

def sort(values, include_start=True):
    # sort values such that start comes first and end comes last, and in between is sorted alphabetically
    new_values = []
    tail = []
    if "start" in values:
        if include_start:
           new_values.append("start")
        values.remove("start")
    if "end" in values:
        new_values.append("end")
        values.remove("end")
    values.sort()
    new_values.extend(values)
    new_values.extend(tail)
    return new_values

def issmall(value):
    if value.lower() == value and not value == 'end' and not value == 'start':
        return True
    else:
        return False

with open("testinput.txt") as f:
    data = [line.split("-") for line in f.read().splitlines()]

# create dict with possible targets from each node (exlcuding "end")
nodes = {}

for d in data:
    if not d[0] in nodes:
        nodes[d[0]] = [d[1]]
    elif d[0] in nodes:
        nodes[d[0]].append(d[1])
    if not d[1] in nodes:
        nodes[d[1]] = [d[0]]
    elif d[1] in nodes:
        nodes[d[1]].append(d[0])

delete = []

# if a small cave has only one entrance it can be removed from the options list because it will never be useful to visit.
# this is not necessary, algorithm works fine without it, maybe slightly more efficient.
for key, value in nodes.items():
    if issmall(key) and len(value) == 1 and issmall(value[0]):
        delete.append(key)
for d in delete:
    nodes.pop(d)

# sort the values of each key
for key, value in nodes.items():
    nodes[key] = sort(value, include_start=False)

# # sort the dictionary by key
# keys = list(nodes.keys())
# keys = sort(keys)
#
# sorted_nodes = {}
# for key in keys:
#     sorted_nodes[key] = nodes[key]
#
# for key, value in sorted_nodes.items():
#     print(key, value)

routes = []
cur = "start"
route = [cur]

def find_routes(nodes):
    route = ["start"]
    routes = [route]
    finished = []
    complete_routes = []
    while len(routes) > 0:
        for i in range(len(routes)):
            route = routes[i]
            cur = route[-1]
            try:
                # a target is an option if it's not a small cave that has already been visited.
                options = [n for n in nodes[cur] if not (issmall(n) and n in route)]
            except KeyError:
                options = []
            for o in options:
                new_route = route.copy()
                new_route.append(o)
                if new_route[-1] == "end":
                    complete_routes.append(new_route)
                else:
                    routes.append(new_route)
            finished.append(route)
        for f in finished:
            routes.remove(f)
        finished = []

        #print(complete_routes)
    return complete_routes

routes = find_routes(nodes)
print(len(routes))

assert len(routes) == 5333