from AoC_tools import aoc22 as aoc
from collections import defaultdict, deque

start_time = aoc.start()


def in_data(pos, data):
    r, c = pos
    if 0 <= r < len(data) and c >= 0 and c < len(data[0]):
        return True
    else:
        return False

def find_nodes(data):
    finish = (len(data)-1, len(data[0])-2)
    start_pos = (0, 1)
    queue = [start_pos]
    visited = [start_pos]
    nodes = [start_pos]
    while len(queue) > 0:
        # Take a path from the queue. Follow path until there is a split, and add the position preceding the split to
        # list of nodes.
        current = queue.pop(0)
        while True:
            visited.append(current)
            r, c = current
            # find out where we can go from here
            nb = [(r-1, c), (r, c+1), (r+1, c), (r, c-1)]  # n, e, s, w
            options = []
            for i, n in enumerate(nb):
                if in_data(n, data) and data[n[0]][n[1]] in [".", "^", ">", "v", "<"] and n not in visited:
                    options.append(n)
            # if there are no more options, discard path by breaking
            if len(options) == 0:
                break
            # if there is one option, add new position to visited and update the current position and distance
            if len(options) == 1:
                # update current node
                current = options[0]
                if options[0] == finish:
                    nodes.append(options[0])
                    break
            # als er meer dan 1 optie is: voeg de node toe aan nodes dict en zet 2 nieuwe paden in de queue.
            elif len(options) > 1:
                # add node to dictionary
                nodes.append(current)
                visited.append(current)
                for o in options:
                    if o == finish:
                        nodes.append = o
                        break
                    else:
                        queue.append(o)
                break
    return nodes


def find_distances(node, nodes, distances, data):
    """
    Start from first node. Walk in all possible directions until you find another node, while keeping track of distance.
    Once you find a node, record the distance and register distance in a dict: graph[('A', 'B')] = dist
    Do this for all nodes.
    """
    visited = [nodes[node]]
    # (node position, distance)
    queue = [(nodes[node], 0)]
    while len(queue) > 0:
        pos, dist = queue.pop(0)
        r, c = pos
        # find out where we can go from here
        nb = [(r - 1, c), (r, c + 1), (r + 1, c), (r, c - 1)]  # n, e, s, w
        options = []
        for i, n in enumerate(nb):
            if in_data(n, data) and data[n[0]][n[1]] in [".", "^", ">", "v", "<"] and n not in visited:
                options.append(n)
        dist += 1
        for o in options:
            visited.append(o)
            if o in nodes.values():
                for key, value in nodes.items():
                    if value == o:
                        other_node = key
                new_key = tuple(sorted([node, other_node]))
                if new_key not in distances:
                    distances[new_key] = dist
            else:
                queue.append((o, dist))

def find_all_paths(start, finish, graph, distances):
    """Begin met startpunt. Ga naar elk mogelijk punt vanaf daar. Voeg elk pad wat hieruit resulteert toe aan de queue.
     Voor elk pad in de queue, neem elk mogelijk vervolgpunt dat nog niet in het pad zit. Als er geen mogelijkheden meer zijn,
     discard. Als je eindpunt bereikt, voeg pad toe aan resultaten."""
    paths = []
    queue = deque([(start, 0)])
    while len(queue) > 0:
        path, dist = queue.popleft()
        # find options
        options = graph[path[-1]]
        options = [o for o in options if o not in path]
        for o in options:
            newpath = path
            newpath += o
            newdist = dist + distances[tuple(sorted([newpath[-1], newpath[-2]]))]
            if o == finish:
                paths.append((newpath, newdist))
            else:
                queue.append((newpath, newdist))
    return paths

with open("input.txt") as file:
    data = file.read().split("\n")

node_positions = find_nodes(data)
nodes = dict()
names = ''
for i in range(65, 91):
    names += chr(i)
for i in range(97, 123):
    names += chr(i)
for i in range(len(node_positions)):
    nodes[names[i]] = node_positions[i]
start = names[0]
finish = names[i]

distances = dict()
for n in nodes:
    find_distances(n, nodes, distances, data)

# create a graph
graph = defaultdict(list)
for key in distances.keys():
    graph[key[0]].append(key[1])
    graph[key[1]].append(key[0])


paths = find_all_paths(start, finish, graph, distances)
maxlen = max([p[1] for p in paths])

assert maxlen == 6522
#assert maxlen == 154

aoc.end(start_time)
