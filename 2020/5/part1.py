# rows 0-128
# F lower
# B upper
# cols 0-8
# L lower
# R upper

with open('C:/Users/Admin/Documents/Code/advent_of_code/5/input.txt') as f:
    data = f.read().split("\n")

def get_row_number(bp):
    min = 0
    max = 128
    for i in (range(len(bp)-3)):
        if bp[i] == 'F':
            max = (max + min) / 2
        elif bp[i] == 'B':
            min = (max + min) /2
    row = int(min)
    return(row)

def get_col_number(bp):
    min = 0
    max = 8
    for i in (range(len(bp)-3, len(bp))):
        if bp[i] == 'L':
            max = (max + min) / 2
        elif bp[i] == 'R':
            min = (max + min) /2
    col = int(min)
    return(col)

def get_seat_id(row, col):
    id = row*8 + col
    return id


assert get_row_number('BFFFBBFRRR') == 70
assert get_row_number('FFFBBBFRRR') == 14
assert get_row_number('BBFFBBFRLL') == 102

assert get_col_number('BFFFBBFRRR') == 7
assert get_col_number('FFFBBBFRRR') == 7
assert get_col_number('BBFFBBFRLL') == 4

seat_ids = []

for bp in data:
    row = get_row_number(bp)
    col  =get_col_number(bp)
    seat_ids.append(get_seat_id(row, col))

print(max(seat_ids))




