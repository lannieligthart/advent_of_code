with open("input.txt") as file:
    data = file.read().split("\n")

# parse input to a list of lists
data = [list(map(int, d.split("x"))) for d in data]

def ribbon_length(dim):
    dim.sort()
    shortest2 = dim[0:2]
    base_len = shortest2[0]*2 + shortest2[1]*2
    bow = dim[0]*dim[1]*dim[2]
    return base_len + bow

total = 0
for d in data:
    total += ribbon_length(d)

assert total == 3812909