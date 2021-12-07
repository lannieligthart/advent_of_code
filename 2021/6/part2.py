import AoC_tools.aoc_tools as aoc
from collections import Counter

state = aoc.string2list('input.txt', sep=",", numeric=True, display=False)

def run(freq):
    newfreq = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
    for key, value in freq.items():
        if key > 0:
            newfreq[key-1] += value
        elif key == 0:
            newfreq[6] += value
            newfreq[8] += value
    return newfreq

freq = Counter(state)
aoc.sorted_print(freq)

for i in range(256):
    freq = run(freq)

#aoc.sorted_print(freq)
result = sum(freq.values())
assert result == 1644874076764
