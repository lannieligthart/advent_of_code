from AoC_tools.aoc22 import read_input

def get_options(stock, costs):
    options = [False, False, False, False, True] # buy orebot, buy claybot, buy obsbot, buy geobot, do nothing.
    # based on stock, fill options.
    # needed to buy an orebot:
    if stock[0] >= costs[0]:
        options[0] = True
    if stock[0] >= costs[1]:
        options[1] = True
    if stock[0] >= costs[2][0] and stock[1] >= costs[2][1]:
        options[2] = True
    if stock[0] >= costs[3][0] and stock[2] >= costs[3][1]:
        options[3] = True
    # option 4 is always true
    return options


data = read_input("testinput.txt", "\n")
data = [d.split() for d in data]

def keep_ints(los):
    return [int(s) for s in los if s.isdigit()]

def organize(n):
    return [n[0], n[1], (n[2], n[3]), (n[4], n[5])]


"""ore robot -> clay robot -> obsidian robot -> geode robot"""

class State(object):

    def __init__(self, stock, robots, costs):
        self.stock = stock
        self.robots = robots
        self.costs = costs

    @classmethod
    def new(cls, blueprint):
        stock = [0, 0, 0, 0]  # ore, clay, obsidian, geode
        robots = [1, 0, 0, 0]  # ore, clay, obsidian, geode
        costs = blueprint  # ore, ore, ore/clay, ore/obs
        return cls(stock, robots, costs)

    def __str__(self):
        return(f"Stock: {self.stock[0]} ore, {self.stock[1]} clay, {self.stock[2]} obsidian, {self.stock[3]} geodes\n"
               f"Robots: {self.robots[0]} ore, {self.robots[1]} clay, {self.robots[2]} obsidian, {self.robots[3]} geodes\n")



def buy_orebot(robots, stock, costs):
    robots[0] += 1
    stock[0] -= costs[0]
    return robots, stock, costs

def buy_claybot(robots, stock, costs):
    robots[1] += 1
    stock[0] -= costs[1]
    return robots, stock, costs

def buy_obsbot(robots, stock, costs):
    robots[2] += 1
    stock[0] -= costs[2][0]
    stock[1] -= costs[2][1]
    return robots, stock, costs

def buy_geobot(robots, stock, costs):
    robots[3] += 1
    stock[0] -= costs[3][0]
    stock[2] -= costs[3][1]
    return robots, stock, costs



def run(paths, states):
    # create an array for new possible paths
    newpaths = []
    newstates = []
    for i, path in enumerate(paths):
        # get the state belonging with the path
        state = states[i]
        # explore options
        options = get_options(state.stock, state.costs)
        # voor alle opties die er zijn, creëer een path
        for o in range(len(options)):
            if options[o]:
                newpath = path.copy()
                newpath.append(o)
                # run option on state
                stock = state.stock.copy()
                robots = state.robots.copy()
                costs = state.costs.copy()
                # update the new state with produce of one minute
                for i in range(4):
                    stock[i] += robots[i]
                if o == 0:
                    robots, stock, costs = buy_orebot(robots, stock, costs)
                elif o == 1:
                    robots, stock, costs = buy_claybot(robots, stock, costs)
                elif o == 2:
                    robots, stock, costs = buy_obsbot(robots, stock, costs)
                elif o == 3:
                    robots, stock, costs = buy_geobot(robots, stock, costs)
                newstate = State(stock, robots, costs)
                newpaths.append(newpath)
                newstates.append(newstate)

    return newpaths, newstates

def get_n(blueprint):
    paths = [[]]
    states = [State.new(blueprint)]
    for x in range(24):
        print("Round", x+1)
        paths, states, = run(paths, states)
        n_clay = []
        n_geo = []
        n_obs = []
        for s in states:
            n_clay.append(s.stock[1])
            n_obs.append(s.stock[2])
            n_geo.append(s.stock[3])
        print(max(n_clay), max(n_obs), max(n_geo))
        if len(n_geo) > 0:
            print(max(n_geo))
        if max(n_geo) > 0:
            selected_states = []
            selected_paths = []
            for i in range(len(states)):
                if states[i].stock[3] == max(n_geo):
                    selected_states.append(states[i])
                    selected_paths.append(paths[i])
            states = selected_states
            paths = selected_paths
        # if max(n_obs) > 0:
        #     selected_states = []
        #     selected_paths = []
        #     for i in range(len(states)):
        #         if states[i].stock[2] == max(n_obs):
        #             selected_states.append(states[i])
        #             selected_paths.append(paths[i])
        #     states = selected_states
        #     paths = selected_paths
    return max(n_geo)

data = list(map(keep_ints, data))
data = list(map(organize, data))

results = []
for i in range(len(data)):
    blueprint = data[i]
    print(f"Blueprint: {i+1}")
    result = get_n(blueprint)
    results.append(result)

total = 0
for e, r in enumerate(results):
    print((e + 1), r)
    total += (e + 1) * r

print(total)

#