infile = "input.txt"
#infile = "testinput.txt"
part = 1

with open(infile) as f:
    data = [list(map(int, line.split())) for line in f]

def check(deltas):
    """check conditions: if the first two conditions are both false, or the latter is false, return False"""
    if not (all(d > 0 for d in deltas) or all(d < 0 for d in deltas)) or any(abs(d) >= 4 for d in deltas):
        return False
    return True

safe = []

for levels in data:
    # get deltas
    deltas = [levels[i] - levels[i - 1] for i in range(1, len(levels))]
    # if the line is safe, append to the safe list
    if check(deltas):
        safe.append(levels)
        #print(f"{levels} is safe")
    # if not safe yet, we need to apply a leave-one-out procedure to check if that makes it safe (part 2 only)
    else:
        if part == 2:
            for i in range(len(levels)):
                # generate the levels with one left out
                l_loo = levels.copy()
                del(l_loo[i])
                # get deltas
                deltas = [l_loo[i] - l_loo[i - 1] for i in range(1, len(l_loo))]
                if check(deltas):
                    safe.append(deltas)
                    #print(f"{levels} is safe")
                    break


# check answers

if infile == "input.txt" and part == 1:
    assert len(safe) == 524
elif infile == "testinput.txt" and part == 1:
    assert len(safe) == 2

if infile == "input.txt" and part == 2:
    assert len(safe) == 569
elif infile == "testinput.txt" and part == 2:
    assert len(safe) == 4

