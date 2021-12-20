import AoC_tools.aoc_tools as aoc


def display(pixels):
    """convert row/col structure to x,y coordinates and create a grid to display correctly"""
    pixels_xy = {}
    for key, value in pixels.items():
        y, x = key
        pixels_xy[(x,y)] = value
    grid = aoc.Grid(pixels_xy, empty='.', matrix=True)
    grid.display(transpose=True)


def get_neighbours(row, col):
    nb = []
    nb.append((row - 1, col - 1))
    nb.append((row - 1, col))
    nb.append((row - 1, col + 1))
    nb.append((row, col - 1))
    nb.append((row, col))
    nb.append((row, col + 1))
    nb.append((row + 1, col - 1))
    nb.append((row + 1, col))
    nb.append((row + 1, col + 1))
    return nb

def get_value(pos):
    # obtain value of a pixel based on its neighbours' values
    row, col = pos
    nb = get_neighbours(row, col)
    string = ''
    for n in nb:
        if n in pixels:
            string += '1'
        else:
            string += '0'
    #print(string)
    value = int(string, 2)
    return value


def enhance(pixels, round):
    # get range for rows and cols
    rows = []
    cols = []
    for p in pixels.keys():
        row, col = p
        rows.append(row)
        cols.append(col)

    # list the pixels to take into consideration for each round, existing range plus and minus 1
    pixel_list = []
    for r in range(min(rows) - 4, max(rows) + 5): # these numbers depend on the round
        for c in range(min(cols) - 4, max(cols) + 5):
            pixel_list.append((r, c))

    pixels_new = {}

    for p in pixel_list:
        value = get_value(p)
        newpixel = alg[value]
        if newpixel == '#':
            pixels_new[p] = newpixel
    display(pixels_new)
    return pixels_new

data = aoc.read_groups("input.txt")
alg = data[0]
image = data[1].split("\n")
pixels = {}
nrow = len(image)
ncol = len(image[0])
for row in range(nrow):
    for col in range(ncol):
        if image[row][col] == '#':
            pixels[(row, col)] = "#"

for i in range(1, 3):
    pixels = enhance(pixels, i)
    display(pixels)
    print(len(pixels))

# bepaal aantal rijen en kolommen in untrimmed image:
rows = []
cols = []
for key in pixels.keys():
    rows.append(key[0])
    cols.append(key[1])
rmin = min(rows)
cmin = min(cols)
rmax = max(rows)
cmax = max(cols)

trimmed_image = {}

for key, value in pixels.items():
    row, col = key
    if row > rmin + i*2 and col > cmin + i*2 and row < rmax-(i*2+1) and col < cmax-(i*2+1):
        trimmed_image[(row, col)] = value

print("Trimmed:")
display(trimmed_image)
print(len(trimmed_image))

#5619
#3 rondes: 7061