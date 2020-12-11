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
        self.original_code = code
        self.code = code.copy()
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

    def run(self, value1=None, value2=None, reset=True):
        # change start values, if necessary
        if value1 is not None:
            self.code[1] = value1
        if value2 is not None:
            self.code[2] = value2
        while True:
            if self.opcode == 99:
                # reset pointer and (optionally) program code
                result = self.code[0]
                self.pointer = 0
                if reset:
                    self.code = self.original_code.copy()
                return result
            elif self.opcode == 1:
                self.add()
            elif self.opcode == 2:
                self.multiply()
            else:
                print("invalid opcode!")
                return None

program = Intcode(code)
print(program.run(12, 2))
assert program.run(12, 2) == 3101878

def get_verb_and_noun(program):
    for i in range(100):
        for j in range(100):
            print(i, j)
            if program.run(i, j) == 19690720:
                return(100*i + j)

result = (get_verb_and_noun(program))
print(result)

assert program.run(12, 2) == 3101878
assert program.run(84, 44) == 19690720
assert result == 8444



