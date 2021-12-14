import unittest
import AoC_tools.aoc_tools as aoc

class TestGrid(unittest.TestCase):

    def test_make_grid(self):
        data = {
            (-2, -2): 'C',
            (-2, -1): 'X',
            (-2, 0): 'X',
            (-2, 1): 'X',
            (-2, 2): 'D',
            (-1, -2): 'X',
            (-1, -1): 'X',
            (-1, -0): 'X',
            (-1, 1): 'X',
            (-1, 2): 'X',
            (0, -2): 'o',
            (0, -1): 'o',
            (0, 0): 'o',
            (0, 1): 'o',
            (0, 2): 'o',
            (1, -2): 'X',
            (1, -1): 'X',
            (1, 0): 'X',
            (1, 1): 'X',
            (1, 2): 'X',
            (2, -2): 'A',
            (2, -1): 'X',
            (2, 0): 'X',
            (2, 1): 'X',
            (2, 2): 'B'}
        grid = aoc.Grid(data)
        image = grid.display()
        expected = """A X X X B
X X X X X
o o o o o
X X X X X
C X X X D
"""
        self.assertEqual(image, expected)

    def test_read_string(self):
        data = """A X X X B
X X X X X
o o o o o
X X X X X
C X X X D"""
        grid = aoc.Grid.make(data)
        image = grid.display()
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
        grid = aoc.Grid.make(data)
        image = grid.display()
        expected = """A X X X B
X X X X X
o o o o o
X X X X X
C X X X D
"""
        self.assertEqual(image, expected)

    def test_read_list(self):
        data = ["A X X X B", "X X X X X", "o o o o o", "X X X X X", "C X X X D"]
        grid = aoc.Grid.make(data)
        image = grid.display()
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
        grid = aoc.Grid.make(data)
        image = grid.display()
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
        grid = aoc.Grid.make(data)
        image = grid.display(transpose=True)
        expected = """A X o X C
X X o X X
X X o X X
X X o X X
B X o X D
"""
        self.assertEqual(image, expected)

    # if coordinates are provided as row, col (positive values only) instead of (x,y)
    def test_matrix_mode(self):
        """if coordinates are provided as (r, c) matrix mode should be specified to display them
        correctly"""
        rc_data = {
            ( 0,  0): 'X',
            ( 1,  0): 'X',
            ( 2,  0): 'o',
            ( 0,  1): 'X',
            ( 1,  1): 'X',
            ( 2,  1): 'o',
            ( 0,  2): 'B',
            ( 1,  2): 'X',
            ( 2,  2): 'o'}
        grid = aoc.Grid(rc_data, matrix=True)
        image = grid.display()
        expected = """X X B
X X X
o o o
"""
        self.assertEqual(expected, image)

    def test_rc_values_matrix_mode_off(self):
        """if coordinates are provided as (r, c) and matrix is not specified, display will be upside down with a
        warning"""
        data = {
            (0, 0): 'X',
            (1, 0): 'X',
            (2, 0): 'o',
            (0, 1): 'X',
            (1, 1): 'X',
            (2, 1): 'o',
            (0, 2): 'B',
            (1, 2): 'X',
            (2, 2): 'o'}
        grid = aoc.Grid(data)
        image = grid.display()
        expected = """o o o
X X X
X X B
"""
        # TODO add exception and test raise
        self.assertEqual(expected, image)



if __name__ == '__main__':
    unittest.main()
