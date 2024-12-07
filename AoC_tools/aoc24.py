import os
import pandas as pd
import time

aocdir = "C:/Users/rlt700/OneDrive - Vrije Universiteit Amsterdam/Code/advent_of_code"

def check_result(filename, result, test, real, start_time=None):
    print(f"Result based on {filename}: {result}")

    if filename == "testinput.txt":
        assert result == test

    elif filename == "input.txt":
        assert result == real
    if start_time is not None:
        end(start_time)

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
    #open(file1, 'a').close()
    open(file2, 'a').close()
    open(inputfile, 'a').close()
    open(testfile, 'a').close()
    standard_content = """
from AoC_tools import aoc24 as aoc

s = aoc.start()
infile = "testinput.txt"
#infile = "input.txt"

with open(infile) as f:
    data = f.read()


#aoc.check_result(infile, result, testanswer, realanswer, s)
"""
    with open(file1, "w") as f:
        f.write(standard_content)



def s2n(input):
    """converts a list of strings to a list of ints"""
    if isinstance(input, list):
        return [int(x) for x in input]
    else:
        raise TypeError("Input should be a list of strings")

def read_input(path, sep1="\n", sep2=None, strip=True):
    """reads in data separated by 1 or optionally 2 levels of separators"""
    with open(path) as file:
        data = file.read()
    if sep1 is not None:
        data = data.split(sep1)
        if strip:
            data = [d.strip() for d in data]
    if sep2 is not None:
        data = [d.split(sep2) for d in data]
        if strip:
            data = [list(map(lambda d: d.strip(), d)) for d in data]
    print("your data looks like this:")
    print(data)
    return data

def dprint(dict):
    for key, value in dict.items():
        print(key, value)

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


def pad(str, n):
    dif = n - len(str)
    prefix = " "*dif
    return prefix + str

def find_cycle(seq, minlen=2, offset_range=100):
    """detects repetitive patterns in a sequence and returns the period. When there's an offset, it will
    only detect the pattern if start_pos > offset.
    minlen is the minimum length the repeat should have (in case there are shorter repetitive patterns in the offset
    range).
    NB: scans only the first detected repeat!"""
    def findperiod(seq, offset, minlen):
        for length in range(minlen, len(seq)):
            rep = seq[offset:length + offset]
            if seq[length + offset: 2*length + offset] == rep and seq[2*length + offset: 3*length + offset] == rep:
                return length

    for offset in range(offset_range):
        period = findperiod(seq, offset, minlen)
        if period is not None:
            break
    return(period, offset)

def transpose(lol):
    return list(map(list, zip(*lol)))

def get_nb(pos):
    r, c = pos
    return [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]

def flood_fill(data, r, c):
    """takes a matrix and a start position, returns filled up matrix"""
    done = set()
    queue = [(r, c)]
    while len(queue) > 0:
        r, c = queue.pop(0)
        if data[r][c] != "#" and (r, c) not in done:
            data[r][c] = "X"
            done.add((r, c))
        nb = aoc.get_nb((r, c))
        # if these neigbours are on the grid, not in done, and not a "#" convert them and add their neighbours to the queue
        for n in nb:
            if on_grid(data, n) and data[r][c] != "#" and n not in queue and n not in done:
                queue.append(n)
    return data


class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"""Position: ({self.x}, {self.y})"""

    @property
    def pos(self):
        return (self.x, self.y)

    def mhd(self, other):
        """manhattan distance"""
        return abs(self.x - other.x) + abs(self.y - other.y)

    @property
    def N(self):
        return Point(self.x, self.y - 1)

    @property
    def S(self):
        return Point(self.x, self.y + 1)

    @property
    def W(self):
        return Point(self.x - 1, self.y)

    @property
    def E(self):
        return Point(self.x + 1, self.y)


class Vector(Point):

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Vector(x, y)

    def __mul__(self, other):
        # multiply by another vector
        if isinstance(other, Vector):
            x = self.x * other.x
            y = self.y * other.y
            return Vector(x, y)
        # multiply by an int
        elif isinstance(other, int):
            x = self.x * other
            y = self.y * other
            return Vector(x, y)
        else:
            raise TypeError("Vector can only be multiplied by Vector or int")



