# pos 0: modes + opcode: mode par3, mode par2, mode par1, two-digit opcode (leading zeros)
# pos 1: position first input value
# pos 2: position second input value
# pos 3: position output value

# mode 0: position mode
# mode 1: immediate mode (value)

# opcode 1: instruction length 4 (add 1 and 2, store at position in 3)
# opcode 2: instruction length 4 (multiply 1 and 2, store at position in 3)
# opcode 3: instruction length 2 (store input at position in 1)
# opcode 4: instruction length 2 (output value at position in 1)
# opcode 99: instruction length 1 (finish)

# 1002,4,3,4
# opcode 2 (multiply), parameter modes 0, 1, 0
#

def parse_code(filename):
    with open(filename) as f:
        code = f.read().split(",")
    for i in range(len(code)):
        code[i] = int(code[i])
    return code

# 0 - opcode (1 = add, 2 = multiply, 99 = stop)
# 1 - pos int1
# 2 - pos int2
# 3 - position to store result

class Parameter(object):

    def __init__(self, value, mode):
        self.value = value
        self.mode = mode

    def __str__(self):
        if self.value is None:
            return("None")
        else:
            return("Value: " + str(self.value) + " Mode:" + str(self.mode))

class Intcode(object):

    def __init__(self, code):
        # intcode program has code, an copy of the original, unmodified code, and a pointer.
        self.original_code = code
        self.code = code.copy()
        self.pointer = 0
        self.par1 = Parameter(None, None)
        self.par2 = Parameter(None, None)
        self.par3 = Parameter(None, None)
        self.input = None
        self.output = []

    def __str__(self):
        par1 = str(self.par1)
        par2 = str(self.par2)
        par3 = str(self.par3)

        string = """
        opcode: {0}
        par1: {1}
        par2: {2}
        par3: {3}
        """.format(str(self.opcode), par1, par2, par3)
        return string

    def read_instruction(self):
        # method to read the more complex instructions that include paramaters and modes.
        # until now max 3 parameters are possible so read 4 positions (opcode + pars)
        # first read opcode to know how many parameters there should be.
        extended_opcode = str(self.code[self.pointer]).zfill(5)
        self.opcode = int(extended_opcode[-2:])
        # opcodes with 3 parameters
        if self.opcode in [1, 2]:
            modes = [int(extended_opcode[2]), int(extended_opcode[1]), int(extended_opcode[0])]
            values = self.code[self.pointer+1:self.pointer+4]
            self.par1 = Parameter(values[0], modes[0])
            self.par2 = Parameter(values[1], modes[1])
            self.par3 = Parameter(values[2], modes[2])

        # opcodes with 1 parameter
        elif self.opcode in [3, 4]:
            mode = int(extended_opcode[0])
            value = self.code[self.pointer+1]
            self.par1 = Parameter(value, mode)
            self.par2 = Parameter(None, None)
            self.par3 = Parameter(None, None)

        # other (for now only 99, which has 0 parameters)
        else:
            self.par1 = Parameter(None, None)
            self.par2 = Parameter(None, None)
            self.par3 = Parameter(None, None)
        print(self)


    def add(self):
        # method to be carried out if opcode == 1
        # uses three parameters to find two values and write their sum to a third position.
        target = self.par3.value
        p1 = self.par1.value if self.par1.mode == 1 else self.code[self.par1.value]
        p2 = self.par2.value if self.par2.mode == 1 else self.code[self.par2.value]
        summed = p1 + p2
        print("added", p1, "and", p2)
        self.code[target] = summed
        print("inserted", summed, "at position", target)
        self.pointer += 4

    def multiply(self):
        # method to be carried out if opcode == 2
        # uses three parameters to find two values and write their product to a third position.
        target = self.par3.value
        # immediate vs position mode
        p1 = self.par1.value if self.par1.mode == 1 else self.code[self.par1.value]
        p2 = self.par2.value if self.par2.mode == 1 else self.code[self.par2.value]
        product = p1 * p2
        print("multiplied", p1, "by", p2)
        self.code[target] = product
        print("inserted", product, "at position", target)
        self.pointer += 4

    def op3(self):
        # takes a single integer as input and saves it to the position given by its only parameter.
        # For example, the instruction 3,50 would take an input value and store it at address 50.
        self.code[self.par1.value] = self.input
        print("inserted input value (" + str(self.input) + ") at position " + str(self.par1.value))
        self.pointer += 2

    def op4(self):
        # outputs the value of its only parameter.
        # For example, the instruction 4,50 would output the value at address 50.
        if self.par1.mode == 0:
            self.output.append(self.code[self.par1.value])
        elif self.par1.mode == 1:
            self.output.append(self.par1.value)
        print(self.output[-1])
        self.pointer += 2


    def run(self, input=None, value1=None, value2=None, reset=True):
        # this method runs the program, taking two optional start values as input.
        # whether or not the state of the intcode program should be preserved can be specified with the reset argument.
        if value1 is not None:
            self.code[1] = value1
        if value2 is not None:
            self.code[2] = value2
        self.execute(input=input)

    def execute(self, input=None):
        self.read_instruction()
        self.input = input
        while True:
            if self.opcode == 1:
                self.add()
            elif self.opcode == 2:
                self.multiply()
            elif self.opcode == 3:
                self.op3()
            elif self.opcode == 4:
                self.op4()
            elif self.opcode == 99:
                return self.code[0]
            self.read_instruction()

### Parameters that an instruction writes to will never be in immediate mode.

# code_day2 = parse_code('C:/Users/Admin/Documents/Code/advent_of_code/2019/2/input.txt')
# day2 = Intcode(code_day2)
# assert day2.run(12, 2) == 3101878

# code_day2 = parse_code('C:/Users/Admin/Documents/Code/advent_of_code/2019/5/testinput2.txt')
# day2 = Intcode(code_day2)
# day2.run()
# print(day2.code)

# testcode_day5 = parse_code('C:/Users/Admin/Documents/Code/advent_of_code/2019/5/testinput.txt')
# day5test = Intcode(testcode_day5)
# print(day5test.code)
# assert day5test.code == [1002, 4, 3, 4, 33]
# day5test.run()
# print(day5test.code)
# assert day5test.code == [1002, 4, 3, 4, 99]



code_day5 = parse_code('C:/Users/Admin/Documents/Code/advent_of_code/2019/5/input.txt')
day5 = Intcode(code_day5)
#print(day5.code)
day5.run(input=1)
assert day5.output[-1] == 14155342
#print(day5.code)
