import AoC_tools.aoc_tools as aoc

data = aoc.read_input("input.txt", "\n", ",")


def s(d):
    d = d.split("-")
    d = [int(x) for x in d]
    return d


def check_contains(pair):
    start1, stop1 = pair[0]
    start2, stop2 = pair[1]
    if start1 >= start2 and stop1 <= stop2:
        return True
    elif start2 >= start1 and stop2 <= stop1:
        return True
    else:
        return False

data = [list(map(s, d)) for d in data]
total = len(list(filter(check_contains, data)))

assert total == 534
