import AoC_tools.aoc_tools as aoc

data = aoc.lines2list(path="C:/Users/Admin/SURFdrive/Code/advent_of_code/2021/5/testinput.txt")
data = aoc.split_list(data, sep=" -> ")
#print(data)
for i in range(len(data)):
    data[i] = [(int(data[i][0].split(',')[0]), int(data[i][0].split(',')[1])),
               (int(data[i][1].split(',')[0]), int(data[i][1].split(',')[1]))]
#print(data)

# selecteer horizontale en diagonale lijnen

lines = []
for i in range(len(data)):
    if data[i][0][0] == data[i][1][0] or data[i][0][1] == data[i][1][1]:
        lines.append(data[i])

#print(lines)


# expand lines

def expand(line):
    x1, y1 = line[0]
    x2, y2 = line[1]
    newline = []
    # increase in x
    if x2 - x1 > 0:
        for i in range((x2 - x1) + 1):
            newline.append((x1 + i, y1))
    elif x2 - x1 < 0:
        for i in range((x1 - x2) + 1):
            newline.append((x2 + i, y1))
    # increase in y
    if y2 - y1 > 0:
        for i in range((y2 - y1) + 1):
            newline.append((x1, y1 + i))
    elif y2 - y1 < 0:
        for i in range((y1 - y2) + 1):
            newline.append((x1, y2 + i))
    return newline

for i in range(len(lines)):
    lines[i] = expand(lines[i])

aoc.lprint(lines)

positions = {}

for l in lines:
    for p in l:
        if p not in positions:
            positions[p] = 1
        elif p in positions:
            positions[p] += 1

#print(positions)

grid = aoc.Grid(positions, empty='.')
#grid.display(transpose=True)

# aantal punten met minstens waarde 2:

danger_points = 0
for key, value in positions.items():
    if value >= 2:
        danger_points += 1

print(danger_points)

from collections import Counter
print(Counter(positions.values()))

assert danger_points == 5442