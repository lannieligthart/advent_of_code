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

import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.DEBUG)

def parse_code(filename):
    with open(filename) as f:
        code = f.read().split(",")
    code = {i: int(code[i]) for i in range(0, len(code))}
    return code

def parse(code):
    code = code.split(",")
    code = {i: int(code[i]) for i in range(0, len(code))}
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
        self.relative_base = 0
        self.output = []
        self.round = 0

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
        return

    def translate(self, par):
        # 0 = position mode
        # 1 = immediate mode
        # 2 = relative mode
        if par.value is not None:
            # if the position does not exist yet, initialize it at zero.
            # do the same for this position plus the relative base.
            if par.mode == 0:
                if not par.value in self.code and par.value >= 0:
                    self.code[par.value] = 0
                pt = self.code[par.value]
            elif par.mode == 1:
                pt = par.value
            elif par.mode == 2:
                if not par.value in self.code and par.value >= 0:
                    self.code[par.value + self.relative_base] = 0
                pt = self.code[par.value + self.relative_base]
        else:
            pt = None
        return pt

    def translate_literal(self, par):
        if par.mode == 0 or par.mode == 1:
            pt = par.value
        if par.mode == 2:
            pt = par.value + self.relative_base
        return pt

    def add(self):
        # method to be carried out if opcode == 1
        # uses three parameters to find two values and write their sum to a third position.
        p1 = self.translate(self.par1)
        p2 = self.translate(self.par2)
        p3 = self.translate_literal(self.par3)
        summed = p1 + p2

        logging.debug(f"added {p1} and {p2}")
        # note: p3 should be the value! do not interpret mode or tests will fail.
        self.code[p3] = summed
        logging.debug(f"inserted {summed} at position {p3}")


    def multiply(self):
        # method to be carried out if opcode == 2
        # uses three parameters to find two values and write their product to a third position.
        p3 = self.translate_literal(self.par3)
        # immediate vs position mode
        p1 = self.translate(self.par1)
        p2 = self.translate(self.par2)
        product = p1 * p2
        logging.debug(f"multiplied {p1} by {p2}")
        self.code[p3] = product
        logging.debug(f"inserted {product} at position {p3}")


    def op3(self, input):
        p1 = self.translate_literal(self.par1)
        logging.debug(f"save input to position {p1}")
        # takes a single integer as input and saves it to the position given by its only parameter.
        # For example, the instruction 3,50 would take an input value and store it at address 50.
        self.code[p1] = input
        logging.debug(f"inserted input value ({input}) at position {p1}")

    def op4(self):
        # outputs the value of its only parameter (translated! otherwise tests fail).
        # For example, the instruction 4,50 would output the value at address 50.
        p1 =self.translate(self.par1)
        logging.debug(f"return value {p1}")
        return p1

    def op5(self):
        logging.debug(f"jump if p1 is non-zero")
        # jump-if-true: if the first parameter is non-zero, it sets the instruction pointer to the value from the second
        # parameter. Otherwise, it does nothing.
        p1 =self.translate(self.par1)
        p2 =self.translate(self.par2)
        if not p1 == 0:
            self.pointer = p2
            logging.debug(f"set pointer at position {p2}")


    def op6(self):
        logging.debug(f"jump if p1 is zero")
        # jump-if-false: if the first parameter is zero, it sets the instruction pointer to the value from the second
        # parameter. Otherwise, it does nothing.
        p1 =self.translate(self.par1)
        p2 =self.translate(self.par2)
        if p1 == 0:
            self.pointer = p2
            logging.debug(f"set pointer at position {p2}")


    def op7(self):
        # less than: less than: if the first parameter is less than the second parameter, it stores 1 in the position
        # given by the third parameter. Otherwise, it stores 0.
        p1 =self.translate(self.par1)
        p2 =self.translate(self.par2)
        p3 = self.translate_literal(self.par3)

        logging.debug(f"if p1 < p2, store 1 in position p3 ({p3}), otherwise store 0")
        if p1 < p2:
            self.code[p3] = 1
            logging.debug(f"inserted value 1 at position {p3}")
        else:
            self.code[p3] = 0
            logging.debug(f"inserted value 0 at position {p3}")

    def op8(self):
        # equals: if the first parameter is equal to the second parameter, it stores 1 in the position given by the
        # third parameter. Otherwise, it stores 0.
        p1 =self.translate(self.par1)
        p2 =self.translate(self.par2)
        p3 = self.translate_literal(self.par3)
        logging.debug(f"if p1 == p2, store 1 in position p3 ({p3}), otherwise store 0.")
        if p1 == p2:
            self.code[p3] = 1
            logging.debug(f"inserted value 1 at position {p3}")
        else:
            self.code[p3] = 0
            logging.debug(f"inserted value 0 at position {p3}")

    def op9(self):
        p1 =self.translate(self.par1)
        logging.debug(f"adding {p1} to relative base")
        self.relative_base += p1

    def run(self, input=None, value1=None, value2=None, reset=True, return_last=False, halt_on_output=False):
        self.round += 1
        # this method runs the program, taking two optional start values as input.
        # whether or not the state of the intcode program should be preserved can be specified with the reset argument.
        if reset:
            self.code = self.original_code.copy()
            self.pointer = 0
            self.output = []

        # set start values
        if value1 is not None:
            self.code[1] = value1
        if value2 is not None:
            self.code[2] = value2
        self.read_instruction()

        while True:
            if self.opcode == 1:
                self.add()
            elif self.opcode == 2:
                self.multiply()
            elif self.opcode == 3:
                if input is not None:
                    self.op3(input)
                    # reset input to None to avoid using it again when next input is required
                    input = None
                else:
                    # move pointer backwards so that upon the next run, it picks up where input is needed
                    self.pointer -= 2
                    return "need input"

            elif self.opcode == 4:
                result = self.op4()
                if result is not None:
                    if halt_on_output:
                        return result
                    else:
                        self.output.append(result)
                    logging.debug(f"Output: {self.output}")
            elif self.opcode == 5:
                self.op5()
            elif self.opcode == 6:
                self.op6()
            elif self.opcode == 7:
                self.op7()
            elif self.opcode == 8:
                self.op8()
            elif self.opcode == 9:
                self.op9()
            elif self.opcode == 99:
                if return_last or len(self.output) == 1:
                    return self.output[-1]
                elif not return_last and len(self.output) > 0:
                    return self.output
                elif len(self.output) == 0:
                    return None
            self.read_instruction()




"""
run once, 
when input is required, stop and return prompt for input
when output is generated, write it to output list
when end is reached, return output, if any
write wrapper that executes and feeds input when prompted
"""