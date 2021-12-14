import pandas as pd

class Grid(object):

    def __init__(self, positions, empty=' ', lookup_table=None, matrix=False):
        """takes positions formatted in grid as (x, y). If positions are provided as (row,col),
        all positions should be positive."""
        # positions should be a dictionary with coordinates and corresponding values.
        self.points = {key: (key, value) for key, value in positions.items()}
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

        # the y-axis values go from low to high.
        index = [i for i in range(self.y_min, self.y_max + 1)]

        df = pd.DataFrame(columns=cols, index=index)

        # first, fill up with emtpy strings
        for col in df.columns:
            df[col].values[:] = self.empty

        if self.lookup_table is None:
            for point in self.points.values():
                df.loc[point[0][1], point[0][0]] = point[1]
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


def fold(oldpoints, axis, cutoff):
    # to fold along the y axis, divide the points into two groups: y > ymax/2
    coords = list(oldpoints.keys())
    if axis == 'y':
        y_coords = [point[1] for point in coords]
        print(y_coords)
        y_max = max(y_coords)

        for i in range(len(y_coords)):
            if y_coords[i] > cutoff:
                # y_coords[i] = y_max - y_coords[i]
                y_coords[i] = cutoff - (y_coords[i] - cutoff)
        print(y_coords)
        newpoints = {}
        for i in range(len(y_coords)):
            newpoints[(coords[i][0], y_coords[i])] = "#"
        print(oldpoints)
        print(" ")
        print(newpoints)
        return newpoints
    elif axis == 'x':
        x_coords = [point[0] for point in coords]
        print(x_coords)
        x_max = max(x_coords)

        for i in range(len(x_coords)):
            if x_coords[i] > cutoff:
                x_coords[i] = cutoff - (x_coords[i] - cutoff)
        print(x_coords)
        newpoints = {}
        for i in range(len(x_coords)):
            newpoints[(x_coords[i], coords[i][1])] = "#"
        print(oldpoints)
        print(" ")
        print(newpoints)
        return newpoints


with open("input.txt") as f:
    data = f.read().split("\n\n")
points = data[0].split("\n")
instructions = data[1].split("\n")
points = [p.split(",") for p in points]
points = {(int(p[0]), int(p[1])): "#" for p in points}

instructions = [i.replace("fold along ", "").split("=") for i in instructions]
for i in instructions:
    points = fold(points, axis=i[0], cutoff=int(i[1]))

paper = Grid(points, empty='.')
paper.display()
