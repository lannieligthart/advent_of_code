with open("input.txt") as f:
    data = f.read().split("\n")

data = [d.split() for d in data]

l1 = [int(d[0]) for d in data]
l2 = [int(d[1]) for d in data]

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

