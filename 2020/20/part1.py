import itertools

with open('input.txt') as f:
    data = f.read().split("\n\n")

for i in range(len(data)):
    data[i] = data[i].split("\n")
print(data)

class Grid(object):

    def __init__(self, tiles):
        self.tiles = tiles

    def compare_sides(self, tile1, tile2):
        #print('comparing sides of', tile1.number, "and", tile2.number)
        matches = 0
        matches_flipped = 0
        sides = list(itertools.product(tile1.sides, tile2.sides))
        for s in sides:
            if s[0] == s[1][::-1]:
                matches += 1
        sides = list(itertools.product(tile1.sides_flipped, tile2.sides))
        for s in sides:
            if s[0] == s[1][::-1]:
                matches_flipped += 1
        if matches_flipped > matches:
            self.tiles[tile1.number].flip()
            return matches_flipped
        elif matches > matches_flipped:
            return matches

    def compare_all(self):
        comparisons = list(itertools.combinations(self.tiles.keys(), 2))
        matches = {}
        for key, value in self.tiles.items():
            matches[key] = 0
        for c in comparisons:
            tile1, tile2 = c
            if (self.compare_sides(self.tiles[tile1], self.tiles[tile2])) == 1:
                matches[tile1] += 1
                matches[tile2] += 1
        return(matches)


class Tile(object):

    def __init__(self, number, image):
        self.number = number
        self.image = image

    @property
    def sides(self):
        # generate list with sides based on self.image
        side1 = self.image[0]

        side2 = []
        for im in self.image:
            side2.append(im[-1])
        side2 = "".join(side2)

        side3 = self.image[-1]
        side3 = side3[::-1]

        side4 = []
        for im in self.image:
            side4.append(im[0])
        side4.reverse()
        side4 = "".join(side4)

        sides = [side1, side2, side3, side4]
        return sides

    @property
    def sides_flipped(self):
        sides = []
        for s in self.sides:
            sides.append(s[::-1])
        return sides

    def flip(self):
        # reverse the image
        for i in range(len(self.image)):
            self.image[i] = self.image[i][::-1]

    @staticmethod
    def generate(input):
        number = input[0].replace("Tile ", "")
        number = int(number.replace(":", ""))
        image = input[1:]
        return Tile(number, image)

def find_corners(matches):
    corners = []
    for tile in matches:
        if matches[tile] == 2:
            corners.append(tile)
    print(corners)
    if len(corners) == 4:
        result = corners[0] * corners[1] * corners[2] * corners[3]
        print(result)
    else:
        print("more than 4:", len(corners))

tiles = {}
for d in data:
    t = Tile.generate(d)
    tiles[t.number] = t

grid = Grid(tiles)

matches = grid.compare_all()
print(matches)
from collections import Counter
print(Counter(matches.values()).most_common())

corners = []
for key, value in matches.items():
    if value == 2:
        corners.append(key)

print(corners)

result = corners[0] * corners[1] * corners[2] * corners[3]
print(result)

assert result == 108603771107737
