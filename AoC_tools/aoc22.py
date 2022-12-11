import os
import pandas as pd
import time

# import AoC_tools.aoc_tools as aoc

aocdir = "C:/Users/lanni/Code/advent_of_code"


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

def s2n(input):
    """converts a list of strings to a list of ints"""
    if isinstance(input, list):
        return [int(x) for x in input]
    else:
        raise TypeError("Input should be a list of strings")

def read_input(path, sep1="\n", sep2=None):
    """reads in data separated by 1 or optionally 2 levels of separators"""
    with open(path) as file:
        data = file.read()
    if sep1 is not None:
        data = data.split(sep1)
        data = [d.strip() for d in data]
    if sep2 is not None:
        data = [d.split(sep2) for d in data]
        data = [list(map(lambda d: d.strip(), d)) for d in data]
    print("your data looks like this:")
    print(data)
    return data

def sorted_print(dict, by='key'):
    """prints a dictionary sorted by key"""
    if by == 'key':
        for key, value in sorted(dict.items(), key=lambda x: x[0]):
            print(f"{key} : {value}")
    elif by == 'value':
        for key, value in sorted(dict.items(), key=lambda x: x[1]):
            print(f"{key} : {value}")


def start():
    return time.time()


def end(start_time):
    executionTime = (time.time() - start_time)
    print('Execution time in seconds: ' + str(executionTime))


class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y


    def __str__(self):
        return f"""Position: ({self.x}, {self.y})"""

    @property
    def pos(self):
        return (self.x, self.y)

