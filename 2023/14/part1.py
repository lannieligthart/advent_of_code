from AoC_tools import aoc22 as aoc

def transform(data):
    return list(map(list, zip(*data)))

def roll(row):
    row_new = row
    for i in range(1, len(row)):
        # print("".join(row))
        if row[i] == 'O' and row[i - 1] == ".":
            row_new[i - 1] = 'O'
            row_new[i] = '.'
    return row_new

def roll_rocks(row):
    for i in range(len(row)):
        row = roll(row)
    print(row)
    return row


with open("input.txt") as file:
    data = file.read().split("\n")

data = [list(d) for d in data]

# transform so we can just roll to the beginning of a list
data_t = transform(data)
grid_t = aoc.Grid.read(data_t)

# roll each row
for i in range(len(data_t)):
    data_t[i] = roll_rocks(data_t[i])

# transform back
data_rolled = transform(data_t)

# check result
grid = aoc.Grid.read(data_rolled)
grid.display()

# calculate outcome
factor = [abs(i - len(data_rolled)) for i in range(len(data_rolled))]
counts = [data_rolled[i].count("O") for i in range(len(data_rolled))]
total = sum([counts[i] * factor[i] for i in range(len(counts))])

print(total)

assert total == 113486