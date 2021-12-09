import os
import pandas as pd
import time

aocdir = "C:/Users/Admin/SURFdrive/Code/advent_of_code"


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

def sorted_print(dict, by='key'):
    """prints a dictionary sorted by key"""
    if by == 'key':
        for key, value in sorted(dict.items(), key=lambda x: x[0]):
            print(f"{key} : {value}")
    elif by == 'value':
        for key, value in sorted(dict.items(), key=lambda x: x[1]):
            print(f"{key} : {value}")

def split_list(data, sep=" "):
    """further splits the elements of a list, creating a list of lists"""
    for i in range(len(data)):
        data[i] = data[i].split(sep)
    return data


def start():
    return time.time()

def end(start_time):
    executionTime = (time.time() - start_time)
    print('Execution time in seconds: ' + str(executionTime))


class Grid(object):

    def __init__(self, positions, empty=' ', lookup_table=None, matrix=True):
        """takes positions formatted in matrix style as (row, col). If positions are provided as (x,y) coordinates,
        set matrix to True to reverse them upon creating the grid"""
        self.positions = positions # dictionary with coordinates and corresponding values.
        if not matrix:
            self.reverse_positions()
        self.lookup_table = lookup_table
        self.empty = empty

    def reverse_positions(self):
        newdict = {}
        for key, value in self.positions.items():
            x, y = key
            newkey = (y, x)
            newdict[newkey] = value
        self.positions = newdict

    @staticmethod
    def make(data, rowsep='\n', colsep=" "):
        """takes a list of lists, a list of strings, or a single string and returns a grid"""
        #print("\ninput:")
        #print(data, "\n")
        if isinstance(data, str):
            # if data is a single string, it should be converted to a list of lists using the separators.
            rows = data.split(rowsep)
            data = [row.split(colsep) for row in rows]
        elif isinstance(data, list):
            # if the elements of the lists are not lists themselves, split them up into lists.
            if isinstance(data[0], str):
                data = [row.split(colsep) for row in data]
        positions = {}
        # rows
        for i in range(len(data)):
            # columns
            for j in range(len(data[i])):
                positions[(i, j)] = data[i][j]
        return Grid(positions)

    @property
    def x_min(self):
        """lowest value on x-axis"""
        x_values = [p[0] for p in self.positions]
        return min(x_values)

    @property
    def x_max(self):
        """highest value on x-axis"""
        x_values = [p[0] for p in self.positions]
        return max(x_values)

    @property
    def x_range(self):
        return (self.x_min, self.x_max)

    @property
    def y_min(self):
        """lowest value on y-axis"""
        y_values = [p[0] for p in self.positions]
        return min(y_values)

    @property
    def y_max(self):
        """highest value on y-axis"""
        y_values = [p[0] for p in self.positions]
        return max(y_values)

    @property
    def y_range(self):
        return (self.y_min, self.y_max)

    @property
    def dim(self):
        dim_x = self.x_max + abs(self.x_min) + 1
        dim_y = self.y_max + abs(self.y_min) + 1
        return (dim_x, dim_y)

    @property
    def grid(self):
        # column indices always run from low to high
        cols = [i for i in range(self.x_min, self.x_max + 1)]

        if self.x_min < 0:
            # if the grid has positive values as well as negative ones, the y-axis values go from high to low.
            index = [i for i in range(self.y_max, self.y_min - 1, -1)]
        # if the grid only has positive values, the axis values behave like those in the lower right quadrant, except
        # the y-axis values go from low to high (essentially like a matrix).
        else:
            index = [i for i in range(self.y_min, self.y_max + 1)]

        grid = pd.DataFrame(columns=cols, index=index)

        # first, fill up with emtpy strings
        for col in grid.columns:
            grid[col].values[:] = self.empty

        if self.lookup_table is None:
            for key, value in self.positions.items():
                grid.loc[key[0], key[1]] = str(value)

        elif self.lookup_table is not None:
            for p in self.positions:
                for key, value in self.lookup_table.items():
                    if self.positions[p] == key:
                        grid.loc[p[0], p[1]] = str(value)
        return grid

    def display(self, transpose=False, show=True):
        """print the grid to console, with option to transpose it"""
        if transpose:
            grid = self.grid.T
        else:
            grid = self.grid
        lol = grid.values.tolist()
        image = ""
        for l in lol:
            image += " ".join(l) + "\n"
        if show:
            print(image)
        return(image)

# TODO: integrate Point class in Grid, so a Grid contains Points instead of positions.

class Point():

    def __init__(self, pos, value):
        self.x = pos[0]
        self.y = pos[1]
        self.value = int(value)

    def __str__(self):
        return f"({self.x}, {self.y}): {self.value}"

    @property
    def position(self):
        return (self.x, self.y)

    @property
    def N(self):
        return (self.x - 1, self.y)

    @property
    def S(self):
        return (self.x + 1, self.y)

    @property
    def W(self):
        return (self.x, self.y - 1)

    @property
    def E(self):
        return (self.x, self.y + 1)


    def get_neighbours(self, grid):
        """obtain a point's neighbours' coordinates and values based on grid info.
        First gets the neighbour's position based on NESW properties, then retrieves the values from
        grid.positions, which is a dictionary of positions with their corresponding values."""
        neighbours = []
        #print("neighbours:")
        try:
            neighbour_S = Point(self.S, grid.positions[self.S])
            #print("South: ", neighbour_S)
            neighbours.append(neighbour_S)
        except KeyError as e:
            pass
        try:
            neighbour_E = Point(self.E, grid.positions[self.E])
            #print("East: ", neighbour_E)
            neighbours.append(neighbour_E)
        except KeyError as e:
            pass
        try:
            neighbour_N = Point(self.N, grid.positions[self.N])
            #print("North: ", neighbour_N)
            neighbours.append(neighbour_N)
        except KeyError as e:
            pass
        try:
            neighbour_W = Point(self.W, grid.positions[self.W])
            #print("West: ", neighbour_W)
            neighbours.append(neighbour_W)
        except KeyError as e:
            pass
        return neighbours



