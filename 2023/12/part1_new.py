from AoC_tools import aoc22 as aoc
# get all combinations
import itertools

with open("input.txt") as file:
    data = file.read().split("\n")

def check_fit(string, groups, original_string, original_groups):
    #print(f"calling check_fit with arguments {string}, {groups}, {original_string}, {original_groups}.")
    # only adds to the count once all groups have been processed and no hashes are found in the remaining string.
    if len(groups) == 0 and "#" not in string:
        print("adding 1!")
        #print(output)
        n_options[(original_string, tuple(original_groups))] += 1
        return 1

    elif len(groups) == 0 and "#" in string:
        return 0

    elif len(string) == 0 and len(groups) > 0:
        return 0

    def dot(string, groups):
        check_fit(string[1:], tuple(groups), original_string, tuple(original_groups))
        return 1

    def pound(string, groups, n):
        # if this is the end of the string and it fits, empty them and call check_fit one last time
        if len(string) == n and "." not in string:
            check_fit('', groups[1:], original_string, tuple(original_groups))
            return 1
        # if not the end of the string, check if the current group fits and then proceed to the next group
        elif len(string) > n and "." not in string[0:n] and string[n] != "#":
            check_fit(string[n + 1:], tuple(groups[1:]), original_string, tuple(original_groups))
            return 1
        # if this group is exactly the length of the remaining string and it fits:
        elif len(string) == n and "." not in string[0:n]:
            check_fit('', tuple([]), original_string, tuple(original_groups))
            return 1
        else:
            # if it doesn't fit, this is where it ends.
            return 0

    # else, we proceed with the groups and string remaining at this point.
    n = groups[0]
    char = string[0]

    if char == "#":
        out = pound(string, groups, n)
    elif char == ".":
        out = dot(string, groups)
    elif char == "?":
        out = dot(string, groups) + pound(string, groups, n)
    else:
        raise RuntimeError

    #print(string, groups, "->", out)
    return out


n_options = dict()

output = 0
for d in data:
    string, groups = d.split()
    groups = list(map(int, groups.split(",")))
    n_options[(string, tuple(groups))] = 0
    original_string = string
    original_groups = groups
    output += check_fit(string, tuple(groups), original_string, tuple(original_groups))


aoc.dprint(n_options)
total = 0
for v in n_options.values():
    total += v
print(total)
