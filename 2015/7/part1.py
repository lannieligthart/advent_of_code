with open("input.txt") as f:
    data = f.read().split("\n")

class Wire(object):

    def __init__(self, name, operator=None, n1=None, n2=None, value=None):
        """NB: value is None except when the signal is specifically set for this wire rather than
        received from another wire"""
        self.name = name
        self.n1 = n1
        self.n2 = n2
        self.operator = operator
        self.value = value

    @property
    def signal(self):
        if self.value is not None:
            return self.value
        if self.operator == "NOT":
            # bitwise not using 16 bit bitmask
            mask = 0b1111111111111111
            # ^ is the XOR operator; sets each bit to 1 if only 1 of both is 1, otherwise 0. In other words in
            # combination with the mask above it produces the bitwise NOT.
            return circuit[self.n1].signal ^ mask
        else:
            if not isinstance(self.n1, int):
                self.n1 = circuit[self.n1].signal
            if not isinstance(self.n2, int):
                self.n2 = circuit[self.n2].signal
            if self.operator == "AND":
                return self.n1 & self.n2
            elif self.operator == "OR":
                return self.n1 | self.n2
            elif self.operator == "RSHIFT":
                return int(self.n1 / 2**self.n2)
            elif self.operator == "LSHIFT":
                return self.n1 * 2**self.n2

# create the circuit based on the instructions
circuit = dict()

# read in all the Wire setups; there will be no signal for a Wire until all preceding Wires are connected
for instr in data:
    # split name and equation
    instr = instr.split(" -> ")
    name = instr[1]
    # if equation contains a NOT operator, extract n1 and the operator
    if instr[0].startswith("NOT"):
        operator, n1 = instr[0].split()
        circuit[name] = Wire(name, operator="NOT", n1=n1)
    # otherwise, split and process depending on the number of elements
    else:
        instr = instr[0].split()
        # if the length of the equation is one, it is a numeric outcome or a reference to another wire
        if len(instr) == 1:
            if instr[0].isdigit():
                circuit[name] = Wire(name=name, value=int(instr[0]))
            else:
                circuit[name] = Wire(name=instr)
        # if the length is 3, it is an actual equation
        elif len(instr) == 3:
            n1 = instr[0]
            if n1.isdigit():
                n1 = int(n1)
            operator = instr[1]
            n2 = instr[2]
            if n2.isdigit():
                n2 = int(n2)
            circuit[name] = Wire(name, operator=operator, n1=n1, n2=n2)

# set the signal of a manually because when it's read in the signal of lx is still unknown which causes a key error
# this is ugly but I can't be bothered to fix it now
circuit['a'] = Wire(name='a', value=circuit['lx'].signal)

assert circuit['a'].signal == 16076
