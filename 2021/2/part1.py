import AoC_tools.aoc_tools as aoc

path = "C:/Users/Admin/SURFdrive/Code/advent_of_code/2021/2/input.txt"
data = aoc.lines2list(path)
data = aoc.split_list(data)
for d in data:
    d[1] = int(d[1])
print(data)

# forward position, depth
pos = 0
depth = 0


for d in data:
    if d[0] == 'forward':
        pos += d[1]
    elif d[0] == 'down':
        depth += d[1]
    elif d[0] == 'up':
        depth -= d[1]

print(pos, depth)
print(pos * depth)
assert pos * depth == 1488669