class Grid(object):
    # grid has x and y axis. In principle, x axis runs from low to high, y axis also, except if flip_y is
    # specified. If positions are given as row, column, r/c should be reversed to x/y (specify matrix=True).

    # Grid() should create an object based on dictionary of positions and values. Use default values if no value is
    # specified. If no dictionary is available, use Grid.make().

    def __init__(self, points, values, na=" "):
        self.points = points
        self.values = values
        self.na = na

    @staticmethod
    def read(data, rowsep='\n', colsep=" "):
        """reads a list of lists, a list of strings, or a single string and returns a grid"""
        # print("\ninput:")
        # print(data, "\n")
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
            # data = [row.split(colsep) for row in rows]
        elif isinstance(data, list):
            # if the elements of the lists are not lists themselves, split them up into lists.
            if isinstance(data[0], str):
                data = [row.split(colsep) for row in data]
        points = {}
        values = {}
        # rows
        nrows = len(data)
        ncols = len(data[0])
        for r in range(nrows):
            # columns
            for c in range(ncols):
                points[(c, r)] = Point(c, r)
                values[(c, r)] = data[r][c]
        return Grid(points, values)

    def transpose(self):
        points = self.points
        values = self.values
        points_t = {(p.y, p.x): Point(p.y, p.x) for p in points.values()}
        values_t = {(key[1], key[0]): value for key, value in values.items()}
        self.points = points_t
        self.values = values_t

    def flip_v(self):
        """flip a grid vertically"""
        points = self.points
        values = self.values
        points_fv = {(self.x_max - p.x, p.y): Point(self.x_max - p.x, p.y) for p in points.values()}
        values_fv = {((self.x_max - key[0]), key[1]): value for key, value in values.items()}
        self.points = points_fv
        self.values = values_fv

    def flip_h(self):
        """flip a grid horizontally"""
        points = self.points
        values = self.values
        points_fh = {(p.x, self.y_max - p.y): Point(p.x, self.y_max - p.y) for p in points.values()}
        values_fh = {(key[0], (self.y_max - key[1])): value for key, value in values.items()}
        self.points = points_fh
        self.values = values_fh

    @property
    def x_min(self):
        """lowest value on x-axis"""
        x_values = [point.x for point in self.points.values()]
        return min(x_values)

    @property
    def x_max(self):
        """highest value on x-axis"""
        x_values = [point.x for point in self.points.values()]
        return max(x_values)

    @property
    def x_range(self):
        return (self.x_min, self.x_max)

    @property
    def y_min(self):
        """lowest value on y-axis"""
        y_values = [point.y for point in self.points.values()]
        return min(y_values)

    @property
    def y_max(self):
        """highest value on y-axis"""
        y_values = [point.y for point in self.points.values()]
        return max(y_values)

    @property
    def y_range(self):
        return (self.y_min, self.y_max)

    @property
    def dim(self):
        dim_x = abs((self.x_max - self.x_min) + 1)
        dim_y = abs((self.y_max - self.y_min) + 1)
        return (dim_x, dim_y)

    @property
    def df(self):
        """creates a df in which empty positions are filled up with a specified NA value (" " by default),
        for the purpose of displaying the grid."""
        # column indices always run from low to high
        cols = [i for i in range(self.x_min, self.x_max + 1)]
        index = [i for i in range(self.y_min, self.y_max + 1)]
        df = pd.DataFrame(columns=cols, index=index)
        # first, fill up entirely with NAs (specified rather than pandas default)
        for col in df.columns:
            df[col].values[:] = self.na
        # add existing points to the df
        for key, value in self.values.items():
            df.loc[key[1], key[0]] = str(value)
        return df

    def display(self, transpose=False, show=True):
        """print the grid to console, with option to transpose it"""
        if transpose:
            grid = self.df.T
        else:
            grid = self.df
        lol = grid.values.tolist()
        image = ""
        for l in lol:
            image += " ".join(l) + "\n"
        if show:
            print(image)
        # return for testing purposes
        return(image)

    def get_neighbour(self, pos):
        # before returning a point, check that it exists on the grid. If not, return None.
        if pos in self.values.keys():
            return Point(*pos)
        else:
            return None

    def get_north(self, point):
        nb_pos = (point.x, point.y - 1)
        return self.get_neighbour(nb_pos)

    def get_northeast(self, point):
        nb_pos = (point.x + 1, point.y - 1)
        return self.get_neighbour(nb_pos)

    def get_east(self, point):
        nb_pos = (point.x + 1, point.y)
        return self.get_neighbour(nb_pos)

    def get_southeast(self, point):
        nb_pos = (point.x + 1, point.y + 1)
        return self.get_neighbour(nb_pos)

    def get_south(self, point):
        nb_pos = (point.x, point.y + 1)
        return self.get_neighbour(nb_pos)

    def get_southwest(self, point):
        nb_pos = (point.x - 1, point.y + 1)
        return self.get_neighbour(nb_pos)

    def get_west(self, point):
        nb_pos = (point.x - 1, point.y)
        return self.get_neighbour(nb_pos)

    def get_northwest(self, point):
        nb_pos = (point.x - 1, point.y - 1)
        return self.get_neighbour(nb_pos)

    def get_neighbours(self, point, n):
        """returns north, east, south and west neighbours for a point"""
        N = self.get_north(point)
        NE = self.get_northeast(point)
        E = self.get_east(point)
        SE = self.get_southeast(point)
        S = self.get_south(point)
        SW = self.get_southwest(point)
        W = self.get_west(point)
        NW = self.get_northwest(point)
        if n == 4:
            return [N, S, E, W]
        elif n == 8:
            return [N, NE, E, SE, S, SW, W, NW]
        else:
            raise ValueError("Invalid number of neighbours specified! Specify 4 or 8.")

    def nb_4dir(self, point):
        """returns a list of all neighbouring points in 4 directions until the end of the grid"""
        north = []
        south = []
        east = []
        west = []
        for x in reversed(range(0, point.x)):
            north.append(Point(x, point.y))
        for x in range(point.x+1, self.x_max + 1):
            south.append(Point(x, point.y))
        for y in reversed(range(0, point.y)):
            west.append(Point(point.x, y))
        for y in range(point.y+1, self.y_max + 1):
            east.append(Point(point.x, y))
        return (north, east, south, west)




