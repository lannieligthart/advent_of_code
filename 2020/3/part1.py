with open('input.txt') as f:
    text = f.read().splitlines()

row = 0
col = 0
trees = 0

while row < len(text)-1:
    row += 1
    col += 3
    if col > len(text[1]):
        mapcol = (col % len(text[1]))
    else:
        mapcol = col
    if text[row][mapcol] == '#':
        trees += 1

print("aantal bomen:")
print(trees)
