with open("input.txt") as file:
    data = file.read().split("\n")

data = [list(map(int, d.split())) for d in data]


def find_next(seq):
    # find deltas for input seq
    while not all(e == 0 for e in seq[-1]):
        # add a new row by calculating the difference between adjacent numbers
        seq.append([seq[-1][i + 1] - seq[-1][i] for i in range(len(seq[-1]) - 1)])
    # once only zeroes are left, extrapolate each sequence, starting with the last one that contains only zeroes
    output = [0]
    for i in reversed(range(len(seq))):
        output.append(seq[i][-1] + output[-1])
    return output[-1]


# for each sequence in the input, obtain the next value. Sum these values across all sequences.

# part 1
total = sum([find_next([seq]) for seq in data])
assert total == 1681758908

# part 2
total = 0
for seq in reversed(data):
    seq.reverse()
    total += find_next([seq])
assert total == 803

