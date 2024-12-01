with open("input.txt") as f:
    data = f.readlines()

data = [d.split() for d in data]

l1 = [int(d[0]) for d in data]
l2 = [int(d[1]) for d in data]

l1.sort()
l2.sort()

sum = 0
for i in range(len(l1)):
    sum += abs(l2[i] - l1[i])

assert sum == 2815556