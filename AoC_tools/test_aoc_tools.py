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


if __name__ == '__main__':
    unittest.main()
