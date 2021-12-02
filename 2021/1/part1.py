import AoC_tools.aoc_tools as aoc

# part 1

measurements = aoc.lines2list('input.txt', numeric=True)

intervals = [(measurements[n]-measurements[n-1]) for n in range(1, len(measurements))]

count = 0
for i in intervals:
    if i > 0:
        count += 1

print(count)
assert(count == 1624)


# part 2
numbers = aoc.lines2list('input.txt', numeric=True)

measurements = [(numbers[n] + numbers[n+1] + numbers[n+2]) for n in range(len(numbers)-2)]

#aoc.lprint(measurements)

intervals = [(measurements[n]-measurements[n-1]) for n in range(1, len(measurements))]

count = 0
for i in intervals:
    if i > 0:
        count += 1

print(count)
assert(count == 1653)