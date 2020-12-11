with open('C:/Users/Admin/Documents/Code/advent_of_code/2019/2/input.txt') as f:
    code = f.read().split(",")

for i in range(len(code)):
    code[i] = int(code[i])

# 0 - opcode (1 = add, 2 = multiply, 99 = stop)
# 1 - pos int1
# 2 - pos int2
# 3 - position to store result

class Intcode():

    def __init__(self, code):
        self.code = code
        self.pointer = 0

    @property
    def parameters(self):
        p1 = None
        p2 = None
        p3 = None
        if self.opcode in [1, 2]:
            try:
                p1 = self.code[self.pointer + 1]
                p2 = self.code[self.pointer + 2]
                p3 = self.code[self.pointer + 3]
            except IndexError:
                pass
        elif self.opcode == 99:
            pass
        pars = (p1, p2, p3)
        return pars

    @property
    def opcode(self):
        return self.code[self.pointer]

    def add(self):
        # opcode 1
        target = self.parameters[2]
        summed = self.code[self.parameters[0]] + self.code[self.parameters[1]]
        self.code[target] = summed
        print("inserted", summed, "at position", target)
        self.pointer += 4

    def multiply(self):
        # opcode 2
        target = self.parameters[2]
        product = self.code[self.parameters[0]] * self.code[self.parameters[1]]
        self.code[target] = product
        print("inserted", product, "at position", target)
        self.pointer += 4

    def run(self, value1=None, value2=None):
        # change start values, if necessary
        if value1 is not None:
            self.code[1] = value1
        if value2 is not None:
            self.code[2] = value2
        while True:
            if self.opcode == 99:
                return self.code[0]
            elif self.opcode == 1:
                self.add()
            elif self.opcode == 2:
                self.multiply()
            else:
                print("invalid opcode!")
                return None

program = Intcode(code)
assert program.run(12, 2) == 3101878
