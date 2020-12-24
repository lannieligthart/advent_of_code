import time

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
        self.cur = (0, 0)
        self.tiles = {self.cur: HexFloor.Tile()}

    def track_path(self, path):
        i = 0
        # each path starts at 0, 0
        self.cur = (0, 0)  # (north, east)
        pos = list(self.cur)
        while i < len(path):
            if path[i] == 'e':
                pos[1] += 2
                i += 1
            elif path[i] == 'w':
                pos[1] -= 2
                i += 1
            elif path[i:i+2] == 'ne':
                pos[0] += 1
                pos[1] += 1
                i += 2
            elif path[i:i+2] == 'nw':
                pos[0] += 1
                pos[1] -= 1
                i += 2
            elif path[i:i+2] == 'se':
                pos[0] -= 1
                pos[1] += 1
                i += 2
            elif path[i:i+2] == 'sw':
                pos[0] -= 1
                pos[1] -= 1
                i += 2
            else:
                return
            self.cur = tuple(pos)

        if self.cur not in self.tiles:
            self.tiles[self.cur] = HexFloor.Tile()
        self.get_neighbours(self.cur)
        # flip the final tile
        self.tiles[self.cur].flip()

    def get_neighbours(self, pos):
        # gets positions of neighbours, based on a specified position,
        positions = {'e': (pos[0], pos[1] + 2), 'w': (pos[0], pos[1] - 2), 'ne': (pos[0] + 1, pos[1] + 1),
                     'nw': (pos[0] + 1, pos[1] - 1), 'se': (pos[0] - 1, pos[1] + 1), 'sw': (pos[0] - 1, pos[1] - 1)}

        neighbours = []
        for key, value in positions.items():
            # if this neighbour does not exist yet, create a white tile at this position
            if value not in self.tiles:
                self.tiles[value] = HexFloor.Tile()
            neighbours.append(value)
        return neighbours

    def get_flipped_neighbours(self, pos):
        neighbours = self.get_neighbours(pos)
        count = 0
        for n in neighbours:
            if self.tiles[n].flipped:
                count += 1
        return count

    def apply_rules(self, pos):
        # returns new value of tile.flipped
        tile = self.tiles[pos]
        flipped_neighbours = self.get_flipped_neighbours(pos)
        # Any black tile with zero or more than 2 black tiles immediately adjacent to it is flipped to white.
        if tile.flipped and (flipped_neighbours == 0 or flipped_neighbours > 2):
            return False
        # Any white tile with exactly 2 black tiles immediately adjacent to it is flipped to black.
        elif not tile.flipped and flipped_neighbours == 2:
            return True
        else:
            return tile.flipped

    def count_flipped(self):
        flipped = 0
        for key in self.tiles:
            if self.tiles[key].flipped:
                flipped += 1
        return flipped

    def count_not_flipped(self):
        not_flipped = 0
        for key in self.tiles:
            if not self.tiles[key].flipped:
                not_flipped += 1
        return not_flipped

    def flip_all(self):
        to_flip = []
        # copy the tiles in the current dictionary to avoid modification of the dictionary while looping through it.
        all_pos = self.tiles.copy()
        for pos in all_pos:
            if self.apply_rules(pos) != self.tiles[pos].flipped:
                to_flip.append(pos)
        for pos in to_flip:
            self.tiles[pos].flip()

startTime = time.time()

with open('input.txt') as f:
    data = f.read().split("\n")

floor = HexFloor()
for d in data:
    floor.track_path(d)

print(floor.count_flipped(), "black tiles")

for _ in range(100):
    floor.flip_all()
flipped = floor.count_flipped()
assert flipped == 3665
print(flipped, "black tiles")

executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))

