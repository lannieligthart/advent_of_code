with open("input.txt") as file:
    data = file.read().split("\n")

data = [d + "." for d in data] # append a . to each row so I don't miss any numbers at the end
symbol_positions = dict()
symbols = set()
adjacent = []

for r, row in enumerate(data):
    for c, char in enumerate(row):
        if not char.isdigit() and char != ".":
            symbol_positions[(r, c)] = set()

"""loop through strings. When you reach the first digit, record the position. Check if following char is also a digit, 
if so, also record the position. Once a non-digit is reached, you have the full digit. For all the positions, check if 
they have an x or y that is at most one away from a symbol position. 
"""

def check_position(r, c, symbol_positions):
    for pos in symbol_positions.keys():
        rp, cp = pos
        difr = abs(r - rp)
        difc = abs(c - cp)
        if difr <= 1 and difc <= 1 and difr + difc > 0:
            # return the position of the neighbouring symbol
            return pos
    return None

for r, row in enumerate(data):
    digit_positions = []
    number = ''
    for c, col in enumerate(row):
        if col.isdigit():
            number += col
            digit_positions.append((r, c))
        elif number != '':
            neighbouring_symbol_positions = []
            for p in digit_positions:
                r, c = p
                nsp = check_position(r, c, symbol_positions)
                if nsp is not None:
                    neighbouring_symbol_positions.append(nsp)
            if len(neighbouring_symbol_positions) > 0:
                adjacent.append(int(number))
            for n in neighbouring_symbol_positions:
                symbol_positions[n].add((number))
            # reset
            digit_positions = []
            number = ''

gr = []

for v in symbol_positions.values():
    if len(v) == 2:
        v = list(v)
        gear_ratio = int(v[0]) * int(v[1])
        gr.append(gear_ratio)

assert sum(gr) == 81296995