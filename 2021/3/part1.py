import AoC_tools.aoc_tools as aoc

data = aoc.lines2list("C:/Users/Admin/SURFdrive/Code/advent_of_code/2021/3/input.txt")

# initialize count for most common bits in each position
bits = [0] * len(data[0])

print(bits)
for line in data:
    for i in range(len(line)):
        bits[i] += int(line[i])

print(bits)

for b in range(len(bits)):
    if bits[b] > len(data)/2:
        bits[b] = '1'
    elif bits[b] < len(data)/2:
        bits[b] = '0'


gamma = int("".join(bits), 2)
epsilon = [str(1-int(b)) for b in bits]
epsilon = int("".join(epsilon), 2)
result = gamma*epsilon

assert result == 741950

