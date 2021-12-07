import AoC_tools.aoc_tools as aoc

t = aoc.start()
data = aoc.string2list("input.txt", sep=",", numeric=True, display=False)

amounts = {}

for i in range(min(data), max(data)+1):
    fuel = 0
    for d in data:
        n = abs(d - i)
        fuel += (n*(n+1))/2
    amounts[i] = fuel

result = min(amounts.values())
assert result == 97164301
aoc.end(t)
