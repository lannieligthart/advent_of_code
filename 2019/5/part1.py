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

with open('C:/Users/Admin/Documents/Code/advent_of_code/2019/2/input.txt') as f:
    data = f.read().split(",")

for i in range(len(data)):
    data[i] = int(data[i])


def read_opcode(input):
    input = str(input)
    # last two numbers are the opcode itself (incl. leading zero)
    opcode = int(input[-2:])
    if opcode not in [1, 2, 3, 4, 99]:
        raise ValueError(str(opcode) + " is an invalid opcode!")
    # opcodes with no parameters:
    if opcode == 99:
        if len(input) > 2:
            raise ValueError("no parameters expected for opcode " + str(opcode))
        return(opcode)
    # opcodes with only one parameter:
    if opcode in [3, 4] and len(input) > 3:
        raise ValueError("invalid input, expecting only one parameter!")
    # opcodes with at least one parameter:
    if opcode in [1, 2, 3, 4]:
        mode1 = 0
        # if the input is longer than the opcode (including leading zero),
        # read in first parameter
        if len(input) > 2:
            mode1 = int(input[-3])
        if opcode in [3, 4]:
            return (opcode, mode1)
    # opcodes with 3 parameters
    if opcode in [1, 2]:
        mode2 = 0
        # if the input is longer than the opcode plus first parameter,
        # read in second parameter
        if len(input) > 3:
            mode2 = int(input[-4])
        mode3 = 0
        # same for third param
        if len(input) > 4:
            mode3 = int(input[-5])
        return (opcode, mode1, mode2, mode3)

def add_ints(ints, program):
    sum = program[ints[1]] + program[ints[2]]
    program[ints[3]] = sum
    #print("inserted", sum, "at position", ints[3])

def multiply_ints(ints, program):
    product = program[ints[1]] * program[ints[2]]
    program[ints[3]] = product
    #print("inserted", product, "at position", ints[3])

def run_intcode(program, value1=None, value2=None):
    code = program.copy()
    #tmp_program[1] = value1
    #tmp_program[2] = value2
    pos = 0
    while True:
        ints = code[pos:pos+4]
        if ints[0] == 99:
            break
        elif ints[0] == 1:
            add_ints(ints, code)
            pos += 4
        elif ints[0] == 2:
            multiply_ints(ints, code)
            pos += 4
        else:
            raise ValueError("invalid intcode!")
    return tmp_program[0]


assert read_opcode(1002) == (2, 0, 1, 0)
assert read_opcode(1101) == (1, 1, 1, 0)
assert read_opcode(103) == (3, 1)
assert read_opcode(3) == (3, 0)
#assert read_opcode(11003) == (3, 0)
assert read_opcode(104) == (4, 1)
assert read_opcode('004') == (4, 0)
assert read_opcode(4) == (4, 0)
