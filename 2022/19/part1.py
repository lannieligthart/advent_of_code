from AoC_tools.aoc22 import read_input, start, end
from collections import deque


def keep_ints(los):
    return [int(s) for s in los if s.isdigit()]

def organize(n):
    return [n[0], n[1], (n[2], n[3]), (n[4], n[5])]


"""ore robot -> clay robot -> obsidian robot -> geode robot"""

class State(object):

    def __init__(self, stock, robots, minutes_left, block):
        self.stock = stock
        self.robots = robots
        self.minutes_left = minutes_left
        self.block = block

    @classmethod
    def new(cls):
        stock = [0, 0, 0, 0]  # ore, clay, obsidian, geode
        robots = [1, 0, 0, 0] # ore, clay, obsidian, geode
        block = [False, False, False, False]
        return cls(stock, robots, 24, block)

    @property
    def fingerprint(self):
        stock = self.stock.copy()
        robots = self.robots.copy()
        stock.extend(robots)
        stock.append(self.minutes_left)
        return tuple(stock)

    def __str__(self):
        return(f"Stock: {self.stock[0]} ore, {self.stock[1]} clay, {self.stock[2]} obsidian, {self.stock[3]} geodes\n"
               f"Robots: {self.robots[0]} ore, {self.robots[1]} clay, {self.robots[2]} obsidian, {self.robots[3]} geodes\n")

    def get_options(self, blueprint):
        # blueprint contains the cost of each option
        options = [False, False, False, False, True] # buy orebot, buy claybot, buy obsbot, buy geobot, do nothing.
        if self.stock[0] >= blueprint[0] and self.robots[0] < max_needed(blueprint)[0]:
            options[0] = True
        if self.stock[0] >= blueprint[1] and self.robots[1] < max_needed(blueprint)[1]:
            options[1] = True
        if self.stock[0] >= blueprint[2][0] and self.stock[1] >= blueprint[2][1] and self.robots[2] < max_needed(blueprint)[2]:
            options[2] = True
        if self.stock[0] >= blueprint[3][0] and self.stock[2] >= blueprint[3][1]:
            options[3] = True
        return options


def max_needed(blueprint):
    max_ore = max(blueprint[0], blueprint[1], blueprint[2][0], blueprint[3][0])
    max_clay = blueprint[2][1]
    max_obs = blueprint[3][1]
    return max_ore, max_clay, max_obs

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

def update_state(state, blueprint, option, options=None):
    # run option on state
    stock = state.stock.copy()
    robots = state.robots.copy()
    minutes_left = state.minutes_left - 1
    costs = blueprint
    block = state.block.copy()

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
    # if an option could have been chosen but wasn't, block it until something is bought that lowers the cost
    # such that the option is no longer feasible.
    for i in range(4):
        if options[i] and option == 4:
            block[i] = True
    # unblock options that are currently blocked but can't be afforded anymore
        if block[i] and not options[i]:
            block[i] = False
    #if the resources exceed the resources we could possibly need, they can be capped.
    # maximum we might need:
    # max_needed for this type * minutes_left - bots * minutes left
    for i in range(3):
        maxval = max_needed(blueprint)[i] * minutes_left
        stock[i] = min(stock[i], maxval)
    return State(stock, robots, minutes_left, block)

def max_prod(robots, stock, minutes_left):
    # aantal bots * aantal minuten over
    max_production = stock
    # for each next minute, we add the number of minutes left * robots
    for i in reversed(range(1, minutes_left + 1)):
        # per minuut komt erbij: het aantal minuten maal het aantal robots op dat moment.
        # daarna een robot toevoegen.
        max_production += i * robots
        robots += 1
    return max_production

def guaranteed(state):
    # aantal geode bots * aantal minuten over + current stock
    guaranteed = state.stock[3] + state.minutes_left * state.robots[3]
    return guaranteed

def run_blueprint(blueprint):
    state = State.new()
    states = deque([state])
    max_stock = [0, 0, 0, 0]
    guaranteed_max = 0
    maxval = max_needed(blueprint)
    # print("blueprint:")
    # print(blueprint)
    for x in range(24):
        #print(f"\nMinute {x + 1}")
        state_dict = {}
        newstates = deque()
        while len(states) > 0:
            if len(states) % 100000 == 0:
                print("states left to process:", len(states))
            s = states.pop()
            options = s.get_options(blueprint)
            for i in range(len(options)):
                if options[i]:
                    newstate = update_state(s, blueprint, i, options)
                    for idx in range(4):
                        if newstate.stock[idx] > max_stock[idx]:
                            max_stock[idx] = newstate.stock[idx]
                    if guaranteed(state) > guaranteed_max:
                        guaranteed_max = guaranteed(state)
                    if max_prod(newstate.robots[3], newstate.stock[3], newstate.minutes_left) < guaranteed_max:
                        continue
                    if newstate.fingerprint not in state_dict:
                        # add to the state dictionary
                        state_dict[newstate.fingerprint] = newstate
                        newstates.append(newstate)
        # if logged_states[x] not in state_dict:
        #     print("Missing a path!!")
        states = newstates.copy()
        #print("Number of states:", len(states))
        #print("Max stock:", max_stock)
        #end(start)
    print("Max stock:", max_stock)
    return max_stock[3]


data = read_input("input.txt", "\n")
data = [d.split() for d in data]
data = list(map(keep_ints, data))
data = list(map(organize, data))



state = State.new()
states = deque([state])
start = start()
max_n_geodes = []

for i, d in enumerate(data):
    print(f"Blueprint #{i +1} of {len(data)}")
    max_n_geodes.append((i+1, run_blueprint(d)))
    print(d)

total = 0
for i in range(len(max_n_geodes)):
    total += max_n_geodes[i][0] * max_n_geodes[i][1]

print(total)

end = end(start)