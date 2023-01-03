from AoC_tools.aoc22 import read_input, start, end
from collections import deque


def keep_ints(los):
    return [int(s) for s in los if s.isdigit()]

def organize(n):
    return [n[0], n[1], (n[2], n[3]), (n[4], n[5])]


"""ore robot -> clay robot -> obsidian robot -> geode robot"""

class State(object):

    def __init__(self, stock, robots, minutes_left):
        self.stock = stock
        self.robots = robots
        self.minutes_left = minutes_left

    @classmethod
    def new(cls):
        stock = [0, 0, 0, 0]  # ore, clay, obsidian, geode
        robots = [1, 0, 0, 0] # ore, clay, obsidian, geode
        return cls(stock, robots, 32)

    def __str__(self):
        return(f"Stock: {self.stock[0]} ore, {self.stock[1]} clay, {self.stock[2]} obsidian, {self.stock[3]} geodes\n"
               f"Robots: {self.robots[0]} ore, {self.robots[1]} clay, {self.robots[2]} obsidian, {self.robots[3]} geodes\n")

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
        # iets is alleen een optie als dat ook het doel was binnen deze branch (of er was nog geen doel gesteld).
        if self.stock[0] >= blueprint[0] and self.robots[0] < self.max_needed(blueprint)[0]:
            options[0] = True
        if self.stock[0] >= blueprint[1] and self.robots[1] < self.max_needed(blueprint)[1]:
            options[1] = True
        if self.stock[0] >= blueprint[2][0] and self.stock[1] >= blueprint[2][1] and self.robots[2] < self.max_needed(blueprint)[2]:
            options[2] = True
        if self.stock[0] >= blueprint[3][0] and self.stock[2] >= blueprint[3][1]:
            options[3] = True
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
    minutes_left = state.minutes_left - 1
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
    return State(stock, robots, minutes_left)


data = read_input("testinput.txt", "\n")
data = [d.split() for d in data]
data = list(map(keep_ints, data))
data = list(map(organize, data))

# test blueprint 1 path as described in example
# 0 buy orebot, 1 buy claybot, 2 buy obsbot, 3 buy geobot, 4 do nothing.
# logged_states = []
# options = [4, 4, 1, 4, 1, 4, 1, 4, 4, 4, 2, 1, 4, 4, 2, 4, 4, 3, 4, 4, 3, 4, 4, 4]
# blueprint = data[0]
# state = State.new()
# for i, o in enumerate(options):
#     print(f"minute {i + 1}")
#     state = update_state(state, blueprint, o)
#     logged_states.append((tuple(state.robots), tuple(state.stock)))
#     print(state)
#
# assert state.stock == [6, 41, 8, 9]
# assert state.robots == [1, 4, 2, 2]

# part 2 test run should produce 56
logged_states = []
options = [4, 4, 4, 4, 0, 4, 1, 1, 1, 1, 1, 1, 1, 2, 4, 2, 2, 4, 2, 3, 2, 3, 3, 3, 4, 3, 3, 4, 3, 3, 3, 4]
blueprint = data[0]
state = State.new()
for i, o in enumerate(options):
    print(f"minute {i + 1}")
    state = update_state(state, blueprint, o)
    logged_states.append((tuple(state.robots), tuple(state.stock)))
    print(state)



data = read_input("testinput.txt", "\n")
data = [d.split() for d in data]
data = list(map(keep_ints, data))
data = list(map(organize, data))


state = State.new()
blueprint = data[1]
states = deque([state])
max_geodes = 0
max_obs = 0

def is_duplicate(state, state_dict):
    # check if state is a duplicate of one that has already been considered
    fingerprint = (tuple(state.robots), tuple(state.stock))
    if fingerprint not in state_dict:
        return False
    else:
        return True


def run_blueprint(blueprint):
    state = State.new()
    states = deque([state])
    max_clay = 0
    max_obs = 0
    max_geodes = 0
    print("blueprint:")
    print(blueprint)
    for x in range(32):
        print(f"\nMinute {x + 1}")
        state_dict = {}
        newstates = deque()
        while len(states) > 0:
            s = states.pop()
            options = s.get_options(blueprint)
            for i in range(len(options)):
                if options[i]:
                    newstate = update_state(s, blueprint, i)
                    # update max
                    if newstate.stock[1] > max_clay:
                        max_clay = newstate.stock[1]
                    if newstate.stock[2] > max_obs:
                        max_obs = newstate.stock[2]
                    if newstate.stock[3] > max_geodes:
                        max_geodes = newstate.stock[3]
                    if not is_duplicate(newstate, state_dict):
                        # add to the state dictionary
                        state_dict[(tuple(newstate.robots), tuple(newstate.stock))] = newstate
                        newstates.append(newstate)
        if logged_states[x] not in state_dict:
            print("halt")
        states = newstates.copy()
        print("Number of states:", len(states))
        print("Max clay:", max_clay)
        print("Max obsidian:", max_obs)
        print("Max geodes:", max_geodes)
    print(max_geodes)
    return max_geodes

start = start()

max_n_geodes = []
#run_blueprint(data[1])
for i, d in enumerate(data[0:1]):
    print(f"Blueprint #{i +1} of {len(data)}")
    max_n_geodes.append((i+1, run_blueprint(d)))
    print(d)

total = 0
for i in range(len(max_n_geodes)):
    total += max_n_geodes[i][0] * max_n_geodes[i][1]

print(total)

end = end(start)