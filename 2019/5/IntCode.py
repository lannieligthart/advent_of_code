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
    code = {i: int(code[i]) for i in range(0, len(code))}
    # for i in range(len(code)):
    #     code[i] = int(code[i])
    return code

def parse(code):
    code = code.split(",")
    code = {i: int(code[i]) for i in range(0, len(code))}
    # for i in range(len(code)):
    #     code[i] = int(code[i])
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
        self.relative_base = 0
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

        # reset parameter values
        self.par1 = Parameter(None, None)
        self.par2 = Parameter(None, None)
        self.par3 = Parameter(None, None)

        # read opcode to know how many parameters there should be.
        extended_opcode = str(self.code[self.pointer]).zfill(5)
        self.opcode = int(extended_opcode[-2:])

        # read in new modes and values
        modes = [int(extended_opcode[2]), int(extended_opcode[1]), int(extended_opcode[0])]

        # opcodes with 3 parameters
        if self.opcode in [1, 2, 7, 8]:
            values = [self.code[self.pointer + 1], self.code[self.pointer + 2], self.code[self.pointer + 3]]
            self.par1 = Parameter(values[0], modes[0])
            self.par2 = Parameter(values[1], modes[1])
            self.par3 = Parameter(values[2], modes[2])
            self.pointer += 4

        # # opcodes with 2 parameters
        elif self.opcode in [5, 6]:
            values = [self.code[self.pointer + 1], self.code[self.pointer + 2]]
            self.par1 = Parameter(values[0], modes[0])
            self.par2 = Parameter(values[1], modes[1])
            self.pointer += 3

        # opcodes with 1 parameter
        elif self.opcode in [3, 4, 9]:
            values = [self.code[self.pointer + 1]]
            self.par1 = Parameter(values[0], modes[0])
            self.pointer += 2


    def translate(self):
        # 0 = position mode
        # 1 = immediate mode
        # 2 = relative mode
        if self.par1.value is not None:
            # if the position does not exist yet, initialize it at zero.
            # do the same for this position plus the relative base.
            if self.par1.mode == 0:
                if not self.par1.value in self.code and self.par1.value >= 0:
                    self.code[self.par1.value] = 0
                p1 = self.code[self.par1.value]
            elif self.par1.mode == 1:
                p1 = self.par1.value
            elif self.par1.mode == 2:
                if not self.par1.value in self.code and self.par1.value >= 0:
                    self.code[self.par1.value + self.relative_base] = 0
                p1 = self.code[self.par1.value + self.relative_base]
        else:
            p1 = None
        if self.par2.value is not None:
            if self.par2.mode == 0:
                if not self.par2.value in self.code and self.par2.value >= 0:
                    self.code[self.par2.value] = 0
                p2 = self.code[self.par2.value]
            elif self.par2.mode == 1:
                p2 = self.par2.value
            elif self.par2.mode == 2:
                if not self.par2.value in self.code and self.par2.value >= 0:
                    self.code[self.par2.value + self.relative_base] = 0
                p2 = self.code[self.par2.value + self.relative_base]
        else:
            p2 = None
        if self.par3.value is not None:
            if self.par3.mode == 0:
                if not self.par3.value in self.code and self.par3.value >= 0:
                    self.code[self.par3.value] = 0
                p3 = self.code[self.par3.value]
            elif self.par3.mode == 1:
                p3 = self.par3.value
            elif self.par3.mode == 2:
                if not self.par2.value in self.code and self.par2.value >= 0:
                    self.code[self.par2.value + self.relative_base] = 0
                p3 = self.code[self.par3.value + self.relative_base]
        else:
            p3 = None
        return (p1, p2, p3)

    def add(self, debug):
        # method to be carried out if opcode == 1
        # uses three parameters to find two values and write their sum to a third position.
        p1, p2 = self.translate()[0:2]
        summed = p1 + p2
        if debug:
            print("added", p1, "and", p2)
        # note: p3 should be the value! do not interpret mode or tests will fail.
        self.code[self.par3.value] = summed
        if debug:
            print("inserted", summed, "at position", self.par3.value)


    def multiply(self, debug):
        # method to be carried out if opcode == 2
        # uses three parameters to find two values and write their product to a third position.
        target = self.par3.value
        # immediate vs position mode
        p1, p2 = self.translate()[0:2]
        product = p1 * p2
        if debug:
            print("multiplied", p1, "by", p2)
        self.code[target] = product
        if debug:
            print("inserted", product, "at position", target)


    def op3(self, debug):
        if debug:
            print("save input to position", self.par1.value)
        # takes a single integer as input and saves it to the position given by its only parameter.
        # For example, the instruction 3,50 would take an input value and store it at address 50.
        self.code[self.par1.value] = self.input[0]
        if debug:
            print("inserted input value (" + str(self.input[0]) + ") at position " + str(self.par1.value))
        if len(self.input) > 1:
            self.input = self.input[1:]

    def op4(self, debug):
        # outputs the value of its only parameter (translated! otherwise tests fail).
        # For example, the instruction 4,50 would output the value at address 50.
        p1 = self.translate()[0]
        if debug:
            print("return value", p1)
        return p1

    def op5(self, debug):
        if debug:
            print("jump if p1 is non-zero")
        # jump-if-true: if the first parameter is non-zero, it sets the instruction pointer to the value from the second
        # parameter. Otherwise, it does nothing.
        p1, p2 = self.translate()[0:2]
        if not p1 == 0:
            self.pointer = p2
            if debug:
                print("set pointer at position", p2)


    def op6(self, debug):
        if debug:
            print("jump if p1 is zero")
        # jump-if-false: if the first parameter is zero, it sets the instruction pointer to the value from the second
        # parameter. Otherwise, it does nothing.
        p1, p2 = self.translate()[0:2]
        if p1 == 0:
            self.pointer = p2
            if debug:
                print("set pointer at position", p2)


    def op7(self, debug):
        # less than: less than: if the first parameter is less than the second parameter, it stores 1 in the position
        # given by the third parameter. Otherwise, it stores 0.
        p1, p2, p3 = self.translate()
        if debug:
            print("if p1 < p2, store 1 in position p3 (" + str(p3) + "), otherwise store 0")
        if p1 < p2:
            self.code[self.par3.value] = 1
            if debug:
                print("inserted value 1 at position", self.par3.value)
        else:
            self.code[self.par3.value] = 0
            if debug:
                print("inserted value 0 at position", self.par3.value)

    def op8(self, debug):
        # equals: if the first parameter is equal to the second parameter, it stores 1 in the position given by the
        # third parameter. Otherwise, it stores 0.
        p1, p2, p3 = self.translate()
        if debug:
            print("if p1 == p2, store 1 in position p3 (" + str(p3) + "), otherwise store 0.")
        if p1 == p2:
            self.code[self.par3.value] = 1
            if debug:
                print("inserted value 1 at position", self.par3.value)
        else:
            self.code[self.par3.value] = 0
            if debug:
                print("inserted value 0 at position", self.par3.value)

    def op9(self, debug):
        p1 = self.translate()[0]
        if debug:
            print("adding", p1, "to relative base")
        self.relative_base += p1

    def execute(self, input=None, value1=None, value2=None, reset=True, debug=False):
        # this method runs the program, taking two optional start values as input.
        # whether or not the state of the intcode program should be preserved can be specified with the reset argument.
        if reset:
            self.code = self.original_code.copy()
            self.pointer = 0
            self.output=[]

        # set start values
        if value1 is not None:
            self.code[1] = value1
        if value2 is not None:
            self.code[2] = value2
        self.read_instruction()

        if input is not None and isinstance(input, list):
            self.input = input
        elif input is not None and isinstance(input, int):
            self.input = [input]

        while True:
            if self.opcode == 1:
                self.add(debug)
            elif self.opcode == 2:
                self.multiply(debug)
            elif self.opcode == 3:
                self.op3(debug)
            elif self.opcode == 4:
                result = self.op4(debug)
                if result is not None:
                    self.output.append(result)
                    return 'exit'
            elif self.opcode == 5:
                self.op5(debug)
            elif self.opcode == 6:
                self.op6(debug)
            elif self.opcode == 7:
                self.op7(debug)
            elif self.opcode == 8:
                self.op8(debug)
            elif self.opcode == 9:
                self.op9(debug)
            elif self.opcode == 99:
                return 'exit'
            self.read_instruction()

    def run(self, input=None, value1=None, value2=None, reset=True, debug=False):
        while True:
            tmp = self.execute(input, value1, value2, reset, debug)
            if tmp == 'exit':
                return self.output

### Parameters that an instruction writes to will never be in immediate mode.
