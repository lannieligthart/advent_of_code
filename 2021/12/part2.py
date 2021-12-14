

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

with open("input.txt") as f:
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

# sort the values of each key
for key, value in nodes.items():
    nodes[key] = sort(value, include_start=False)

routes = []
cur = "start"
route = [cur]

def visited_twice(route):
    counts = {}
    for node in route:
        if issmall(node):
            counts[node] = route.count(node)
            if counts[node] == 2:
                return True
    return None

def find_routes(nodes):
    route = ["start"]
    routes = [route]
    finished = []
    complete_routes = []
    while len(routes) > 0:
        # walk through the routes
        for i in range(len(routes)):
            # add possible nodes to the current route
            route = routes[i]
            cur = route[-1]
            # make a list of options
            try:
                options = []
                for n in nodes[cur]:
                    # a target is an option if it's a big cave
                    if not issmall(n):
                        options.append(n)
                    # or if it's a small cave and no small cave has yet been visited twice
                    elif issmall(n) and not (visited_twice(route) and n in route):
                        options.append(n)
            except KeyError:
                options = []
            # walk through the options and add a new route to the list of routes for each option
            for o in options:
                new_route = route.copy()
                new_route.append(o)
                # if the route is now finished, add the route to the list of completed routes
                if new_route[-1] == "end":
                    complete_routes.append(new_route)
                else:
                    routes.append(new_route)
            # keep a list of which routes have been done in this round
            finished.append(route)
        # at the end of each round, remove the old entries (without the added node) and reset finished.
        for f in finished:
            routes.remove(f)
        finished = []
        #print(complete_routes)
    return complete_routes

print(visited_twice(['start', 'A', 'c', 'A', 'b', 'A']))

routes = find_routes(nodes)
print(len(routes))

