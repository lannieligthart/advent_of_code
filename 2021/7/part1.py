import AoC_tools.aoc_tools as aoc
data = aoc.string2list("input.txt", sep=",", numeric=True)

amounts = {}

for i in range(min(data), max(data)+1):
    fuel = 0
    for d in data:
        fuel += abs(d - i)
    amounts[i] = fuel

result = min(amounts.values())

assert result == 344297

