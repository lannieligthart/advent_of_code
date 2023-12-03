with open("input.txt") as file:
    data = file.read().split("\n")

data = [d + "." for d in data]  # append a . to each row so I don't miss any numbers at the end

symbols = set()
# add all the symbol coordinates to an otherwise empty dictionary.
symbol_positions = {
    (r, c): None
    for r, row in enumerate(data)
    for c, char in enumerate(row)
    if not char.isdigit() and char != "."
    }

"""loop through strings. When you reach the first digit, record the position. Check if following char is also a digit, 
if so, also record the position. Once a non-digit is reached, you have the full digit. For all the positions, check if 
they have an x or y that is at most one away from a symbol position. 
"""

def check_adjacency(r, c, symbol_positions):
    # check if a set of coordinates is adjacent to any of the symbol coordinates
    for pos in symbol_positions:
        rp, cp = pos
        difr = abs(r - rp)
        difc = abs(c - cp)
        if difr <= 1 and difc <= 1 and difr + difc > 0:
            return True
    return False

adjacent = []

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
            # for all coordinates of the number, check if they are adjacent to a symbol position
            for p in digit_positions:
                result = check_adjacency(*p, symbol_positions.keys())
                if result:
                    adjacent.append(int(number))
                    break
            digit_positions = []
            number = ''

assert sum(adjacent) == 517021
