import AoC_tools.aoc_tools as aoc

data = aoc.lines2list("input.txt")

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
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
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
                return True

corrupt = []
for i in range(len(data)):
    result = find_corrupt(data[i])
    if result:
        corrupt.append(i)

# remove corrupt lines from data
data = [data[i] for i in range(len(data)) if i not in corrupt]

line = '[({(<(())[]>[[{[]{<()<>>'

def autocomplete(line):
    i = 0
    while not i == len(line):
        if line[i] in ['[', '(', '{', '<']:
            i += 1
        elif line[i] in [']', ')', '}', '>']:
            if brackets[line[i]] == brackets[line[i-1]]:
                line = line[:i-1] + line[i+1:]
                i = 0
    to_add = ''
    for char in line:
        if char == '{':
            to_add += '}'
        if char == '[':
            to_add += ']'
        if char == '(':
            to_add += ')'
        if char == '<':
            to_add += '>'
    return to_add[::-1]

def compute_score(to_add):
    total = 0
    for i in range(len(to_add)):
        total = total * 5 + values[to_add[i]]
    return total

scores = []
for line in data:
    to_add = autocomplete(line)
    scores.append(compute_score(to_add))

scores.sort()
from math import trunc
middle = trunc(len(scores)/2)
result = scores[middle]
assert result == 2391385187