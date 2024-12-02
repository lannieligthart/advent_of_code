with open("input.txt") as f:
    data = [list(map(int, line.split())) for line in f]

# separate the two lists
l1, l2 = zip(*data)

def count_occ(n, l):
    total = 0
    for i in range(len(l)):
        if l[i] == n:
            total += 1
    return total

result = 0
for i in range(len(l1)):
    result += l1[i] * count_occ(l1[i], l2)

assert result == 23927637

