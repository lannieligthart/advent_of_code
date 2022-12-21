from AoC_tools.aoc22 import read_input

class Node(object):

    def __init__(self, id, number):
        self.id = id
        self.number = number
        self.next = None
        self.previous = None


class CircularLinkedList:

    def __init__(self, head):
        self.head = head

    def remove(self):
        node = self.head
        self.head.previous.next  = self.head.next
        self.head.next.previous = self.head.previous
        # stel de volgende node in als head
        self.head = self.head.next
        node.next = None
        node.previous = None
        return node

    def move_forward(self, n):
        for x in range(n):
            self.head = self.head.next

    def move_backward(self, n):
        for x in range(n):
            self.head = self.head.previous

    def insert_before(self, node):
        previous = self.head.previous
        self.head.previous = node
        node.next = self.head
        node.previous = previous
        node.next.previous = node
        previous.next = node

    def move_node(self, steps):
        node = self.remove()
        if steps > 0:
            self.move_forward(steps)
        elif steps < 0:
            self.move_backward(abs(steps))
        self.insert_before(node)


data = read_input("input.txt", "\n")
data = list(map(int, data))

# create nodes
nodes = []
for i, d in enumerate(data):
    nodes.append(Node(i, data[i]))

# link nodes
for i, d in enumerate(data):
    nodes[i].previous = nodes[i-1]
    nodes[i].next = nodes[(i+1) % len(data)]

cll = CircularLinkedList(head=nodes[0])

# mix
for i in range(len(data)):
    cll.head = nodes[i]
    cll.move_node(data[i])

cll.head = nodes[data.index(0)]
coordinates = []
for i in range(3):
    cll.move_forward(1000)
    coordinates.append(cll.head.number)

assert sum(coordinates) == 19070