from AoC_tools.aoc22 import read_input
from collections import deque


def keep_ints(los):
    return [int(s) for s in los if s.isdigit()]

def organize(n):
    return [n[0], n[1], (n[2], n[3]), (n[4], n[5])]


"""ore robot -> clay robot -> obsidian robot -> geode robot"""

class State(object):

    def __init__(self, stock, robots):
        self.stock = stock
        self.robots = robots

    @classmethod
    def new(cls):
        stock = [0, 0, 0, 0]  # ore, clay, obsidian, geode
        robots = [1, 0, 0, 0] # ore, clay, obsidian, geode
        return cls(stock, robots)

    def __str__(self):
        return(f"Stock: {self.stock[0]} ore, {self.stock[1]} clay, {self.stock[2]} obsidian, {self.stock[3]} geodes\n"
               f"Robots: {self.robots[0]} ore, {self.robots[1]} clay, {self.robots[2]} obsidian, {self.robots[3]} geodes\n")



    def production(self, blueprint):
        # how many cycles are needed to produce each type of robot?
        production = [0, 0, 0, 0]
        if self.robots[0] > 0:
            # aantal orebots dat gemaakt kan worden is het aantal orebots gedeeld door de kosten van een orebot, afgerond naar beneden
            production[0] =  self.robots[0] // blueprint[0]
        # clay bots kosten ook ore
        if self.robots[0] > 0:
            # aantal claybots dat gemaakt kan worden is het aantal orebots gedeeld door de kosten van een claybot, afgerond naar beneden
            production[1] = self.robots[0] // blueprint[1]
        # obsidian bots kosten ore en clay
        if self.robots[0] > 0 and self.robots[1] > 0:
            production[2] = min(blueprint[2][0] // self.robots[0], blueprint[2][1] // self.robots[1])
        # geode bots kosten ore en obsidian
        if self.robots[0] > 0 and self.robots[2] > 0:
            production[2] = min(blueprint[3][0] // self.robots[0], blueprint[3][1] // self.robots[2])
        return production

    def max_needed(self, blueprint):
        max_ore = blueprint[0] + blueprint[1] + blueprint[2][0] + blueprint[3][0]
        max_clay = blueprint[2][1]
        max_obs = blueprint[3][1]
        return max_ore, max_clay, max_obs


    def get_options(self, blueprint):
        # blueprint contains the cost of each option
        options = [False, False, False, False, True] # buy orebot, buy claybot, buy obsbot, buy geobot, do nothing.
        # if all robots can already be made with the production of a single round, explore no further options
        # if min(self.production(blueprint)) > 0:
        #     return options
        # based on stock, fill options.
        # needed to buy an orebot:
        if self.stock[0] >= blueprint[0] and self.robots[0] < self.max_needed(blueprint)[0]:
            options[0] = True
        if self.stock[0] >= blueprint[1] and self.robots[1] < self.max_needed(blueprint)[1]:
            options[1] = True
        if self.stock[0] >= blueprint[2][0] and self.stock[1] >= blueprint[2][1] and self.robots[2] < self.max_needed(blueprint)[2]:
            options[2] = True
        if self.stock[0] >= blueprint[3][0] and self.stock[2] >= blueprint[3][1]:
            options[3] = True
        # option 4 is always true
        return options

        # when a state already produces enough to create any type of bot in a single round, only option 4 is needed.
        # when a state can't possibly produce more in the future than is already being produced by the current best state, prune it
        # when a state is exactly the same as another state, prune it

def buy_orebot(robots, stock, costs):
    #print(f"Spend {costs[0]} ore to buy an orebot")
    robots[0] += 1
    stock[0] -= costs[0]
    return robots, stock, costs

def buy_claybot(robots, stock, costs):
    #print(f"Spend {costs[1]} ore to buy a claybot")
    robots[1] += 1
    stock[0] -= costs[1]
    return robots, stock, costs

def buy_obsbot(robots, stock, costs):
    #print(f"Spend {costs[2][0]} ore and {costs[2][1]} clay to buy an obsidian bot")
    robots[2] += 1
    stock[0] -= costs[2][0]
    stock[1] -= costs[2][1]
    return robots, stock, costs

def buy_geobot(robots, stock, costs):
    #print(f"Spend {costs[3][0]} ore and {costs[3][1]} obsidian to buy a geode bot")
    robots[3] += 1
    stock[0] -= costs[3][0]
    stock[2] -= costs[3][1]
    return robots, stock, costs


def update_state(state, blueprint, option):
    # run option on state
    stock = state.stock.copy()
    robots = state.robots.copy()
    costs = blueprint
    # update the new state with harvest of the previous minute (robots still being produced do not harvest anything yet,
    # so first we update the harvest, and then we add the new bot)
    for i in range(4):
        stock[i] += robots[i]
    # depending on the option setting (0-4, where 4 means do nothing), add a robot (or not).
    if option == 0:
        robots, stock, costs = buy_orebot(robots, stock, costs)
    elif option == 1:
        robots, stock, costs = buy_claybot(robots, stock, costs)
    elif option == 2:
        robots, stock, costs = buy_obsbot(robots, stock, costs)
    elif option == 3:
        robots, stock, costs = buy_geobot(robots, stock, costs)
    return State(stock, robots)

data = read_input("testinput.txt", "\n")
data = [d.split() for d in data]
data = list(map(keep_ints, data))
data = list(map(organize, data))

# test blueprint 1 path as described in example
# 0 buy orebot, 1 buy claybot, 2 buy obsbot, 3 buy geobot, 4 do nothing.
# options = [4, 4, 1, 4, 1, 4, 1, 4, 4, 4, 2, 1, 4, 4, 2, 4, 4, 3, 4, 4, 3, 4, 4, 4]
# blueprint = data[0]
# state = State.new()
# for i, o in enumerate(options):
#     print(f"minute {i + 1}")
#     state = update_state(state, blueprint, o)
#     print(state)
#
# assert state.stock == [6, 41, 8, 9]
# assert state.robots == [1, 4, 2, 2]

# test production method

stock = [0, 0, 0, 0]
blueprint = data[0]
state = State(stock, [2, 0, 0, 0])
# prod = state.production(blueprint)
# assert prod == [0, 1, 0, 0]
# state = State(stock, [4, 0, 0, 0])
# prod = state.production(blueprint)
# assert prod == [1, 2, 0, 0]
# state = State(stock, [3, 0, 0, 0])
# prod = state.production(blueprint)
# assert prod == [0, 1, 0, 0]
# state = State(stock, [7, 0, 0, 0])
# prod = state.production(blueprint)
# assert prod == [1, 3, 0, 0]
# state = State(stock, [3, 14, 0, 0])
# prod = state.production(blueprint)
# assert prod == [0, 1, 1, 0]

# assert state.max_needed(blueprint) == (11, 14, 7)
# assert state.max_needed(data[1]) == (11, 8, 12)

# test options
stock = [20, 20, 20, 20]
blueprint = data[0]
state = State(stock, [11, 0, 0, 0])
assert state.get_options(blueprint) == [False, True, True, True, True]


# investigate all options

state = State.new()
blueprint = data[1]
states = deque([state])
max_geodes = 0
max_obs = 0

for x in range(24):
    print(f"minute {x+1}")
    newstates = deque()
    while len(states) > 0:
        s = states.pop()
        if s.stock[3] >= max_geodes:
            options = s.get_options(blueprint)
            for i in range(len(options)):
                if options[i]:
                    newstates.append(update_state(s, blueprint, i))
    states = newstates.copy()
    n_obs = [s.stock[2] for s in states]
    n_geodes = [s.stock[3] for s in states]
    max_obs = max(n_obs)
    max_geodes = max(n_geodes)
    print(len(states))

print(max_geodes)


def run_blueprint(blueprint):
    state = State.new()
    states = deque([state])
    max_geodes = 0

    for x in range(24):
        print(f"minute {x + 1}")
        newstates = deque()
        while len(states) > 0:
            s = states.pop()
            if s.stock[3] >= max_geodes:
                options = s.get_options(blueprint)
                for i in range(len(options)):
                    if options[i]:
                        newstates.append(update_state(s, blueprint, i))
        states = newstates.copy()
        n_geodes = [s.stock[3] for s in states]
        max_geodes = max(n_geodes)
        print(len(states))

    return max_geodes

max_n_geodes = []
for d in data:
    max_n_geodes.append(run_blueprint(d))

print(max(max_n_geodes))