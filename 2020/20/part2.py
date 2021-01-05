import itertools, math
import pandas as pd
import re
import time

with open('input.txt') as f:
    data = f.read().split("\n\n")

for i in range(len(data)):
    data[i] = data[i].split("\n")
print(data)


class Grid(object):

    def __init__(self, tiles, dim):
        self.tiles = tiles
        self.dim = dim
        self.image = [[] for _ in range(dim)]
        for i in range(len(self.image)):
            self.image[i] = [None for _ in range(dim)]

    def compare_sides(self, tile1, tile2):
        # print('comparing sides of', tile1.number, "and", tile2.number)
        tile1 = self.tiles[tile1]
        tile2 = self.tiles[tile2]
        sides = list(itertools.product([0, 1, 2, 3], [0, 1, 2, 3]))
        for s in sides:
            if tile1.sides[s[0]] == tile2.sides[s[1]][::-1] or tile1.sides[s[0]] == tile2.sides[s[1]]:
                self.tiles[tile1.number].neighbours[s[0]] = tile2
                self.tiles[tile2.number].neighbours[s[1]] = tile1

    def get_neighbours(self):
        comparisons = list(itertools.combinations(self.tiles.keys(), 2))
        for c in comparisons:
            tile1, tile2 = c
            self.compare_sides(tile1, tile2)

    def assemble(self, corner):
        current = self.tiles[corner]
        self.image[0][0] = current
        # make sure the corner piece is rotated such that neighbours 1 and 2 are valid (this will be the top left
        # corner)
        while not (isinstance(current.neighbours[1], Tile) and isinstance(current.neighbours[2], Tile)):
            current.rotate()
        # go to the first top edge piece, which should be neighbour 1, and rotate it until the corner piece is its
        # neighbour 3
        for i in range(1, dim):
            next = self.tiles[current.neighbours[1].number]
            for s in next.sides:
                if s == current.sides[1]:
                    next.flip()
            while not (next.sides[3] == current.sides[1] or next.sides[3] == current.sides[1][::-1]):
                next.rotate()
            self.image[0][i] = next
            current = next

        # now continue with the intermediate rows
        for r in range(1, dim):
            for c in range(dim):
                # neigbour above
                above = self.image[r - 1][c]
                self.image[r][c] = above.neighbours[2]
                next = self.image[r][c]
                while not (next.sides[0] == above.sides[2] or next.sides[0] == above.sides[2][::-1]):
                    next.rotate()
                if next.sides[0] == above.sides[2]:
                    next.flip()

    def render(self):
        self.render = [[] for _ in range(self.dim)]
        for r in range(len(self.image[0])):
            for c in range(len(self.image)):
                image = pd.DataFrame(self.image[r][c].image)
                # crop top and bottom rows
                image = image.iloc[1:image.shape[0]-1,1:image.shape[1]-1]
                self.render[r].append(image)
        dim = len(self.render)
        rows = []
        for r in range(dim):
            rows.append(pd.concat(self.render[r], axis=1, ignore_index=True))
        self.render = pd.concat(rows, axis=0, ignore_index=True)

    def split(self):
        for t in self.tiles.values():
            for i in range(len(t.image)):
                t.image[i] = [char for char in t.image[i]]

