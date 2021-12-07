import AoC_tools.aoc_tools as aoc

state = aoc.string2list('input.txt', sep=",", numeric=True)

def run():
    for i in range(len(state)):
        if state[i] == 0:
            state.append(8)
            state[i] = 6
        else:
            state[i] -= 1
    #print(state)

for i in range(80):
    #print("after", i+1, "days:")
    run()
print(len(state))

assert len(state) == 362740