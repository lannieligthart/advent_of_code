import time

startTime = time.time()

input = "193467258"
input = [int(input[i]) for i, cup in enumerate(input)]

class Node:
    def __init__(self, label):
        self.label = label
        self.next = None

    def __repr__(self):
        return str(self.label)

class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        self.cups = {} # dictionary to store cups in
        if nodes is not None:
            node = Node(label=nodes.pop(0))
            self.cups[node.label] = node
            self.head = node
            for elem in nodes:
                node.next = Node(label=elem)
                node = node.next
                self.cups[node.label] = node
        # make it a circular list by connecting head and tail
        node.next = self.head

    def __repr__(self):
        node = self.cups[1]
        nodes = []
        for _ in range(len(self.cups)):
            nodes.append(str(node.label))
            node = node.next
        return "".join(nodes)

    def remove(self, last):
        self.head.next = self.cups[last].next

    def insert_after(self, dest, first, last):
        after = self.cups[dest].next
        self.cups[dest].next = self.cups[first]
        self.cups[last].next = after

    def play(self):
        # pick three cups after current
        first = self.head.next.label
        mid = self.head.next.next.label
        last = self.head.next.next.next.label
        if self.head.label == 1:
            dest = len(self.cups)
        else:
            dest = self.cups[self.head.label - 1].label
        while dest in [first, mid, last]:
            dest -= 1
            if dest == 0:
                dest = len(self.cups)
        self.remove(last)
        self.insert_after(dest, first, last)
        #print("cups:", self)
        #print("current:", self.head)
        #print("pick up:", first, mid, last)
        #print("destination:", dest)
        self.head = self.head.next

ll = LinkedList(nodes=input)

for _ in range(100):
    ll.play()

result = str(ll)[1:]

print(result)

assert result == "25468379"