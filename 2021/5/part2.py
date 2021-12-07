import AoC_tools.aoc_tools as aoc

st = aoc.start()

data = aoc.lines2list(path="C:/Users/Admin/SURFdrive/Code/advent_of_code/2021/5/input.txt")
data = aoc.split_list(data, sep=" -> ")
#print(data)
for i in range(len(data)):
    data[i] = [(int(data[i][0].split(',')[0]), int(data[i][0].split(',')[1])),
               (int(data[i][1].split(',')[0]), int(data[i][1].split(',')[1]))]
#print(data)

lines = data
print(lines)

# expand lines

def expand(line):
    x1, y1 = line[0]
    x2, y2 = line[1]
    newline = []
    dif_x = abs(x1 - x2)
    dif_y = abs(y1 - y2)
    dif = max(dif_x, dif_y)
    for i in range(dif + 1):
        if y2 - y1 > 0:
            i_y = i
        elif y2-y1 < 0:
            i_y = -i
        elif y2 == y1:
            i_y = 0
        if x2-x1 > 0:
            i_x = i
        elif x2-x1 < 0:
            i_x = -i
        elif x2 == x1:
            i_x = 0
        newline.append((x1 + i_x, y1 + i_y))
    return newline

for i in range(len(lines)):
    lines[i] = expand(lines[i])

#aoc.lprint(lines)

positions = {}

for l in lines:
    for p in l:
        if p not in positions:
            positions[p] = 1
        elif p in positions:
            positions[p] += 1

#grid = aoc.Grid(positions, empty=".")
#grid.display(transpose=True)

# aantal punten met minstens waarde 2:

danger_points = 0
for key, value in positions.items():
    if value >= 2:
        danger_points += 1

#print(danger_points)

from collections import Counter
#print(Counter(positions.values()))

assert danger_points == 19571

aoc.end(st)
