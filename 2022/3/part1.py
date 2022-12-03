import AoC_tools.aoc_tools as aoc

data = aoc.read_input("input.txt", "\n")
data = [list(d) for d in data]

def get_prio(letter):
    if letter == letter.lower():
        return ord(letter) - ord("a") + 1
    elif letter == letter.upper():
        return ord(letter) - ord("A") + 27

def split_half(prio):
    half = int(len(prio)/2)
    prio = [prio[0:half], prio[half:]]
    return prio

def get_dup(prio):
    for p in prio[0]:
        if p in prio[1]:
            return p

prios = [list(map(get_prio, d)) for d in data]
prios_split = list(map(split_half, prios))
assert sum(list(map(get_dup, prios_split))) == 8252

