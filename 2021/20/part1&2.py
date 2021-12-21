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

def get_value(pos, pixels):
    # obtain value of a pixel based on its neighbours' values
    row, col = pos
    nb = get_neighbours(row, col)
    string = ''
    for n in nb:
        # als deze pixel voorkomt in de grid betekent het dat hij aan staat.
        if pixels[n] == '#':
            string += '1'
        elif pixels[n] == '.':
        # zo niet, dan staat hij uit.
            string += '0'
    # bepaal het getal wat hoort bij deze binaire string.
    value = int(string, 2)
    return value


def enhance(pixels, round):
    if round % 2 == 0:
        even = True
    else:
        even = False
    # get the relevant pixel positions depending on even or odd round.
    pixels_selected = {}
    for key, value in pixels.items():
        if not even:
            if pixels[key] == '#':
                pixels_selected[key] = "#"
        if even:
            if pixels[key] == '.':
                pixels_selected[key] = "."

    pixels = pixels_selected
    # get range for rows and cols
    rows = [key[0] for key in pixels.keys()]
    cols = [key[1] for key in pixels.keys()]
    pixels_plus2 = {}
    # vul aan op basis van de min en max.
    for row in range(min(rows)-2, max(rows) + 3):
        for col in range(min(cols)-2, max(cols) + 3):
            if not even:
                if (row, col) in pixels:
                    pixels_plus2[(row, col)] = "#"
                elif (row, col) not in pixels:
                    pixels_plus2[(row, col)] = "."
            elif even:
                if (row, col) in pixels:
                    pixels_plus2[(row, col)] = "."
                elif (row, col) not in pixels:
                    pixels_plus2[(row, col)] = "#"
    pixels_plus4 = {}
    for row in range(min(rows)-4, max(rows) + 5):
        for col in range(min(cols)-4, max(cols) + 5):
            if not even:
                if (row, col) in pixels:
                    pixels_plus4[(row, col)] = "#"
                elif (row, col) not in pixels:
                    pixels_plus4[(row, col)] = "."
            elif even:
                if (row, col) in pixels:
                    pixels_plus4[(row, col)] = "."
                elif (row, col) not in pixels:
                    pixels_plus4[(row, col)] = "#"

    pixels_new = {}
    for key in pixels_plus2.keys():
        # bepaal de waarde die hoort bij elke pixel in de lijst.
        # let op, in oneven rondes gaat dit niet zomaar goed!
        value = get_value(key, pixels_plus4)
        newpixel = alg[value]
        pixels_new[key] = newpixel
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

results = []

for i in range(1, 51):
    pixels = enhance(pixels, round=i)
    if i == 2 or i == 50:
        values = list(pixels.values())
        results.append(values.count("#"))

print(results)
# part 1
assert results[0] == 5619
# part 2
assert results[1] == 20122
