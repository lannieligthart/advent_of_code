
import time
import itertools

class Grid(object):

    class Cube(object):

        def __init__(self, active=False):
            self.active = active

        def change_state(self):
            if self.active:
                self.active = False
            else:
                self.active = True

    def __init__(self, slice):
        self.slices = {0: slice}
        self.cubes = {}
        for s, value in self.slices.items():
            for r in range(len(value)):
                for c in range(len(self.slices[s][r])):
                    self.get_neighbours((s, r, c))
                    if self.slices[s][r][c] == '#':
                        self.cubes[(s, r, c)] = Grid.Cube(active=True)
                    elif self.slices[s][r][c] == '.':
                        self.cubes[(s, r, c)] = Grid.Cube(active=False)
        # indexing: self.slices[s][r][c]

    def get_neighbours(self, pos):
        # gets positions of neighbours, based on a specified position
        # neighbours: s-1, s, s+1, r-1
        s, r, c = pos
        slices = [s-1, s, s+1]
        rows = [r-1, r, r+1]
        cols = [c-1, c, c+1]
        positions = list(itertools.product(slices, rows, cols))
        positions.remove((s, r, c))
        # if this neighbour does not exist yet, create a white tile at this position
        for pos in positions:
            if pos not in self.cubes:
                self.cubes[pos] = Grid.Cube()
        return positions

    def count_active_neighbours(self, pos):
        neighbours = self.get_neighbours(pos)
        count = 0
        for n in neighbours:
            if self.cubes[n].active:
                count += 1
        return count

    def apply_rules(self, pos):
        cube = self.cubes[pos]
        active_neighbours = self.count_active_neighbours(pos)
        # If a cube is active and exactly 2 or 3 of its neighbors are also active, the cube remains active. Otherwise,
        # the cube becomes inactive.
        if cube.active and active_neighbours not in [2, 3]:
            return False
        # If a cube is inactive but exactly 3 of its neighbors are active, the cube becomes active. Otherwise, the cube
        # remains inactive.
        elif not cube.active and active_neighbours == 3:
            return True
        else:
            return cube.active

    def count_active(self):
        active = 0
        for key in self.cubes:
            if self.cubes[key].active:
                active += 1
        return active
    #
    # def count_not_active(self):
    #     not_active = 0
    #     for key in self.cubes:
    #         if not self.cubes[key].active:
    #             not_active += 1
    #     return not_active

    def update(self):
        to_change = []
        # copy the tiles in the current dictionary to avoid modification of the dictionary while looping through it.
        all_pos = self.cubes.copy()
        for pos in all_pos:
            if self.apply_rules(pos) != self.cubes[pos].active:
                to_change.append(pos)
        for pos in to_change:
            self.cubes[pos].change_state()

startTime = time.time()

with open('input.txt') as f:
    slice = f.read().split("\n")


print(slice)

grid = Grid(slice)
print(grid.count_active())
for _ in range(6):
    grid.update()
print(grid.count_active())

# data [slice][row][col]
# data [0] is de eerste rij
# print(floor.count_flipped(), "black tiles")
#
# for _ in range(100):
#     floor.flip_all()
# flipped = floor.count_flipped()
# assert flipped == 3665
# print(flipped, "black tiles")
#
# executionTime = (time.time() - startTime)
# print('Execution time in seconds: ' + str(executionTime))


# A = [-1, 0, 1]
# B = [0, 1, 2]
# C = [1, 2, 3]
# x = list(itertools.product(A, B, C))
# pass