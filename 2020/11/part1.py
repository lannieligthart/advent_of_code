import pandas as pd
import itertools

with open('testinput.txt') as f:
    data = f.read().split("\n")

ncol = len(data[0])
nrow = len(data)

empty_row = ['.'] * (ncol + 2)
rows = []
rows.append(empty_row)

for d in data:
    empty_seat = '.'
    row = []
    row.append(empty_seat)
    new_seats = [s for s in d]
    row.extend(new_seats)
    row.append(empty_seat)
    rows.append(row)
rows.append(empty_row)

seats = pd.DataFrame(rows)
#seats = data
print(seats)

def count_surrounding_occupied_seats(seats_copy, r, c):
    rows = [r-1, r-1, r-1, r,   r,   r+1, r+1, r+1]
    cols = [c-1, c,   c+1, c-1, c+1, c-1, c,   c+1]
    n = 0
    for i in range(len(rows)):
        if seats_copy.iloc[rows[i], cols[i]] == '#':
            n += 1
    return(n)


def update_seat(seats, r, c):
    if seats_copy.iloc[r, c] == 'L' and count_surrounding_occupied_seats(seats_copy, r, c) == 0:
        seats.iloc[r, c] = '#'
    elif seats_copy.iloc[r,c] == '#' and count_surrounding_occupied_seats(seats_copy, r, c) >= 4:
        seats.iloc[r, c] = 'L'


def count_occupied_seats(seats):
    n = 0
    for r in range(1, seats.shape[0]-1):
        for c in range(1, seats.shape[1] - 1):
            if seats.iloc[r, c] == '#':
                n += 1
    return(n)

seats_copy = pd.DataFrame()
while not seats_copy.equals(seats):
    seats_copy = seats.copy(deep=True)
    for r in range(1, seats.shape[1]-1):
        for c in range(1, seats.shape[0] - 1):
            if seats.iloc[r,c] != '.':
                update_seat(seats, r, c)
    #print(seats)

occupied = count_occupied_seats(seats)
print(occupied)
pass

