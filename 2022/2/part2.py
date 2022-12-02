import AoC_tools.aoc_tools as aoc

data = aoc.read_input("input.txt", "\n", " ")

dct = {"A": 1,
     "B": 2,
     "C": 3,
     "X": 1,
     "Y": 2,
     "Z": 3}

def game(p1, outcome):
    # lose
    if outcome == "X":
        # if p1 == A, to lose play Z
        # B -> X
        # C -> Y
        if p1 == "A":
            p2 = "Z"
            return dct[p2]
        elif p1 == "B":
            p2 = "X"
            return dct[p2]
        elif p1 == "C":
            p2 = "Y"
            return dct[p2]
    # draw
    elif outcome == "Y":
        return dct[p1] + 3

    # win
    # if p1 == A, to win play Y
    # B -> Z
    # C -> X
    elif outcome == "Z":
        if p1 == "A":
            p2 = "Y"
            return dct[p2] + 6
        elif p1 == "B":
            p2 = "Z"
            return dct[p2] + 6
        elif p1 == "C":
            p2 = "X"
            return dct[p2] + 6

total = 0
for d in data:
    p1 = d[0]
    p2 = d[1]
    result = game(p1, p2)
    total += result

assert total == 11756