class Line(object):

    def __init__(self, points):
        """basically a series of points representing a horizontal or vertical line between two positions"""
        # TODO: add support for diagonals
        self.points = points

    @classmethod
    def draw(cls, v1, v2):
        """takes two positions (vectors or points? currently vectors only) and creates points at and between those positions"""
        points = []
        dif = v2 - v1
        if dif.x > 0:
            for i in range(dif.x + 1):
                p = Point(v1.x + i, v1.y + 0)
                points.append(p)
        elif dif.x < 0:
            for i in range(0, dif.x - 1, -1):
                p = Point(v1.x + i, v1.y + 0)
                points.append(p)
        elif dif.y > 0:
            for i in range(dif.y + 1):
                p = Point(v1.x + 0, v1.y + i)
                points.append(p)
        elif dif.y < 0:
            for i in range(0, dif.y - 1, -1):
                p = Point(v1.x + 0, v1.y + i)
                points.append(p)
        return cls(points)

class Grid(object):
    """grid has x and y axis. Both x and y axis run from low to high"""

    def __init__(self, points=dict(), values=dict(), na=" "):
        self.points = points # dictionary with Point objects and positions as keys
        self.values = values # dictionary with string or int values and positions as keys
        self.na = na

    @classmethod
    def from_dict(cls, dictionary):
        """create a Grid based on a dictionary with positions as keys and values as dict values"""
        points = dict()
        values = dict()
        for key, value in dictionary.items():
            points[key] = Point(*key)
            values[key] = value
        grid = cls(points, values)
        return grid

    @classmethod
    def from_list(cls, list, char="#"):
        """takes a list of positions and creates a Grid that displays a specified character in the positions in the
        list"""
        points = dict()
        values = dict()
        for item in list:
            if isinstance(item, Point):
                points[item.pos] = item
                values[item.pos] = char
            else:
                points[item] = Point(*item)
                values[item] = char
        grid = cls(points, values)
        return grid

    @staticmethod
    def read(data, rowsep='\n', colsep=" ", nosep=False):
        """reads a list of lists, a list of strings, or a single string and returns a grid"""
        # TODO: moet ook een lijst van strings in kunnen lezen zonder colsep ertussen
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
        lengths = [len(str(value)) for value in self.values.values()]
        maxlen = max(lengths)
        if transpose:
            grid = self.df.T
        else:
            grid = self.df
        lol = grid.values.tolist()
        image = ""
        for l in lol:
            # if values differ in length, pad with whitespace to make sure they align correctly
            l = list(map(lambda x: pad(x, maxlen), l))
            image += " ".join(l) + "\n"
        if show:
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
        elif isinstance(pos,list) and len(pos) == 2:
            pos = list(pos)
        else:
            raise ValueError("Invalid position given")
        return pos

    def get_value(self, pos):
        return self.values[pos]

    def set_value(self, value, pos):
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

    def get_neighbours(self, point, n, direction=None):
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
        for x in range(point.x+1, self.x_max + 1):
            south.append(Point(x, point.y))
        for y in reversed(range(0, point.y)):
            west.append(Point(point.x, y))
        for y in range(point.y+1, self.y_max + 1):
            east.append(Point(point.x, y))
        return north, east, south, west

    def add_line(self, line, char="#"):
        """takes a Line object and adds its points to the grid"""
        for point in line.points:
            self.points[point.pos] = point
            self.values[point.pos] = char



class Node(object):
    """Node for use in a doubly (linear or circular) linked list"""
    def __init__(self, id, number):
        self.id = id
        self.number = number
        self.next = None
        self.previous = None

    def __str__(self):
        result = f"""
self: {self.number}
previous: {self.previous.number}
next: {self.next.number}"""
        return result


class CircularLinkedList:

    def __init__(self, head):
        self.head = head

    def __str__(self):
        start = self.head
        result = []
        while True:
            result.append(self.head.number)
            self.head = self.head.next
            if self.head == start:
                return str(result)

    def remove(self):
        node = self.head
        self.head.previous.next  = self.head.next
        self.head.next.previous = self.head.previous
        # stel de volgende node in als head
        self.head = self.head.next
        node.next = None
        node.previous = None
        return node

    def move_forward(self, n):
        for x in range(n):
            self.head = self.head.next

    def move_backward(self, n):
        for x in range(n):
            self.head = self.head.previous

    def insert_before(self, node):
        previous = self.head.previous
        self.head.previous = node
        node.next = self.head
        node.previous = previous
        node.next.previous = node
        previous.next = node

    def move_node(self, steps):
        node = self.remove()
        if steps > 0:
            self.move_forward(steps)
        elif steps < 0:
            self.move_backward(abs(steps))
        self.insert_before(node)