# class Grid(object):
#
#     def __init__(self, positions, empty=' ', reverse=False, lookup_table=None, matrix=False):
#         """takes positions formatted in grid as (x, y). If positions are provided as (row,col),
#         all positions should be positive."""
#         # positions should be a dictionary with coordinates and corresponding values.
#         self.points = {key: Point(key, value) for key, value in positions.items()}
#         self.lookup_table = lookup_table
#         self.empty = empty
#         self.matrix = matrix
#
#
#     @staticmethod
#     def make(data, rowsep='\n', colsep=" "):
#         """takes a list of lists, a list of strings, or a single string and returns a grid"""
#         #print("\ninput:")
#         #print(data, "\n")
#         if isinstance(data, str):
#             # if data is a single string, it should be converted to a list of lists using the separators.
#             data_new = []
#             rows = data.split(rowsep)
#             for row in rows:
#                 row = row.split(colsep)
#                 # If row elements are not separated, split them
#                 if len(row) == 1:
#                     row = [char for char in row[0]]
#                 data_new.append(row)
#             data = data_new
#             #data = [row.split(colsep) for row in rows]
#         elif isinstance(data, list):
#             # if the elements of the lists are not lists themselves, split them up into lists.
#             if isinstance(data[0], str):
#                 data = [row.split(colsep) for row in data]
#         positions = {}
#         # rows
#         for row in range(len(data)):
#             # columns
#             for col in range(len(data[row])):
#                 positions[(col, row)] = data[row][col]
#         return Grid(positions, matrix=True)
#
#     @property
#     def x_min(self):
#         """lowest value on x-axis"""
#         x_values = [point[0][0] for point in self.points.items()]
#         return min(x_values)
#
#     @property
#     def x_max(self):
#         """highest value on x-axis"""
#         x_values = [point[0][0] for point in self.points.items()]
#         return max(x_values)
#
#     @property
#     def x_range(self):
#         return (self.x_min, self.x_max)
#
#     @property
#     def y_min(self):
#         """lowest value on y-axis"""
#         y_values = [point[0][1] for point in self.points.items()]
#         return min(y_values)
#
#     @property
#     def y_max(self):
#         """highest value on y-axis"""
#         y_values = [point[0][1] for point in self.points.items()]
#         return max(y_values)
#
#     @property
#     def y_range(self):
#         return (self.y_min, self.y_max)
#
#     @property
#     def dim(self):
#         dim_x = self.x_max + abs(self.x_min) + 1
#         dim_y = self.y_max + abs(self.y_min) + 1
#         return (dim_x, dim_y)
#
#     @property
#     def grid(self):
#         # column indices always run from low to high
#         cols = [i for i in range(self.x_min, self.x_max + 1)]
#
#         # in grid mode, the y-axis values go from high to low.
#         if self.x_min < 0 or (self.x_min >= 0 and not self.matrix):
#             index = [i for i in range(self.y_max, self.y_min - 1, -1)]
#             if self.x_min >= 0 and not self.matrix:
#                 print('Grid only has positive values; if it was specified as a matrix (r,c), specify "matrix=True" '
#                       'for correct display.')
#         # in matrix mode, the y-axis values go from low to high.
#         elif self.matrix:
#             index = [i for i in range(self.y_min, self.y_max + 1)]
#
#         df = pd.DataFrame(columns=cols, index=index)
#
#         # first, fill up with emtpy strings
#         for col in df.columns:
#             df[col].values[:] = self.empty
#
#         if self.lookup_table is None:
#             for point in self.points.values():
#                 df.loc[point.position[0], point.position[1]] = str(point.value)
#
#         elif self.lookup_table is not None:
#             for p in self.points:
#                 for key, value in self.lookup_table.items():
#                     if p.position == key:
#                         df.loc[p[0], p[1]] = str(value)
#         return df
#
#     def display(self, transpose=False, show=True):
#         """print the grid to console, with option to transpose it"""
#         if transpose:
#             grid = self.grid.T
#         else:
#             grid = self.grid
#         lol = grid.values.tolist()
#         image = ""
#         for l in lol:
#             image += " ".join(l) + "\n"
#         if show:
#             print(image)
#         return(image)