class Tile(object):

    def __init__(self, number, image):
        self.number = number
        self.image = image
        self.flipped = False
        self.rotation = 0
        self.neighbours = [None, None, None, None]

    def __str__(self):
        return str(self.number)

    def print(self):
        print("\nTile #", self.number)
        for i in self.image:
            print("  ".join(i))
        print("flipped:", self.flipped)
        print("neighbours:")
        nb = []
        for n in self.neighbours:
            if n is not None:
                nb.append(str(n.number))
            else:
                nb.append("-")
        print(", ".join(nb))
        print("rotation:", self.rotation)
        return None

    @property
    def sides(self):
        # generate list with sides based on self.image
        side1 = "".join(self.image[0])

        side2 = []
        for im in self.image:
            side2.append(im[-1])
        side2 = "".join(side2)

        side3 = "".join(self.image[-1])
        side3 = side3[::-1]

        side4 = []
        for im in self.image:
            side4.append(im[0])
        side4.reverse()
        side4 = "".join(side4)

        sides = [side1, side2, side3, side4]
        return sides

    def flip(self):
        # reverse the image
        for i in range(len(self.image)):
            self.image[i] = self.image[i][::-1]
        if not self.flipped:
            self.flipped = True
        else:
            self.flipped = False
        new_neighbours = [self.neighbours[0], self.neighbours[3], self.neighbours[2], self.neighbours[1]]
        self.neighbours = new_neighbours
        #self.print()

    def rotate(self):
        # rotate image
        self.image = [list(row) for row in zip(*reversed(self.image))]
        # rotate neighbours
        for i in range(len(self.image)):
            self.image[i] = "".join(self.image[i])
        new_neighbours = [None for _ in range(len(self.neighbours))]
        for n in range(len(self.neighbours)):
            new_neighbours[(n + 1) % len(self.neighbours)] = self.neighbours[n]
        self.neighbours = new_neighbours
        self.rotation = (self.rotation + 1) % 4
        #self.print()

    @staticmethod
    def generate(input):
        number = input[0].replace("Tile ", "")
        number = int(number.replace(":", ""))
        image = input[1:]
        return Tile(number, image)

def find_monsters(render):
    lines_with_monsters = 0
    for l in range(render.shape[0]-2):
        lines = render.iloc[l:l+3, :]
        # can probably be done much more easily with a single regex but for now it's 3 separate ones for each line.
        rex = ['(?=.{18}#.{1})', '(?=#.{4}##.{4}##.{4}###)', '(?=.#..#..#..#..#..#...)']
        match_indices = []
        for i in range(3):
            line = "".join(list(lines.iloc[i]))
            match_indices.append([m.start(0) for m in re.finditer(rex[i], line)])
        for i in match_indices[0]:
            if i in match_indices[1] and i in match_indices[2]:
                #print("monster in line", l, "index", i, "!")
                lines_with_monsters += 1
    return lines_with_monsters

def rotate(render):
    render = render.values.tolist()
    render = Tile(number=0,  image=render)
    render.rotate()
    for i in range(len(render.image)):
        render.image[i] = [char for char in render.image[i]]
    render = pd.DataFrame(render.image)
    return render

def flip(render):
    render = render[render.columns[::-1]]
    return render

def count_monsters(render):
    # rotate and flip and count each time until > 0 monsters are found (they only occur in one orientation).
    for _ in range(4):
        if find_monsters(render) > 0:
            return find_monsters(render)
        render = rotate(render)
    render = flip(render)
    for _ in range(4):
        if find_monsters(render) > 0:
            return find_monsters(render)
        render = rotate(render)

startTime = time.time()

tiles = {}
for d in data:
    t = Tile.generate(d)
    tiles[t.number] = t

dim = int(math.sqrt(len(data)))
grid = Grid(tiles, dim)

grid.get_neighbours()

# rotate test corner tile to allow comparison with the example
# grid.tiles[1951].flip()
# grid.tiles[1951].rotate()
# grid.tiles[1951].rotate()
#grid.assemble(1951)

# start assembly with one of the tiles identified as a corner in part 1.
grid.assemble(3413)
# split up currently joined strings into lists of hashes and points so they can be individual columns in a data frame.
# not very elegant but does the job.
grid.split()
grid.render()

monsters = count_monsters(grid.render)
print(monsters)
count = 0

# count total number of hashes in render
for i in range(grid.render.shape[0]):
    n = grid.render.iloc[:, i].value_counts()
    count += n.loc["#"]

result = count - (monsters * 15)
assert result == 2129

executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))
