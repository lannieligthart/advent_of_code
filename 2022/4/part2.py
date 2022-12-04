import AoC_tools.aoc_tools as aoc

data = aoc.read_input("input.txt", "\n", ",")


def s(d):
    d = d.split("-")
    d = [int(x) for x in d]
    return d


def check_overlaps(pair):
    start1, stop1 = pair[0]
    start2, stop2 = pair[1]
    if stop1 < start2 or stop2 < start1:
        return False
    else:
        return True


data = [list(map(s, d)) for d in data]
total = len(list(filter(check_overlaps, data)))

assert total == 841
