#infile = "testinput.txt"
infile = "input.txt"

with open(infile) as f:
    data = f.read().split("\n")

def check_word(data, r, c, inc_r, inc_c):
    try:
        word = data[r][c] + data[r + inc_r][c + inc_c] + data[r + 2*inc_r][c + 2*inc_c] + data[r + 3*inc_r][c + 3*inc_c]
        if word in ["XMAS", "SAMX"] and r + 3*inc_r >= 0 and c + 3*inc_c >= 0:
            return 1
        else:
            return 0
    except IndexError:
        return 0

# check all directions

total = 0

for r in range(len(data)):
    for c in range(len(data[0])):
        # horizontal
        total += check_word(data, r, c, inc_r=0, inc_c=1)
        # vertical
        total += check_word(data, r, c, inc_r=1, inc_c=0)
        # diagonal
        total += check_word(data, r, c, inc_r=1, inc_c=1)
        total += check_word(data, r, c, inc_r=-1, inc_c=1)

print(total)

assert total == 2613

