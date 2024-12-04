import unittest
import AoC_tools.aoc_tools as aoc

class TestPoint(unittest.TestCase):

    def test_point_coordinates(self):
        point = aoc.Point(1,2)
        self.assertEqual(point.x, 1)
        self.assertEqual(point.y, 2)

    def test_print_point(self):
        point = aoc.Point(1, 2)
        string = point.__str__()
        self.assertEqual(string, "Position: (1, 2)")


class TestGridMake(unittest.TestCase):

    def test_xrange(self):
        points = [(0, 1), (3, 4)]
        g = aoc.Grid.make(points)
        self.assertEqual(g.x_range, (0, 3))

    def test_yrange(self):
        points = [(0, 1), (3, 4)]
        g = aoc.Grid.make(points)
        self.assertEqual(g.y_range, (1, 4))

    def test_dim(self):
        points = [(0, 1), (3, 4)]
        g = aoc.Grid.make(points)
        self.assertEqual(g.dim, (4, 4))

    def test_dim_neg(self):
        points = [(-3, -1), (3, 2)]
        g = aoc.Grid.make(points)
        self.assertEqual(g.dim, (7, 4))

    def test_positions(self):
        points = [(-3, -1), (3, 2)]
        g = aoc.Grid.make(points)
        self.assertEqual(g.positions, points)

    def test_values_single_value(self):
        points = [(-3, -1), (3, 2)]
        g = aoc.Grid.make(points, values="#")
        self.assertEqual(g.values, ['#', '#'])

    def test_values_list(self):
        points = [(-3, -1), (3, 2)]
        g = aoc.Grid.make(points, values=["#", "O"])
        self.assertEqual(g.values, ['#', 'O'])

class TestGridDisplay(unittest.TestCase):

    def test_grid_display(self):
        points = [(-3, -1), (3, 2)]
        g = aoc.Grid.make(points, na=".")
        result = g.display()
        expected = """X . . . . . .
. . . . . . .
. . . . . . .
. . . . . . X
"""
        self.assertEqual(expected, result)

class TestGridRead(unittest.TestCase):

    def test_read_string(self):
        data = """A X X X B
X X X X X
o o o o o
X X X X X
C X X X D"""
        g = aoc.Grid.read(data)
        image = g.display()
        expected = """A X X X B
X X X X X
o o o o o
X X X X X
C X X X D
"""
        self.assertEqual(image, expected)

    def test_read_string_without_sep(self):
        data = """AXXXB
XXXXX
ooooo
XXXXX
CXXXD"""
        g = aoc.Grid.read(data)
        image = g.display()
        expected = """A X X X B
X X X X X
o o o o o
X X X X X
C X X X D
"""
        self.assertEqual(image, expected)

    def test_read_list(self):
        data = ["A X X X B", "X X X X X", "o o o o o", "X X X X X", "C X X X D"]
        g = aoc.Grid.read(data)
        image = g.display()
        expected = """A X X X B
X X X X X
o o o o o
X X X X X
C X X X D
"""
        self.assertEqual(image, expected)

    def test_read_lol(self):
        data = [["A", "X", "X", "X", "B"],
                ["X", "X", "X", "X", "X"],
                ["o", "o", "o", "o", "o"],
                ["X", "X", "X", "X", "X"],
                ["C", "X", "X", "X", "D"]]
        g = aoc.Grid.read(data)
        image = g.display()
        expected = """A X X X B
X X X X X
o o o o o
X X X X X
C X X X D
"""
        self.assertEqual(image, expected)

    def test_display_transpose(self):
        data = """A X X X B
X X X X X
o o o o o
X X X X X
C X X X D"""
        g = aoc.Grid.read(data)
        image = g.display(transpose=True)
        expected = """A X o X C
X X o X X
X X o X X
X X o X X
B X o X D
"""
        self.assertEqual(image, expected)

    def test_make_single_value_grid_custom_na(self):
        positions = [(-2, -2), (-1,-1), (0, 0), (1, 1), (2, 2)]
        values = 'X'
        g = aoc.Grid.make(positions, values, na='.')
        image = g.display()
        expected = """X . . . .
. X . . .
. . X . .
. . . X .
. . . . X
"""
        self.assertEqual(image, expected)

    def test_make_single_value_grid_default_na(self):
        positions = [(-2, -2), (-1, -1), (0, 0), (1, 1), (2, 2)]
        values = 'X'
        g = aoc.Grid.make(positions, values)
        image = g.display()
        expected = """X        
  X      
    X    
      X  
        X
"""
        self.assertEqual(image, expected)


    def test_make_multi_value_grid(self):
        positions = [(-2, -2), (-1,-1), (0, 0), (1, 1), (2, 2)]
        values = ['X', 'X', 'O', 'X', 'X']
        g = aoc.Grid.make(positions, values, na='.')
        image = g.display()
        expected = """X . . . .
. X . . .
. . O . .
. . . X .
. . . . X
"""
        self.assertEqual(image, expected)

    def test_row_col_mode(self):
        """if coordinates are provided as (r, c) matrix mode should be specified to display them
        correctly"""
        positions = [(0, 0), (0, 4), (3, 0), (3, 4), (4, 2)]
        values = 'X'
        g = aoc.Grid.make(positions, values, na='.', xy=False)
        image = g.display()
        expected = """X . . . X
. . . . .
. . . . .
X . . . X
. . X . .
"""
        self.assertEqual(image, expected)

    def test_matrix_mode_neg(self):
        """if coordinates are provided as (r, c) matrix mode should be specified to display them
        correctly"""
        positions = [(-1, -1), (-1, 3), (2, -1), (2, 3), (3, 1)]
        values = 'X'
        g = aoc.Grid.make(positions, values, na='.', xy=False)
        image = g.display()
        expected = """X . . . X
. . . . .
. . . . .
X . . . X
. . X . .
"""
        self.assertEqual(image, expected)

