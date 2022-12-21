from AoC_tools.aoc22 import read_input


class Monkey(object):

    def __init__(self, name, name1=None, name2=None, operator=None, numeric_name=None):
        self.name = name
        self.name1 = name1
        self.name2 = name2
        self.operator = operator
        self.numeric_name = numeric_name

    def get_number(self):
        if self.numeric_name is not None:
            return self.numeric_name
        else:
            return int(eval(str(monkeys[self.name1].get_number()) + self.operator + str(monkeys[self.name2].get_number())))

    @property
    def is_equal(self):
        if monkeys[self.name1].get_number() == monkeys[self.name2].get_number():
            return True
        else:
            return False


data = read_input("input.txt", "\n", ": ")

monkeys = dict()

for d in data:
    if len(d[1].split()) == 3:
        monkeys[d[0]] = Monkey(name=d[0], name1=d[1].split()[0], name2=d[1].split()[2], operator=d[1].split()[1])
    else:
        monkeys[d[0]] = Monkey(name=d[0], numeric_name=int(d[1]))

assert monkeys["root"].get_number() == 299983725663456


