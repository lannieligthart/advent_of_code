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

    # if coordinates are provided as (x,y) instead of
    def test_xy_mode(self):
        data = {
            (-2, -2): 'C',
            (-1, -2): 'X',
            ( 0, -2): 'X',
            ( 1, -2): 'X',
            ( 2, -2): 'D',
            (-2, -1): 'X',
            (-1, -1): 'X',
            (-0, -1): 'X',
            ( 1, -1): 'X',
            ( 2, -1): 'X',
            (-2,  0): 'o',
            (-1,  0): 'o',
            ( 0,  0): 'o',
            ( 1,  0): 'o',
            ( 2,  0): 'o',
            (-2,  1): 'X',
            (-1,  1): 'X',
            ( 0,  1): 'X',
            ( 1,  1): 'X',
            ( 2,  1): 'X',
            (-2,  2): 'A',
            (-1,  2): 'X',
            ( 0,  2): 'X',
            ( 1,  2): 'X',
            ( 2,  2): 'B'}
        grid = aoc.Grid(data, matrix=False)
        image = grid.display()
        expected = """A X X X B
X X X X X
o o o o o
X X X X X
C X X X D
"""
        self.assertEqual(image, expected)

if __name__ == '__main__':
    unittest.main()
