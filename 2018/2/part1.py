import AoC_tools.aoc_tools as aoc

data = aoc.read_input("input.txt", "\n")

count_2 = 0
count_3 = 0

for d in data:
    dct = {}
    for letter in d:
        if letter not in dct:
            dct[letter] = 1
        else:
            dct[letter] += 1

    count2 = False
    count3 = False
    for x in dct.values():
        if x == 2:
            count2 = True
        elif x == 3:
            count3 = True
    if count2:
        count_2 += 1
    if count3:
        count_3 += 1

assert count_2 * count_3 == 6723
