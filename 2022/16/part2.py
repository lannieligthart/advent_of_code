from AoC_tools.aoc22 import *
from itertools import permutations, combinations
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

    def __init__(self, node1, node2, path1, path2, flow, score, minutes_left1, minutes_left2, nodes_left):
        self.node1 = node1
        self.node2 = node2
        self.nodes_left = nodes_left
        self.path1 = path1
        self.path2 = path2
        self.minutes_left1 = minutes_left1
        self.minutes_left2 = minutes_left2
        self.flow = flow
        self.score = score

    @property
    # calculate the theoretical potential of the unvisited nodes if they were all opened at once, as an indicator of
    # how good each option is. Assume we do this for the player with the most minutes left.
    def potential(self):
        minutes_left = max(self.minutes_left1, self.minutes_left2)
        potential = 0
        for n in self.nodes_left:
            potential += flows[n] * minutes_left
        return potential

    def __gt__(self, other):
        return self.score > other.score

    def __lt__(self, other):
        return self.score < other.score

    def __str__(self):
        string = f"Path 1: {', '.join(self.path1)}; Path 2: {', '.join(self.path2)}; Score: {self.score}; Score + potential: {self.score + self.potential}; "
        return string


def get_new_state(current_state, visited_node1, visited_node2):
    path1 = current_state.path1.copy()
    path2 = current_state.path2.copy()
    minutes_left1 = current_state.minutes_left1 - (shortest_path[(current_state.node1, visited_node1)])
    minutes_left2 = current_state.minutes_left2 - (shortest_path[(current_state.node2, visited_node2)])
    nodes_left = current_state.nodes_left.copy()
    if minutes_left1 > 0:
        path1.append(visited_node1)
        nodes_left.remove(visited_node1)
    if minutes_left2 > 0:
        path2.append(visited_node2)
        nodes_left.remove(visited_node2)
    flow = current_state.flow + flows[visited_node1] + flows[visited_node2]


    score = current_state.score + flows[visited_node1] * minutes_left1 + flows[visited_node2] * minutes_left2
    return State(visited_node1, visited_node2, path1, path2, flow, score, minutes_left1, minutes_left2, nodes_left)


data = read_input("testinput.txt")
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
sorted_print(flows, by='value')

relevant_nodes = [key for key, value in flows.items() if value > 0]
begin_state = State(node1='AA', node2='AA', path1=['AA'], path2=['AA'], flow=0, score=0, minutes_left1=26, minutes_left2=26, nodes_left=relevant_nodes)

q = PriorityQueue()
q.put((begin_state.score, begin_state))
max_score = begin_state.score

while not q.empty():
    # haal een state op
    current_state = q.get()[1]
    # maak alle mogelijke combinaties van 2 toe te voegen nodes en voeg die in beide volgordes aan de state toe.
    node_combos = list(combinations(current_state.nodes_left, 2))
    # loop de nodes langs die in deze state nog over zijn en bepaal voor elke combi van 2 nodes een nieuwe state.
    for nc in node_combos:
        combo1 = nc
        combo2 = (nc[1], nc[0])
        for c in [combo1, combo2]:
            #print(f"adding {visited_node} to {current_state.node}")
            new_state = get_new_state(current_state, c[0], c[1])
            if new_state.score + new_state.potential > max_score:
                #print(f"Max score: {max_score}; keeping {new_state}")
                q.put((-1 * (new_state.score + new_state.potential), new_state))
            #else:
             #   print(f"Max score: {max_score}; discarding {new_state}")
            if new_state.score > max_score:
                max_score = new_state.score
                print(f"Max score: {max_score}; keeping {new_state}")
                print(f"New max score: {max_score}")
                print(len(q.queue))
    #print(len(q.queue))

print(f"max score: {max_score}")

#path = ['AA', 'DD', 'BB', 'JJ', 'HH', 'EE', 'CC']



#2063 too low
