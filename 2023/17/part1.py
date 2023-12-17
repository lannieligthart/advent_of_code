from AoC_tools import aoc22 as aoc
from queue import PriorityQueue
from collections import defaultdict


class State(object):

    def __init__(self, pos, data):
        self.pos = pos
        self.data = data
        self.drc = None
        self.visited = []
        self.heat_loss = 0
        self.n_straight = 0

    def __str__(self):
        return f"""Position: {self.pos}
Direction: {self.drc}
Visited: {self.visited}
Heat loss: {self.heat_loss}
Potential: {self.potential}
"""
    def __gt__(self, other):
        return self.potential < other.potential

    def __lt__(self, other):
        return self.potential < other.potential

    @property
    def potential(self):
        """already incurred heat loss + manhattan distance to finish * 1 (dist * min heat loss per step)"""
        x, y = self.pos
        x_max = len(self.data[0])
        y_max = len(self.data)
        return self.heat_loss + abs(x - x_max) + abs(y - y_max)

    def generate_moves(self):
        # there are 3 directions to move in: left, right, straight.
        # straight is only allowed when at most two previous moves were straight.
        # the other ones are only possible if on the map.
        r, c = self.pos
        right = ("R", (r, c + 1))
        left = ("L", (r, c - 1))
        down = ("D", (r + 1, c))
        up = ("U", (r - 1, c))
        options = {"D": [down, left, right],
                   "U": [up, left, right],
                   "L": [up, left, down],
                   "R": [up, right, down]
                   }
        if self.drc is not None:
            moves = options[self.drc]
        else:
            moves = [up, down, left, right]
        # keep only moves that don't make us go off grid
        moves = [x for x in moves if x[1][0] >= 0 and x[1][0] < len(self.data) and x[1][1] >= 0 and x[1][1] < len(self.data[0])]
        moves = [m for m in moves if not (m[0] == self.drc and self.n_straight == 3)]
        return moves

    def move(self, step):
        drc, pos = step
        self.pos = pos
        # reset if necessary if we change directions
        if self.n_straight == 3 and self.drc != drc:
            self.n_straight = 0
        elif self.n_straight == 3 and drc == self.drc:
            print("het gaat niet goed!")
        elif self.drc == drc:
            self.n_straight += 1
        self.drc = drc
        self.visited.append(pos)
        self.heat_loss += self.data[pos[0]][pos[1]]

# generate a new stated based on an old one plus a new move
def new_state(oldstate, move):
    #oldstate.move(move)
    data = oldstate.data
    drc = oldstate.drc
    pos = oldstate.pos
    n_straight = oldstate.n_straight
    visited = oldstate.visited.copy()
    heat_loss = oldstate.heat_loss
    newstate = State(pos, data)
    newstate.heat_loss = heat_loss
    newstate.drc = drc
    newstate.visited = visited
    newstate.n_straight = n_straight
    newstate.move(move)
    return newstate

previous_states = dict()

with open("testinput.txt") as file:
    data = file.read().split("\n")

data = [list(d) for d in data]
data = [list(map(int, d)) for d in data]
grid = aoc.Grid.read(data)
finish = (grid.x_max, grid.y_max)

states = PriorityQueue()

# maak beginstate aan. Richting kan D of R zijn, maakt niet uit (maakt wel uit voor bepalen wat de volgende stap mag zijn!.
s = State(pos=(0, 0), data=data)

# voeg beginstate toe aan de queue
states.put((len(s.visited), s))

best_path = None
min_heat_loss = 100000

while not states.empty():
    state = states.get()[1]
    moves = state.generate_moves()
    if len(moves) > 0:
        for m in moves:
            #print(state)
            newstate = new_state(state, m)
            #print(newstate)
            # als we hiermee aankomen bij de finish checken we of dit nieuwe pad beter is dan het huidige beste pad:
            if newstate.pos == finish:
                # als dit pad beter is dan het huidige beste pad, vervang het huidige en vraag geen nieuwe moves meer op
                if newstate.heat_loss < min_heat_loss:
                    min_heat_loss = newstate.heat_loss
                    best_path = newstate
                    print("min heat loss:", min_heat_loss)
                    print("queue length:", states.qsize())
            # nog niet aangekomen, dan voegen we het nieuwe pad toe aan de queue.
            # priority baseren op afstand van finish en heat_loss.
            else:
                # if this state has not been seen before, add it
                s = (newstate.pos, newstate.n_straight, newstate.drc)
                if s not in previous_states.keys():
                    previous_states[s] = newstate.potential
                    better = True
                # if it has been seen before, check if it's better than the previous one. If yes, proceed, if not, drop it.
                elif newstate.potential < previous_states[s]:
                    better = True
                elif newstate.potential >= previous_states[s]:
                    better = False
                # als de best mogelijke uitkomst kleiner is dan het nu beste resultaat, laat hem dan door
                if newstate.potential < min_heat_loss and better:
                    states.put((newstate.potential, newstate))
                # if states.qsize() % 10 == 0:
                #     print(states.qsize())
            #max_heat_loss = newstate.heat_loss/len(newstate.visited)


print(min_heat_loss)
print(best_path)



grid = aoc.Grid.from_list(best_path.visited)
grid.transpose()
grid.display()