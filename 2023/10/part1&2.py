from AoC_tools import aoc22 as aoc

with open("input.txt") as file:
    data = file.read().split("\n")

# add padding so I don't mess up with indices on the edges
data.insert(0, '.' * len(data[0]))
data.append('.' * len(data[0]))
data = ["." + d + "." for d in data]
# make list of list so I can use row/column indexing
data = [list(d) for d in data]

# find start position
for r in range(len(data)):
    for c in range(len(data[0])):
        if data[r][c] == "S":
            startpos = (r, c)


def get_connected_pipes(nb_types, curtype):
    conn = {
        "S": ["N", "E", "S", "W"],
        "7": ["W", "S"],
        "F": ["E", "S"],
        "J": ["N", "W"],
        "L": ["N", "E"],
        "|": ["N", "S"],
        "-": ["E", "W"]
    }
    opposites = {"N": "S", "S": "N", "E": "W", "W": "E"}

    nb_pipes = dict()
    for nb in ["N", "E", "S", "W"]:
        # check of daar een neighbour zit.
        if nb_types[nb] != '.':
            nb_pipes[nb] = nb_types[nb]

    # for each of the neighbouring pipe types, check if they can be connected to the current pipe.
    # this depends on the types of both pipes and the direction of the connection.
    connected = []
    for direction, nb_type in nb_pipes.items():
        if direction in conn[curtype] and opposites[direction] in conn[nb_type]:
            connected.append(nb_pos[direction])
    return connected


# doorloop alle neighbours en check of ze accessible zijn vanaf de huidige positie.
visited = [startpos]
curpos = startpos
distance = 0
while True:
    curtype = data[curpos[0]][curpos[1]]
    # find neighbouring positions
    r, c = curpos
    nb_pos = {"N": (r-1, c), "S": (r + 1, c), "E": (r, c + 1), "W": (r, c - 1)}
    # find neighouring pipe types
    nb_types = {direction: data[pos[0]][pos[1]] for direction, pos in nb_pos.items()}
    options = get_connected_pipes(nb_types, curtype)
    options = [o for o in options if o not in visited]
    visited.append(curpos)
    distance += 1
    if len(options) == 0:
        break
    # normally there will be only one option, except the first time, so just pick first element
    curpos = options[0]
maxdist = distance/2
print(maxdist)
assert maxdist == 6613

# Part 2.
# replace all non-loop pipes by a dot
new_data = []
for r, d in enumerate(data):
    new_d = []
    for c, char in enumerate(d):
        if (r, c) in visited:
            new_d.append(char)
        else:
            new_d.append(".")
    new_data.append(new_d)

data = ["".join(d) for d in new_data]

# Now we only have the loop left in the data. For each line, count how many times the loop is crossed.
# Note that FJ and L7 count as one because they're bends in a vertical pipe, and - can be ignored altogether.
# NOTE: in my input, the S represents a J, so I have to replace that one too. Could probably code that so it will work
# on other inputs but I can't be bothered.

# translation 1 is only there to aid visualisation
def translate(data):
    maze_dict = {"S": "┘", "F": "┌", "J": "┘", "L": "└", "7": "┐"}
    for key, value in maze_dict.items():
        data = data.replace(key, value)
    return data

# translation 2 to convert all characters to something that counts as 1 crossing
def translate2(data):
    maze_dict = {"-": "", "┌┘": "|", "└┐": "|", "┌┐": "", "└┘": ""}
    for key, value in maze_dict.items():
        data = data.replace(key, value)
    return data

data = [translate(d) for d in data]
# visualize the loop
# for line in data:
#     print(line)

data = [translate2(d) for d in data]

def count(line):
    # Count number of pipes. Once you reach a dot, if the number of pipes is an odd number, count the dot.
    enclosed = 0
    pipes = 0
    for char in line:
        if char == "|":
            pipes += 1
        elif char == ".":
            if pipes % 2 == 1:
                enclosed += 1
    return enclosed

total_enclosed = sum([count(line) for line in data])
print(total_enclosed)

assert total_enclosed == 511
