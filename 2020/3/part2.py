with open('C:/Users/Admin/Documents/Code/advent_of_code/3/input.txt') as f:
    text = f.read().splitlines()

def get_ntrees(down, right, text):
    row = 0
    col = 0
    trees = 0

    while row < len(text)-1:
        row += down
        col += right
        if col >= len(text[1]):
            mapcol = (col % len(text[1]))
        else:
            mapcol = col
        if text[row][mapcol] == '#':
            trees += 1

    return trees

# possible slopes [down, right] = [row, col]
slopes = [(1,1), (1,3), (1,5), (1,7), (2,1)]

n_trees = []
for s in slopes:
    n_trees.append(get_ntrees(s[0], s[1], text))

product = 1
for i in n_trees:
    product = product * i

print(product)
