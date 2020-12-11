
import pandas as pd

with open('C:/Users/Admin/Documents/Code/advent_of_code/2020/11/input.txt') as f:
    data = f.read().split("\n")

nrows = len(data)
ncols = len(data[0])

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

def get_directions(seats, cur_row, cur_col):
    max_rows = len(seats[0])-1
    max_cols = len(seats)-1

    # south
    south = []
    for i in range(cur_row + 1,max_rows):
        south.append((i, cur_col))

    # north
    north = []
    for i in range(cur_row - 1, 0, -1):
        north.append((i, cur_col))

    # east
    east = []
    col = cur_col + 1
    while col < max_cols:
        east.append((cur_row, col))
        col += 1

    # west
    west = []
    col = cur_col - 1
    while col > 0:
        west.append((cur_row, col))
        col -= 1

    # southeast
    southeast = []
    row = cur_row + 1
    col = cur_col + 1
    while row < max_rows and col < max_cols:
        southeast.append((row,col))
        row += 1
        col += 1

    # northwest
    northwest = []
    row = cur_row - 1
    col = cur_col - 1
    while row > 0 and col > 0:
        northwest.append((row,col))
        row -= 1
        col -= 1

    # southwest
    southwest = []
    row = cur_row + 1
    col = cur_col - 1
    while row < max_rows and col > 0:
        southwest.append((row,col))
        row += 1
        col -= 1

    # northeast
    northeast = []
    row = cur_row - 1
    col = cur_col + 1
    while row > 0 and col < max_cols :
        northeast.append((row,col))
        row -= 1
        col += 1

    directions = [north, south, east, west, northeast, northwest, southeast, southwest]
    return(directions)


def count_surrounding_occupied_seats(seats_copy, directions):
    n = 0
    for d in directions:
        for i in d:
            x, y = i
            try:
                if seats_copy[x][y] == '#':
                    n += 1
                    break
                elif seats_copy[x][y] == 'L':
                    break
            except IndexError:
                print("Index error!")
                print(x, y)
    return(n)

def update_seat(seats, seats_copy, r, c):
    directions = get_directions(seats, r, c)
    count = count_surrounding_occupied_seats(seats_copy, directions)
    if seats_copy[r][c] == 'L' and count == 0:
        seats[r][c] = '#'
    elif seats_copy[r][c] == '#' and count >= 5:
        seats[r][c] = 'L'


seats_copy = []
while not seats_copy == seats:
    seats_copy = [x[:] for x in seats]
    for r in range(1, nrows + 1):
        for c in range(1, ncols + 1):
            #print(r, c)
            if seats[r][c] != '.':
                update_seat(seats, seats_copy, r, c)
    #print(pd.DataFrame(seats))


def count_occupied_seats(seats):
    n = 0
    for r in range(1, nrows + 1):
        for c in range(1, ncols + 1):
            if seats[r][c] == '#':
                n += 1
    return(n)

occupied = count_occupied_seats(seats)
print(occupied)


def test(seats_copy):
    directions = get_directions(seats_copy, 2, 1)
    for d in directions:
        for i in d:
            x, y = i
            seats_copy[x][y] = 'O'

    print(pd.DataFrame(seats_copy))

    # 1966 too high
