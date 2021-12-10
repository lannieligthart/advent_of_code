import AoC_tools.aoc_tools as aoc

data = aoc.lines2list("input.txt")

line = data[0]

brackets = {
    '{': 'curly',
    '}': 'curly',
    '[': 'square',
    ']': 'square',
    '(': 'round',
    ')': 'round',
    '>': 'pointy',
    '<': 'pointy'
}

values = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}


def find_corrupt(line):
    i = 0
    while not i == len(line):
        if line[i] in ['[', '(', '{', '<']:
            i += 1
        elif line[i] in [']', ')', '}', '>']:
            if brackets[line[i]] == brackets[line[i-1]]:
                line = line[:i-1] + line[i+1:]
                i = 0
            else:
                return line[i]


corrupt = []
for line in data:
    result = find_corrupt(line)
    if result is not None:
        corrupt.append(result)

print(len(corrupt))

total = 0
for c in corrupt:
    total += values[c]
print(total)