# TODO: integrate Point class in Grid, so a Grid contains Points instead of positions.

# class Point():
#
#     def __init__(self, pos):
#         self.row = pos[0]
#         self.col = pos[1]
#         try:
#             self.value = int(value)
#         except ValueError:
#             self.value = value
#
#     def __str__(self):
#         return f"({self.row}, {self.col}): {self.value}"
#
#     @property
#     def position(self):
#         return (self.row, self.col)
#
#     @property
#     def N(self):
#         return (self.row - 1, self.col)
#
#     @property
#     def S(self):
#         return (self.row + 1, self.col)
#
#     @property
#     def W(self):
#         return (self.row, self.col - 1)
#
#     @property
#     def E(self):
#         return (self.row, self.col + 1)
#
#
#     @property
#     def NE(self):
#         return (self.row - 1, self.col + 1)
#
#     @property
#     def SE(self):
#         return (self.row + 1, self.col + 1)
#
#     @property
#     def NW(self):
#         return (self.row + 1, self.col - 1)
#
#     @property
#     def SW(self):
#         return (self.row - 1, self.col - 1)
#
#
#     def get_neighbours(self, grid):
#         """obtain a point's neighbours' coordinates and values based on grid info.
#         First gets the neighbour's position based on NESW properties, then retrieves the values from
#         grid.positions, which is a dictionary of positions with their corresponding values."""
#         neighbours = []
#         #print("neighbours:")
#         try:
#             neighbour_S = Point(self.S, grid.points[self.S].value)
#             #print("South: ", neighbour_S)
#             neighbours.append(neighbour_S)
#         except KeyError as e:
#             pass
#         try:
#             neighbour_E = Point(self.E, grid.points[self.E].value)
#             #print("East: ", neighbour_E)
#             neighbours.append(neighbour_E)
#         except KeyError as e:
#             pass
#         try:
#             neighbour_N = Point(self.N, grid.points[self.N].value)
#             #print("North: ", neighbour_N)
#             neighbours.append(neighbour_N)
#         except KeyError as e:
#             pass
#         try:
#             neighbour_W = Point(self.W, grid.points[self.W].value)
#             #print("West: ", neighbour_W)
#             neighbours.append(neighbour_W)
#         except KeyError as e:
#             pass
#         return neighbours
#
#
#
#     def get_8neighbours(self, grid):
#         """obtain a point's neighbours' coordinates and values based on grid info.
#         First gets the neighbour's position based on NESW properties, then retrieves the values from
#         grid.positions, which is a dictionary of positions with their corresponding values."""
#         neighbours = self.get_neighbours(grid)
#         #print("neighbours:")
#         try:
#             neighbour_NE = Point(self.NE, grid.points[self.NE].value)
#             #print("South: ", neighbour_NE)
#             neighbours.append(neighbour_NE)
#         except KeyError as e:
#             pass
#         try:
#             neighbour_SE = Point(self.SE, grid.points[self.SE].value)
#             #print("East: ", neighbour_SE)
#             neighbours.append(neighbour_SE)
#         except KeyError as e:
#             pass
#         try:
#             neighbour_SW = Point(self.SW, grid.points[self.SW].value)
#             #print("North: ", neighbour_SW)
#             neighbours.append(neighbour_SW)
#         except KeyError as e:
#             pass
#         try:
#             neighbour_NW = Point(self.NW, grid.points[self.NW].value)
#             #print("West: ", neighbour_NW)
#             neighbours.append(neighbour_NW)
#         except KeyError as e:
#             pass
#         return neighbours