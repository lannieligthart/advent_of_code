
with open('input.txt') as f:
    data = f.read().split("\n")

ncols = len(data[0])
nrows = len(data)

seats = []
empty_row = ['.'] * (ncols + 2)
seats.append(empty_row)

for string in data:
    row = []
    row.append('.')
    for s in string:
        row.append(s)
    row.append('.')
    seats.append(row)
seats.append(empty_row)

def count_surrounding_occupied_seats(seats_copy, r, c):
    rows = [r-1, r-1, r-1, r,   r,   r+1, r+1, r+1]
    cols = [c-1, c,   c+1, c-1, c+1, c-1, c,   c+1]
    n = 0
    for i in range(len(rows)):
        if seats_copy[rows[i]][cols[i]] == '#':
            n += 1
    return(n)


def update_seat(seats, seats_copy, r, c):
    if seats_copy[r][c] == 'L' and count_surrounding_occupied_seats(seats_copy, r, c) == 0:
        seats[r][c] = '#'
    elif seats_copy[r][c] == '#' and count_surrounding_occupied_seats(seats_copy, r, c) >= 4:
        seats[r][c] = 'L'

def count_occupied_seats(seats):
    n = 0
    for r in range(1, nrows + 1):
        for c in range(1, ncols + 1):
            if seats[r][c] == '#':
                n += 1
    return(n)

seats_copy = []
while not seats_copy == seats:
    seats_copy = [x[:] for x in seats]
    for r in range(1, nrows + 1):
        for c in range(1, ncols + 1):
            if seats[r][c] != '.':
                update_seat(seats, seats_copy, r, c)

occupied = count_occupied_seats(seats)
print(occupied)
assert occupied == 2166


