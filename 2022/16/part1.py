from AoC_tools.aoc22 import *
from itertools import combinations
from queue import PriorityQueue


def find_shortest_path(graph, start, goal):
    visited = []
    queue = [[start]]
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in visited:
            neighbours = graph[node]
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                if neighbour == goal:
                    return len(new_path)
            visited.append(node)


class State(object):

    def __init__(self, node, path, flow, score, minutes_left, nodes_left):
        self.node = node
        self.path = path
        self.flow = flow
        self.score = score
        self.minutes_left = minutes_left
        self.nodes_left = nodes_left

    @property
    # calculate the theoretical potential of the unvisited nodes if they were all opened at once, as an indicator of
    # how good each option is
    def potential(self):
        potential = 0
        for n in self.nodes_left:
            potential += flows[n] * self.minutes_left
        return potential

    def __gt__(self, other):
        return self.node > other.node

    def __lt__(self, other):
        return self.node < other.node

    def __str__(self):
        string = f"{', '.join(self.path)}; Score: {self.score}"
        return string


def get_new_state(current_state, visited_node):
    path = current_state.path.copy()
    minutes_left = current_state.minutes_left - (shortest_path[(current_state.node, visited_node)])
    path.append(visited_node)
    flow = current_state.flow + flows[visited_node]
    nodes_left = current_state.nodes_left.copy()
    nodes_left.remove(visited_node)
    score = current_state.score + flows[visited_node] * minutes_left
    return State(visited_node, path, flow, score, minutes_left, nodes_left)


data = read_input("input.txt")
data = [d.replace("Valve ", "") for d in data]
data = [d.replace(" has flow rate=", ", ") for d in data]
data = [d.replace("; tunnels lead to valves ", ", ") for d in data]
data = [d.replace("; tunnels lead to valve ", ", ") for d in data]
data = [d.replace("; tunnel leads to valve ", ", ") for d in data]
data = [d.split(", ") for d in data]

graph = dict()
for d in data:
    graph[d[0]] = []
    nb = d[2:]
    for n in nb:
        graph[d[0]].append(n)

shortest_path = dict()
combos = list(combinations(graph.keys(), 2))

for c in combos:
    c1, c2 = c
    shortest_path[c1, c2] = find_shortest_path(graph, *c)
    shortest_path[c2, c1] = find_shortest_path(graph, *c)

flows = dict()
for d in data:
    flows[d[0]] = int(d[1])

relevant_nodes = [key for key, value in flows.items() if value > 0]
begin_state = State(node='AA', path=['AA'], flow=0, score=0, minutes_left=30, nodes_left=relevant_nodes)

q = PriorityQueue()

q.put((begin_state.score, begin_state))
max_score = begin_state.score

while not q.empty():
    current_state = q.get()[1]
    for visited_node in current_state.nodes_left:
        new_state = get_new_state(current_state, visited_node)
        if new_state.score + new_state.potential >= max_score:
            q.put((-1 * new_state.score, new_state))
        if new_state.score > max_score:
            max_score = new_state.score

print(f"max score: {max_score}")

assert max_score == 1474

