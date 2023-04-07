import AoC_tools.aoc_tools as aoc
import itertools

data = aoc.read_input("input.txt", "\n")

def compare(id1, id2):
    ncom = 0
    for i in range(len(id1)):
        if id1[i] == id2[i]:
            ncom += 1
    if ncom == len(id1) - 1:
        return (id1, id2)


def compare_all(data):
    result = False
    while not result:
        for a, b in itertools.combinations(data, 2):
            if compare(a, b) is not None:
                result = True
                ids = compare(a, b)
    dif = "".join(set(ids[0]).difference(set(ids[1])))
    result = (ids[0].replace(dif, ""))
    return result

result = compare_all(data)
assert result == "prtkqyluiusocwvaezjmhmfgx"

