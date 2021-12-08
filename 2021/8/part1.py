import AoC_tools.aoc_tools as aoc

data = aoc.lines2list("input.txt")
output_values = [line.split(" | ")[1] for line in data]
print(output_values)

result = 0
for o in output_values:
    digits = o.split()
    for d in digits:
        if len(d) in [2, 3, 4, 7]:
            result += 1

assert result == 375