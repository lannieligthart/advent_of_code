# pos 0: opcode: mode par3, mode par2, mode par3, two-digit opcode (leading zeros)
# pos 1: position first input value
# pos 2: position second input value
# pos 3: position output value



def add_ints(ints, program):
    sum = program[ints[1]] + program[ints[2]]
    program[ints[3]] = sum
    #print("inserted", sum, "at position", ints[3])

def multiply_ints(ints, program):
    product = program[ints[1]] * program[ints[2]]
    program[ints[3]] = product
    #print("inserted", product, "at position", ints[3])

def run_intcode(program, value1, value2):
    tmp_program = program.copy()
    tmp_program[1] = value1
    tmp_program[2] = value2
    pos = 0
    while True:
        ints = tmp_program[pos:pos+4]
        if ints[0] == 99:
            break
        elif ints[0] == 1:
            add_ints(ints, tmp_program)
            pos += 4
        elif ints[0] == 2:
            multiply_ints(ints, tmp_program)
            pos += 4
        else:
            raise ValueError("invalid intcode!")
    return tmp_program[0]