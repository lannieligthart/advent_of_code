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
            result = self.numeric_name
        else:
            result = int(eval(str(monkeys[self.name1].get_number()) + self.operator + str(monkeys[self.name2].get_number())))
        return result

    def set_number(self, number):
        self.numeric_name = number

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
        monkeys[d[0]] = Monkey(name=d[0], name1= d[1].split()[0], name2=d[1].split()[2], operator=d[1].split()[1])
    else:
        monkeys[d[0]] = Monkey(name=d[0], numeric_name=(d[1]))

i = 0

# start checking at very large interval
interval = 10000000000000
while True:
    monkeys["humn"].set_number(i)
    if monkeys["root"].is_equal:
        break
    # once number 2 gets larger than number 1, make the interval smaller and start checking from the previous i
    if monkeys[monkeys["root"].name1].get_number() < monkeys[monkeys["root"].name2].get_number():
        interval = interval / 10
        i = last_checked
    last_checked = i
    i += interval

assert int(i) == 3093175982595