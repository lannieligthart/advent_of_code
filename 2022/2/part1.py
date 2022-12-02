# A for Rock, B for Paper, and C for Scissors
# 1 for Rock, 2 for Paper, and 3 for Scissors
# Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock

# p2 p1
# 1 > 3 win -2
# 1 < 2 lose -1
# 2 > 1 win 1
# 2 < 3 lose -1
# 3 > 2 win 1
# 3 < 1 lose 2

# 0 if you lost, 3 if the round was a draw, and 6 if you won

import AoC_tools.aoc_tools as aoc

data = aoc.read_input("input.txt", "\n", " ")

dct = {"A": 1,
     "B": 2,
     "C": 3,
     "X": 1,
     "Y": 2,
     "Z": 3}

def game(p1, p2):
    p1 = dct[p1]
    p2 = dct[p2]
    if p1 == p2:
        return 3 + p2
    # 1 of -2: win
    elif p2 - p1 in [1, -2]:
        return 6 + p2
    # -1 of 2: lose
    elif p2 - p1 in [-1, 2]:
        return 0 + p2
    elif p2 == p1:
        return 3 + p2

total = 0
for d in data:
    p1 = d[0]
    p2 = d[1]
    result = game(p1, p2)
    total += result

assert total == 12645






