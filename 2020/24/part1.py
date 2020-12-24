
class HexFloor(object):

    class Tile(object):
        def __init__(self, flipped=False):
            self.flipped = flipped

        def flip(self):
            if self.flipped:
                self.flipped = False
            else:
                self.flipped = True

    def __init__(self):
        self.cursor = [0, 0]
        self.tiles = {(self.cursor[0], self.cursor[1]): HexFloor.Tile()}

    @property
    def cur_tile(self):
        return self.tiles[(self.cursor[0], self.cursor[1])]


    def track_path(self, path):
        #self.pos: (n, e)
        i = 0
        if len(path) == 0:
            return
        self.cursor = [0, 0]
        while i < len(path):
            if path[i] == 'e':
                self.cursor[1] += 2
                i += 1
            elif path[i] == 'w':
                self.cursor[1] -= 2
                i += 1
            elif path[i:i+2] == 'ne':
                self.cursor[0] += 1
                self.cursor[1] += 1
                i += 2
            elif path[i:i+2] == 'nw':
                self.cursor[0] += 1
                self.cursor[1] -= 1
                i += 2
            elif path[i:i+2] == 'se':
                self.cursor[0] -= 1
                self.cursor[1] += 1
                i += 2
            elif path[i:i+2] == 'sw':
                self.cursor[0] -= 1
                self.cursor[1] -= 1
                i += 2
            else:
                return
        # if the current tile is not listed yet, add it
        if not (self.cursor[0], self.cursor[1]) in self.tiles:
            self.tiles[(self.cursor[0], self.cursor[1])] = HexFloor.Tile()
        self.cur_tile.flip()



with open('testinput.txt') as f:
    data = f.read().split("\n")

floor = HexFloor()
for d in data:
    floor.track_path(d)

flipped = 0
for key in floor.tiles:
    if floor.tiles[key].flipped:
        flipped += 1

print("tiles seen:", len(floor.tiles))
print("black tiles:", flipped)

assert len(floor.tiles) == 15
assert flipped == 10

with open('testinput.txt') as f:
    data = f.read().split("\n")

floor = HexFloor()
for d in data:
    floor.track_path(d)

flipped = 0
for key in floor.tiles:
    if floor.tiles[key].flipped:
        flipped += 1

print("tiles seen:", len(floor.tiles))
print("black tiles:", flipped)

for key, value in floor.tiles.items():
    print(key, value.flipped)

