with open("input.txt") as file:
    data = file.read().split("\n")

data = [d + "." for d in data] # append a . to each row so I don't miss any numbers at the end
symbols = set()
# add all the symbol coordinates to a dictionary with emtpy sets.
symbol_positions = {
    (r, c): set()
    for r, row in enumerate(data)
    for c, char in enumerate(row)
    if not char.isdigit() and char != "."
    }

def check_adjacency(r, c, symbol_positions):
    for pos in symbol_positions:
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
    for c, char in enumerate(row):
        # if you encounter a digit, add it to the current number
        if char.isdigit():
            number += char
            digit_positions.append((r, c))
        # if you don't encounter a digit, and there is a current number, process the number
        elif number != '':
            # record the positions of adjacent symbols
            adjacent_symbols = []
            for p in digit_positions:
                nsp = check_adjacency(*p, symbol_positions.keys())
                # if an adjacent symbol was detected, add it to the list
                if nsp is not None:
                    adjacent_symbols.append(nsp)
            for n in adjacent_symbols:
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