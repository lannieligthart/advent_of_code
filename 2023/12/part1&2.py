import functools

# Implemented recursion and memoization, thanks reddit

@functools.cache
def dot(string, groups):
    return check_fit(string[1:], tuple(groups))


@functools.cache
def pound(string, groups, n):
    # if this is the end of the string and it fits, empty them and call check_fit one last time
    if len(string) == n and "." not in string:
        return check_fit('', groups[1:])

    # if not the end of the string, check if the current group fits and then proceed to the next group
    elif len(string) > n and "." not in string[0:n] and string[n] != "#":
        return check_fit(string[n + 1:], tuple(groups[1:]))
    # if this group is exactly the length of the remaining string and it fits:
    elif len(string) == n and "." not in string[0:n]:
        return check_fit('', tuple([]))
    else:
        # if it doesn't fit, this is where it ends.
        return 0


@functools.cache
def check_fit(string, groups):
    if len(groups) == 0 and "#" not in string:
        return 1

    elif len(groups) == 0 and "#" in string:
        return 0

    elif len(string) == 0 and len(groups) > 0:
        return 0

    # else, we proceed with the groups and string remaining at this point.
    n = groups[0]
    char = string[0]

    if char == "#":
        out = pound(string, groups, n)
    elif char == ".":
        out = dot(string, groups)
    elif char == "?":
        # NB: this is where the result of check_fit can end up being more than 0 or 1!
        # if pound returns 1, and dot goes to the next ? and again results in a call of dot as well as pound,
        # pound returns 1 and dot can return dot + pound which is > 1, etc, resulting in a potentially large number.
        out = dot(string, groups) + pound(string, groups, n)
    else:
        raise RuntimeError

    return out


with open("input.txt") as file:
    data = file.read().split("\n")

# part 1

output = 0
for d in data:
    string, groups = d.split()
    groups = list(map(int, groups.split(",")))
    output += check_fit(string, tuple(groups))

assert output == 7173

# part 2

data_unfolded = []
for d in data:
    seq, group_lengths = d.split()
    seq = [seq] * 5
    seq = "?".join(seq)
    gl = [group_lengths] * 5
    gl = ",".join(gl)
    d = seq + " " + gl
    data_unfolded.append(d)
data = data_unfolded

output = 0
for d in data:
    string, groups = d.split()
    groups = list(map(int, groups.split(",")))
    output += check_fit(string, tuple(groups))

assert output == 29826669191291