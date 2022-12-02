import AoC_tools.aoc_tools as aoc

data = aoc.read_input("input.txt", "\n", " ")

dct = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}

def game(p1, outcome):
    # lose
    if outcome == "X":
        # if p1 == A, to lose play Z
        # B -> X
        # C -> Y
        if p1 == "A":
            return dct["Z"]
        elif p1 == "B":
            return dct["X"]
        elif p1 == "C":
            return dct["Y"]
    # draw
    elif outcome == "Y":
        return dct[p1] + 3

    # win
    elif outcome == "Z":
        # if p1 == A, to win play Y
        # B -> Z
        # C -> X
        if p1 == "A":
            return dct["Y"] + 6
        elif p1 == "B":
            return dct["Z"] + 6
        elif p1 == "C":
            return dct["X"] + 6

total = 0
for d in data:
    p1 = d[0]
    p2 = d[1]
    result = game(p1, p2)
    total += result

assert total == 11756






