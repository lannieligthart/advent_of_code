def transform(data):
    return list(map(list, zip(*data)))

def roll(row):
    row_new = row
    for i in range(1, len(row)):
        if row[i] == 'O' and row[i - 1] == ".":
            row_new[i - 1] = 'O'
            row_new[i] = '.'
    return row_new

def roll_row(row):
    for i in range(len(row)):
        row = roll(row)
    return row

def roll_west(data):
    for i in range(len(data)):
        data[i] = roll_row(data[i])
    return data

def roll_east(data):
    # transform so that east becomes west
    data = [list(reversed(data[i])) for i in range(len(data))]
    for i in range(len(data)):
        data[i] = roll_row(data[i])
    # transform back
    data = [list(reversed(data[i])) for i in range(len(data))]
    return data

def roll_north(data):
    # transform so that north becomes west
    data_t = transform(data)
    for i in range(len(data_t)):
        data_t[i] = roll_row(data_t[i])
    # transform back
    data_rolled = transform(data_t)
    return data_rolled

def roll_south(data):
    # transform so that north becomes west
    data_t = transform(data)
    data_t = [list(reversed(data_t[i])) for i in range(len(data_t))]

    # roll each row
    for i in range(len(data_t)):
        data_t[i] = roll_row(data_t[i])

    # transform back
    data_t = [list(reversed(data_t[i])) for i in range(len(data_t))]
    data_rolled = transform(data_t)
    return data_rolled

def cycle(data):
    data = roll_north(data)
    data = roll_west(data)
    data = roll_south(data)
    data = roll_east(data)
    data_after = data
    factor = [abs(i - len(data_after)) for i in range(len(data_after))]
    counts = [data_after[i].count("O") for i in range(len(data_after))]
    total = sum([counts[i] * factor[i] for i in range(len(counts))])
    return data_after, total

def findperiod(outcomes, start_pos):
    for length in range(2, len(outcomes)):
        rep = outcomes[start_pos:length + start_pos]
        if outcomes[length + start_pos: length+length + start_pos] == rep:
            return length


with open("input.txt") as file:
    data = file.read().split("\n")

data = [list(d) for d in data]

# determine loads after each cycle
outcomes = []
for i in range(160):
    print(i)
    data, outcome = cycle(data)
    outcomes.append(outcome)

# based on the first 200 loads, determine period and offset
for offset in range(100):
    period = findperiod(outcomes, offset)
    if period is not None:
        break

# determine which index the 1 billionth load would have
idx = ((1000000000-(offset+1)) % period)
# get the corresponding load
result = outcomes[offset + idx]
assert result == 104409
