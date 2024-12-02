with open("input.txt") as f:
    # split and convert both elements of resulting lists to ints
    # do this on every line in f
    data = [list(map(int, line.split())) for line in f]

# separate the two lists
l1, l2 = zip(*data)
l1, l2 = sorted(l1), sorted(l2)

sum = 0
for i in range(len(l1)):
    sum += abs(l2[i] - l1[i])

assert sum == 2815556