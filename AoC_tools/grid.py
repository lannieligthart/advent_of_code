import pandas as pd


class Grid(object):
    """grid has x and y axis. Both x and y axis run from low to high"""

    def __init__(self, values=dict(), na=" ", mode="rc"):
        self.values = values  # dictionary with string or int values and positions as keys
        self.na = na
        self.pos = None
        self.mode = mode # can be rc or xy depending on whether we're dealing with a matrix with rows and columns
        # or an xy type grid. Default is rc.

    @property
    def points(self):
        return list(self.values.keys())

    @classmethod
    def from_dict(cls, dictionary):
        """create a Grid based on a dictionary with positions as keys and values as dict values"""
        values = dict()
        for key, value in dictionary.items():
            values[key] = value
        grid = cls(values)
        return grid

    @classmethod
    def from_list(cls, list, char="#"):
        """takes a list of positions and creates a Grid that displays a specified character in the positions in the
        list"""
        values = dict()
        for item in list:
            values[item] = char
        grid = cls(values)
        return grid

    @staticmethod
    def read(data, rowsep='\n', colsep=" ", nosep=False):
        """reads a list of lists, a list of strings, or a single string and returns a grid"""
        # print("\ninput:")
        # print(data, "\n")
        if isinstance(data, str):
            # if data is a single string, it should be converted to a list of lists using the separators.
            data_new = []
            rows = data.split(rowsep)
            if not nosep:
                for row in rows:
                    row = row.split(colsep)
                    # If row elements are not separated, split them
                    if len(row) == 1:
                        row = [char for char in row[0]]
                    data_new.append(row)
            elif nosep:
                for row in rows:
                    row = list(row)
                    data_new.append(row)
            data = data_new
            # data = [row.split(colsep) for row in rows]
        elif isinstance(data, list):
            # if the elements of the lists are not lists themselves, split them up into lists.
            if isinstance(data[0], str):
                data = [list(row) for row in data]
        # rows
        nrows = len(data)
        ncols = len(data[0])
        points = dict()
        for r in range(nrows):
            # columns
            for c in range(ncols):
                points[(c, r)] = data[r][c]
        return Grid.from_dict(points)

    @staticmethod
    def pad_left(str, n):
        dif = n - len(str)
        prefix = " " * dif
        return prefix + str

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

    def includes(self, point):
        """check if grid includes a point with given coordinates"""
        if self.y_max >= point.y >= self.y_min and self.x_max >= point.x >= self.x_min:
            return True
        else:
            return False

    @property
    def c_min(self):
        """lowest value on x-axis"""
        c_values = [point[0] for point in self.points]
        return min(c_values)

    @property
    def c_max(self):
        """highest value on x-axis"""
        c_values = [point[0] for point in self.points]
        return max(c_values)

    @property
    def c_range(self):
        return (range(self.c_min, self.c_max + 1))

    @property
    def r_min(self):
        """lowest value on y-axis"""
        r_values = [point[1] for point in self.points]
        return min(r_values)

    @property
    def r_max(self):
        """highest value on y-axis"""
        r_values = [point[1] for point in self.points]
        return max(r_values)

    @property
    def r_range(self):
        return (range(self.r_min, self.r_max + 1))


    @property
    def x_min(self):
        """lowest value on x-axis"""
        x_values = [point[0] for point in self.points]
        return min(x_values)

    @property
    def x_max(self):
        """highest value on x-axis"""
        x_values = [point[0] for point in self.points]
        return max(x_values)

    @property
    def x_range(self):
        return (range(self.x_min, self.x_max + 1))

    @property
    def y_min(self):
        """lowest value on y-axis"""
        y_values = [point[1] for point in self.points]
        return min(y_values)

    @property
    def y_max(self):
        """highest value on y-axis"""
        y_values = [point[1] for point in self.points]
        return max(y_values)

    @property
    def y_range(self):
        return (range(self.y_min, self.y_max + 1))

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

    def display(self, transpose=False, hide=False, show_current=None):
        """print the grid to console, with option to transpose it.
        To show the current position, specify how to represent it with parameter show_current."""
        lengths = [len(str(value)) for value in self.values.values()]
        maxlen = max(lengths)
        if transpose:
            grid = self.df.T
        else:
            grid = self.df
        lol = grid.values.tolist()
        image = ""
        if show_current is not None:
            r, c = self.pos
            lol[r][c] = show_current
        for l in lol:
            # if values differ in length, pad with whitespace to make sure they align correctly
            # WHY ONLY LEFT SIDE?
            l = list(map(lambda x: self.pad_left(x, maxlen), l))
            image += " ".join(l) + "\n"
        if not hide:
            print(image)
        # return for testing purposes
        return image

    @staticmethod
    def parse_pos(pos, pos2=None):
        # if pos is already a tuple, do nothing.
        # if it's a point or an int, convert to tuple.
        if isinstance(pos, Point):
            pos = pos.pos
        elif isinstance(pos, int) and isinstance(pos2, int):
            pos = (pos, pos2)
        elif isinstance(pos, tuple) and len(pos) == 2:
            pass
        elif isinstance(pos, list) and len(pos) == 2:
            pos = list(pos)
        else:
            raise ValueError("Invalid position given")
        return pos

    def get_value(self, pos):
        if pos is None:
            pos = self.pos
        return self.values[pos]

    def set_value(self, value, pos):
        if pos is None:
            pos = self.pos
        self.values[pos] = value

    def add(self, point, value="#"):
        if isinstance(point, tuple):
            point = Point(*point)
        self.points[point.pos] = point
        self.values[point.pos] = value

    def remove(self, point):
        if isinstance(point, tuple):
            point = Point(point)
        self.points.pop(point.pos)
        self.values.pop(point.pos)

    def add_points(self, points, value="#"):
        for p in points:
            self.add(p, value)

    def get_neighbour(self, pos):
        # before returning a point, check that it exists on the grid. If not, return None.
        if pos in self.values.keys():
            return pos
        else:
            return None

    def get_north(self):
        r, c = self.pos
        nb_pos = (r - 1, c)
        return self.get_neighbour(nb_pos)

    def get_northeast(self):
        r, c = self.pos
        nb_pos = (r - 1, c + 1)
        return self.get_neighbour(nb_pos)

    def get_east(self):
        r, c = self.pos
        nb_pos = (r, c + 1)
        return self.get_neighbour(nb_pos)

    def get_southeast(self):
        r, c = self.pos
        nb_pos = (r + 1, c + 1)
        return self.get_neighbour(nb_pos)

    def get_south(self):
        r, c = self.pos
        nb_pos = (r + 1, c)
        return self.get_neighbour(nb_pos)

    def get_southwest(self):
        r, c = self.pos
        nb_pos = (r + 1, c - 1)
        return self.get_neighbour(nb_pos)

    def get_west(self):
        r, c = self.pos
        nb_pos = (r, c - 1)
        return self.get_neighbour(nb_pos)

    def get_northwest(self):
        r, c = self.pos
        nb_pos = (r - 1, c - 1)
        return self.get_neighbour(nb_pos)

    def get_neighbours(self, n=4, direction=None):
        """returns north, east, south and west neighbours for a point"""
        N = self.get_north()
        NE = self.get_northeast()
        E = self.get_east()
        SE = self.get_southeast()
        S = self.get_south()
        SW = self.get_southwest()
        W = self.get_west()
        NW = self.get_northwest()
        if n == 4:
            all_nb = [N, S, E, W]
            return [nb for nb in all_nb if nb is not None]
        elif n == 8 and direction is None:
            all_nb = [N, NE, E, SE, S, SW, W, NW]
            return [nb for nb in all_nb if nb is not None]
        elif n == 8 and direction == "N":
            all_nb = [N, NE, NW]
            return [nb for nb in all_nb if nb is not None]
        elif n == 8 and direction == "S":
            all_nb = [S, SE, SW]
            return [nb for nb in all_nb if nb is not None]
        elif n == 8 and direction == "E":
            all_nb = [E, SE, NE]
            return [nb for nb in all_nb if nb is not None]
        elif n == 8 and direction == "W":
            all_nb = [W, SW, NW]
            return [nb for nb in all_nb if nb is not None]
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
        for x in range(point.x + 1, self.x_max + 1):
            south.append(Point(x, point.y))
        for y in reversed(range(0, point.y)):
            west.append(Point(point.x, y))
        for y in range(point.y + 1, self.y_max + 1):
            east.append(Point(point.x, y))
        return north, east, south, west

    def add_line(self, line, char="#"):
        """takes a Line object and adds its points to the grid"""
        for point in line.points:
            self.points[point.pos] = point
            self.values[point.pos] = char

    def move(self, drc):
        if self.mode == "rc":
            r, c = self.pos
            if drc == "U":
                r -= 1
            elif drc == "D":
                r += 1
            elif drc == "R":
                c += 1
            elif drc == "L":
                c -= 1
            if r not in self.r_range or c not in self.c_range:
                raise IndexError("moving off grid!")
            else:
                self.pos = (r, c)

        elif self.mode == "xy":
            x, y = self.pos
            if drc == "U":
                x += 1
            elif drc == "D":
                x -= 1
            elif drc == "R":
                y += 1
            elif drc == "L":
                y -= 1
            if x not in self.x_range or y not in self.y_range:
                raise IndexError("moving off grid!")
            else:
                self.pos = (x, y)
