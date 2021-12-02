import os

aocdir = "C:/Users/Admin/SURFdrive/Code/advent_of_code"

def display_grid(positions, lookup_table=None):
    """takes two dictionaries as input: positions with their values, and a lookup table that specifies
    how each value should be visualized. If value should simply be visualized as itself, no lookup table is needed."""
    x_range = [p[0] for p in positions]
    y_range = [p[1] for p in positions]

#    print(min(x_range), max(x_range))
#    print(min(y_range), max(y_range))

    dim_x = max(x_range) + abs(min(x_range))
    dim_y = max(y_range) + abs(min(y_range))
    #print(dim_x, dim_y)

    cols = [i for i in range(min(x_range), max(x_range)+1)]
    index = [i for i in range(max(y_range), min(y_range)-1, -1)]

#    print(cols)
#    print(index)

    import pandas as pd
    #
    grid = pd.DataFrame(columns=cols, index=index)
    for col in grid.columns:
        grid[col].values[:] = ' '

    if lookup_table is None:
        for key, value in positions.items():
            grid.loc[key[1], key[0]] = value

    elif lookup_table is not None:
        for p in positions:
            for key, value in lookup_table.items():
                if positions[p] == key:
                    grid.loc[p[1], p[0]] = value

    lol = grid.values.tolist()
    for l in lol:
        print(" ".join(l))

def lprint(list):
    """prints the elements of a list on separate lines (e.g. for lists with custom objects in them"""
    for item in list:
        print(item)

def newday(year, day):
    """initializes a new day folder"""
    newdir = os.path.join(aocdir, str(year), str(day))
    file1 = os.path.join(newdir, "part1.py")
    file2 = os.path.join(newdir, "part2.py")
    inputfile = os.path.join(newdir, "input.txt")
    testfile = os.path.join(newdir, "testinput.txt")
    if not os.path.exists(newdir):
        os.mkdir(newdir)
    open(file1, 'a').close()
    open(file2, 'a').close()
    open(inputfile, 'a').close()
    open(testfile, 'a').close()


def lines2list(path, numeric=False, display=True):
    """converts a text file with multiple lines into a list with one element per line"""
    with open(path) as f:
        data = f.read().splitlines()
    if numeric:
        data = [int(d) for d in data]
    if display:
        print("Your input looks like this:")
        print(data)
        print("")
    return data

def string2list(path, sep=" ", numeric=False, display=True):
    """splits a single long string into a list"""
    with open(path) as f:
        data = f.read().split(sep=sep)
    if numeric:
        data = [int(d) for d in data]
    if display:
        print("Your input looks like this:")
        print(data)
        print("")
    return data

def split_list(data, sep=" "):
    """further splits the elements of a list, creating a list of lists"""
    for i in range(len(data)):
        data[i] = data[i].split(sep)
    return data

def read_grid(path, display=True):
    """reads a text file representing a grid; assumes each row of the grid is on a
    separate line in the text file. Returns the grid dictionary used as input for the display function."""
    data = lines2list(path, display=False)
    data = [[char for char in line] for line in data]
    positions = {}
    for i in range(len(data)):
        for j in range(len(data[i])):
            positions[(i, j)] = data[i][j]
    if display:
        print("Your grid looks like this:")
        display_grid(positions)
        print("")
    return positions
