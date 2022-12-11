import AoC_tools.aoc22 as aoc
from collections import deque


class Monkey(object):

    def __init__(self, items, operation, divisor, test_true, test_false):
        self.items = items
        self.op = operation
        self.divisor = divisor
        self.monkey_true = test_true
        self.monkey_false = test_false
        self.icount = 0

    @classmethod
    def read(cls, data):
        items = deque([int(d) for d in data[1].replace("Starting items: ", "").split(", ")])
        operation = data[2].replace("Operation: new = ", "")
        divisor = int(data[3].replace("Test: divisible by ", ""))
        test_true = int(data[4].replace("If true: throw to monkey ", ""))
        test_false = int(data[5].replace("If false: throw to monkey ", ""))
        return Monkey(items, operation, divisor, test_true, test_false)

    @staticmethod
    def add_item(monkey, item):
        monkey.items.append(item)

    def round(self):
        items = self.items.copy()
        for item in items:
            self.icount += 1
            old = item
            item = eval(self.op)
            item = int(item/3)
            if item % self.divisor == 0:
                self.items.pop()
                self.add_item(monkeys[self.monkey_true], item)
            else:
                self.items.pop()
                self.add_item(monkeys[self.monkey_false], item)

#data = aoc.read_input("testinput.txt", sep1="\n\n", sep2="\n")
data = aoc.read_input("input.txt", sep1="\n\n", sep2="\n")

monkeys = [Monkey.read(monkey) for monkey in data]

for i in range(20):
    for m in monkeys:
        m.round()

counts = [m.icount for m in monkeys]
counts.sort()

# assert counts[-1] * counts[-2] == 9030
assert counts[-1] * counts[-2] == 112815
