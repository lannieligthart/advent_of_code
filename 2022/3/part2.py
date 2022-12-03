import AoC_tools.aoc_tools as aoc

data = aoc.read_input("input.txt", "\n")
data = [list(d) for d in data]

def get_prio(letter):
    if letter == letter.lower():
        return ord(letter) - 96
    elif letter == letter.upper():
        return ord(letter) - 38

def split_half(prio):
    half = int(len(prio)/2)
    h1 = prio[0:half]
    h2 = prio[half:]
    prio = [h1, h2]
    return prio

def get_common(prios, i):
    triplet = prios[i:i + 3]
    return(list(set.intersection(*map(set, triplet)))[0])

prios = [list(map(get_prio, d)) for d in data]

i = 0
badges = []
while i < len(prios):
    badges.append(get_common(prios, i))
    i += 3

assert sum(badges) == 2828
