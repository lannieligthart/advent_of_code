#infile = "testinput.txt"
infile = "input.txt"

with open(infile) as f:
    data = f.read().split("\n")

total = 0

# test alle richtingen.
total = 0
for r in range(len(data)):
    for c in range(len(data[0])):
        try:
            word = data[r][c] + data[r][c+2] + data[r+1][c+1] + data[r+2][c] + data[r+2][c+2]
            if word in ["MSAMS", "SSAMM", "SMASM", "MMASS"] and r+2 >= 0 and c+2 >= 0:
                total += 1
        except IndexError:
            pass

print(total)

assert total == 1905
