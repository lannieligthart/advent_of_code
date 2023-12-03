with open("input.txt") as file:
    data = file.read().split("\n")

data = [d + "." for d in data] # append a . to each row so I don't miss any numbers at the end
symbol_positions = dict()
symbols = set()
adjacent = []

for r, row in enumerate(data):
    for c, char in enumerate(row):
        if not char.isdigit() and char != ".":
            symbol_positions[(r, c)] = None

print(symbol_positions)

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
            return True
    return False

for r, row in enumerate(data):
    digit_positions = []
    number = ''
    for c, col in enumerate(row):
        # if you encounter a digit, add it to the current number
        if col.isdigit():
            number += col
            digit_positions.append((r, c))
        # if you don't encounter a digit, and there is a current number, process the number
        elif number != '':
            #print(number)
            # for all digit coordinates, check if the position is adjacent to a symbol position
            for p in digit_positions:
                r, c = p
                result = check_position(r, c, symbol_positions)
                if result:
                    adjacent.append(int(number))
                    break
            digit_positions = []
            number = ''


print(sum(adjacent))

assert sum(adjacent) == 517021
