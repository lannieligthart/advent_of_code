from AoC_tools.aoc22 import *
from itertools import permutations, combinations
from queue import PriorityQueue

def find_shortest_path(graph, start, goal):
    visited = []
    queue = [[start]]
    while queue:
        path = queue.pop(0)
        node = path[-1]

        # Condition to check if the
        # current node is not visited
        if node not in visited:
            neighbours = graph[node]

            # Loop to iterate over the neighbours of the node
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                if neighbour == goal:
                    # path is tijd die het kost om er te komen plus de tijd die het kost om hem open te draaien
                    return len(new_path)
            visited.append(node)

def get_flow_release(path):
    path_length = 0
    flow_release = 0
    for i in range(len(path) - 1):
        #path_length = shortest_path[(path[i], path[i+1])] + path_length
        flow_release += (30 - shortest_path[(path[i], path[i+1])] + path_length) * flows[path[i+1]]
    return(flow_release)



class State():

    def __init__(self, node, path, flow, score, minutes_left, nodes_left):
        self.node = node
        self.path = path
        self.flow = flow
        self.score = score
        self.minutes_left = minutes_left
        self.nodes_left = nodes_left

    @property
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
    # if path == ['AA', 'DD', 'BB', 'JJ', 'HH', 'EE']:
    # minutes left is vorige minutes left min shortest path
    minutes_left = current_state.minutes_left - (shortest_path[(current_state.node, visited_node)])
    path.append(visited_node)
    flow = current_state.flow + flows[visited_node]
    nodes_left = current_state.nodes_left.copy()
    nodes_left.remove(visited_node)
    # de score is de vorige + wat erbij komt dankzij de nieuwe node
    score = current_state.score + flows[visited_node] * minutes_left
    # calculate the theoretical potential of the unvisited nodes
    potential = 0
    for n in nodes_left:
        potential += flows[n] * minutes_left
    return State(visited_node, path, flow, score, minutes_left, nodes_left)



data = read_input("input.txt")

data = [d.replace("Valve ", "") for d in data]
data = [d.replace(" has flow rate=", ", ") for d in data]
data = [d.replace("; tunnels lead to valves ", ", ") for d in data]
data = [d.replace("; tunnels lead to valve ", ", ") for d in data]
data = [d.replace("; tunnel leads to valve ", ", ") for d in data]
data = [d.split(", ") for d in data]
#print(data)

graph = dict()
for d in data:
    graph[d[0]] = []
    nb = d[2:]
    for n in nb:
        #print(f"add connection {c} to node {d[0]} ")
        graph[d[0]].append(n)

shortest_path = dict()
combos = list(combinations(graph.keys(), 2))

for c in combos:
    c1, c2 = c
    shortest_path[c1, c2] = find_shortest_path(graph, *c)
    shortest_path[c2, c1] = find_shortest_path(graph, *c)


#dprint(graph)

flows = dict()
for d in data:
    flows[d[0]] = int(d[1])

sorted_print(flows, by='value')

relevant_nodes = [key for key, value in flows.items() if value > 0]


max_flow = 0
begin_state = State(node='AA', path=['AA'], flow=0, score=0, minutes_left=30, nodes_left=relevant_nodes)
print(begin_state.potential)

# new_state = get_new_state(begin_state, 'BB')
# #
# assert new_state.flow == 13
# assert new_state.path == ['AA', 'BB']
# assert len(new_state.nodes_left) == 5
# assert new_state.minutes_left == 28
# assert new_state.potential == 28 * 2 + 28 * 20 + 28 * 3 + 28 * 22 + 28 * 21
# assert new_state.node == 'BB'
# assert new_state.score == 364
# #
# new_state = get_new_state(new_state, 'CC')
# #
# assert new_state.flow == 15
# assert new_state.path == ['AA', 'BB', 'CC']
# assert len(new_state.nodes_left) == 4
# assert new_state.minutes_left == 26
# assert new_state.potential == 26 * 20 + 26 * 3 + 26 * 22 + 26 * 21
# assert new_state.node == 'CC'
# assert new_state.score == 416

q = PriorityQueue()

q.put((begin_state.score, begin_state))
max_score = begin_state.score

while not q.empty():
    # haal een state op
    current_state = q.get()[1]
    #print(f"current state: {current_state}")
    # loop de nodes langs die in deze state nog over zijn en bepaal voor elke een nieuwe state.
    # voeg al deze states toe aan de queue.
    for visited_node in current_state.nodes_left:
        #print(f"adding {visited_node} to {current_state.node}")
        new_state = get_new_state(current_state, visited_node)
        if new_state.score + new_state.potential >= max_score:
            q.put((-1 * new_state.score, new_state))
        if new_state.score > max_score:
            max_score = new_state.score
        #else:
            #print(f"discarding state {new_state}")
    print(len(q.queue))

print("max score:")
print(max_score)

#path = ['AA', 'DD', 'BB', 'JJ', 'HH', 'EE', 'CC']




# 32760 too high
# 1458 too low
# 2088 too high