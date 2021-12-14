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

def lines2lol(path, numeric=False, display=True):
    """converts a text file with multiple lines into a list with one element per line"""
    with open(path) as f:
        data = f.read().splitlines()
    for i in range(len(data)):
        tmp = data[i].split()
        if len(tmp) == 1:
            tmp = tmp[0]
            if isinstance(tmp[0], str):
                tmp = [char for char in tmp]
        data[i] = tmp
    if numeric:
        for i in range(len(data)):
            for j in range(len(data[i])):
                data[i][j] = int(data[i][j])
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

    def __init__(self, positions, empty=' ', lookup_table=None, matrix=False):
        """takes positions formatted in grid as (x, y). If positions are provided as (row,col),
        all positions should be positive."""
        # positions should be a dictionary with coordinates and corresponding values.
        self.points = {key: Point(key, value) for key, value in positions.items()}
        self.lookup_table = lookup_table
        self.empty = empty
        self.matrix = matrix


    @staticmethod
    def make(data, rowsep='\n', colsep=" "):
        """takes a list of lists, a list of strings, or a single string and returns a grid"""
        #print("\ninput:")
        #print(data, "\n")
        if isinstance(data, str):
            # if data is a single string, it should be converted to a list of lists using the separators.
            data_new = []
            rows = data.split(rowsep)
            for row in rows:
                row = row.split(colsep)
                # If row elements are not separated, split them
                if len(row) == 1:
                    row = [char for char in row[0]]
                data_new.append(row)
            data = data_new
            #data = [row.split(colsep) for row in rows]
        elif isinstance(data, list):
            # if the elements of the lists are not lists themselves, split them up into lists.
            if isinstance(data[0], str):
                data = [row.split(colsep) for row in data]
        positions = {}
        # rows
        for row in range(len(data)):
            # columns
            for col in range(len(data[row])):
                positions[(col, row)] = data[col][row]
        return Grid(positions, matrix=True)

    @property
    def x_min(self):
        """lowest value on x-axis"""
        x_values = [point[0][0] for point in self.points.items()]
        return min(x_values)

    @property
    def x_max(self):
        """highest value on x-axis"""
        x_values = [point[0][0] for point in self.points.items()]
        return max(x_values)

    @property
    def x_range(self):
        return (self.x_min, self.x_max)

    @property
    def y_min(self):
        """lowest value on y-axis"""
        y_values = [point[0][1] for point in self.points.items()]
        return min(y_values)

    @property
    def y_max(self):
        """highest value on y-axis"""
        y_values = [point[0][1] for point in self.points.items()]
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

        # in grid mode, the y-axis values go from high to low.
        if self.x_min < 0 or (self.x_min >= 0 and not self.matrix):
            index = [i for i in range(self.y_max, self.y_min - 1, -1)]
            if self.x_min >= 0 and not self.matrix:
                print('Grid only has positive values; if it was specified as a matrix (r,c), specify "matrix=True" '
                      'for correct display.')
        # in matrix mode, the y-axis values go from low to high.
        elif self.matrix:
            index = [i for i in range(self.y_min, self.y_max + 1)]

        df = pd.DataFrame(columns=cols, index=index)

        # first, fill up with emtpy strings
        for col in df.columns:
            df[col].values[:] = self.empty

        if self.lookup_table is None:
            for point in self.points.values():
                df.loc[point.position[0], point.position[1]] = str(point.value)

        elif self.lookup_table is not None:
            for p in self.points:
                for key, value in self.lookup_table.items():
                    if p.position == key:
                        df.loc[p[0], p[1]] = str(value)
        return df

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
        self.row = pos[0]
        self.col = pos[1]
        try:
            self.value = int(value)
        except ValueError:
            self.value = value

    def __str__(self):
        return f"({self.row}, {self.col}): {self.value}"

    @property
    def position(self):
        return (self.row, self.col)

    @property
    def N(self):
        return (self.row - 1, self.col)

    @property
    def S(self):
        return (self.row + 1, self.col)

    @property
    def W(self):
        return (self.row, self.col - 1)

    @property
    def E(self):
        return (self.row, self.col + 1)


    @property
    def NE(self):
        return (self.row - 1, self.col + 1)

    @property
    def SE(self):
        return (self.row + 1, self.col + 1)

    @property
    def NW(self):
        return (self.row + 1, self.col - 1)

    @property
    def SW(self):
        return (self.row - 1, self.col - 1)


    def get_neighbours(self, grid):
        """obtain a point's neighbours' coordinates and values based on grid info.
        First gets the neighbour's position based on NESW properties, then retrieves the values from
        grid.positions, which is a dictionary of positions with their corresponding values."""
        neighbours = []
        #print("neighbours:")
        try:
            neighbour_S = Point(self.S, grid.points[self.S].value)
            #print("South: ", neighbour_S)
            neighbours.append(neighbour_S)
        except KeyError as e:
            pass
        try:
            neighbour_E = Point(self.E, grid.points[self.E].value)
            #print("East: ", neighbour_E)
            neighbours.append(neighbour_E)
        except KeyError as e:
            pass
        try:
            neighbour_N = Point(self.N, grid.points[self.N].value)
            #print("North: ", neighbour_N)
            neighbours.append(neighbour_N)
        except KeyError as e:
            pass
        try:
            neighbour_W = Point(self.W, grid.points[self.W].value)
            #print("West: ", neighbour_W)
            neighbours.append(neighbour_W)
        except KeyError as e:
            pass
        return neighbours



    def get_8neighbours(self, grid):
        """obtain a point's neighbours' coordinates and values based on grid info.
        First gets the neighbour's position based on NESW properties, then retrieves the values from
        grid.positions, which is a dictionary of positions with their corresponding values."""
        neighbours = self.get_neighbours(grid)
        #print("neighbours:")
        try:
            neighbour_NE = Point(self.NE, grid.points[self.NE].value)
            #print("South: ", neighbour_NE)
            neighbours.append(neighbour_NE)
        except KeyError as e:
            pass
        try:
            neighbour_SE = Point(self.SE, grid.points[self.SE].value)
            #print("East: ", neighbour_SE)
            neighbours.append(neighbour_SE)
        except KeyError as e:
            pass
        try:
            neighbour_SW = Point(self.SW, grid.points[self.SW].value)
            #print("North: ", neighbour_SW)
            neighbours.append(neighbour_SW)
        except KeyError as e:
            pass
        try:
            neighbour_NW = Point(self.NW, grid.points[self.NW].value)
            #print("West: ", neighbour_NW)
            neighbours.append(neighbour_NW)
        except KeyError as e:
            pass
        return neighbours