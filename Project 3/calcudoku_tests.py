"""
Project 3

CPE101
Spring 2021
Author: Jack Forrester
"""

import unittest
from unittest import mock
import calcudoku as c

class MyTest(unittest.TestCase):
    @mock.patch('calcudoku.input', create=True)
    def test_get_num_cages(self, mocked_input):
        mocked_input.side_effect = ['9']
        self.assertEqual(c.get_num_cages(), 9)
        mocked_input.side_effect = ['7']
        self.assertEqual(c.get_num_cages(), 7)
        mocked_input.side_effect = ['8']
        self.assertEqual(c.get_num_cages(), 8)


    @mock.patch('calcudoku.input', create=True)
    def test_get_cage_info(self, mocked_input):
        mocked_input.side_effect = ['9 3 0 5 6', '7 2 1 2', '10 3 3 8 13',
                '14 4 4 9 14 19', '3 1 7', '8 3 10 11 16', '13 4 12 17 21 22',
                '5 2 15 20', '6 3 18 23 24']
        self.assertEqual(c.get_cage_info(9),
                [[9, 3, 0, 5, 6],
                 [7, 2, 1, 2],
                 [10, 3, 3, 8, 13],
                 [14, 4, 4, 9, 14, 19],
                 [3, 1, 7],
                 [8, 3, 10, 11, 16],
                 [13, 4, 12, 17, 21, 22],
                 [5, 2, 15, 20],
                 [6, 3, 18, 23, 24]])
        mocked_input.side_effect = ['4 3 0 1 6', '8 3 2 7 12', '14 3 3 4 8',
                '15 4 5 10 11 15', '14 6 9 13 14 18 19 24', '11 3 16 20 21',
                '9 3 17 22 23']
        self.assertEqual(c.get_cage_info(7),
                [[4, 3, 0, 1, 6],
                 [8, 3, 2, 7, 12],
                 [14, 3, 3, 4, 8],
                 [15, 4, 5, 10, 11, 15],
                 [14, 6, 9, 13, 14, 18, 19, 24],
                 [11, 3, 16, 20, 21],
                 [9, 3, 17, 22, 23]])
        mocked_input.side_effect = ['7 3 0 1 2', '12 4 3 4 8 9',
                '17 6 5 7 10 11 12 13', '5 1 6', '11 3 14 19 24', '7 2 15 20',
                '5 3 16 17 21', '11 3 18 22 23']
        self.assertEqual(c.get_cage_info(8),
                [[7, 3, 0, 1, 2],
                 [12, 4, 3, 4, 8, 9],
                 [17, 6, 5, 7, 10, 11, 12, 13],
                 [5, 1, 6],
                 [11, 3, 14, 19, 24],
                 [7, 2, 15, 20],
                 [5, 3, 16, 17, 21],
                 [11, 3, 18, 22, 23]])


    def test_validate_rows(self):
        grid = [[1, 2, 5, 3, 1],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]]
        self.assertEqual(c.validate_rows(grid), False)
        grid = [[1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1]]
        self.assertEqual(c.validate_rows(grid), False)
        grid = [[3, 5, 2, 1, 4],
                [5, 1, 3, 4, 2],
                [2, 4, 1, 5, 3],
                [1, 2, 4, 3, 5],
                [4, 3, 5, 2, 1]]
        self.assertEqual(c.validate_rows(grid), True)
        grid = [[3, 5, 2, 1, 4],
                [4, 1, 3, 4, 2],
                [5, 4, 1, 5, 3],
                [1, 2, 4, 3, 5],
                [3, 3, 5, 2, 1]]
        self.assertEqual(c.validate_rows(grid), False)
        grid = [[3, 5, 2, 1, 4],
                [5, 1, 3, 4, 2],
                [5, 2, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]]
        self.assertEqual(c.validate_rows(grid), True)


    def test_validate_cols(self):
        grid = [[1, 2, 5, 3, 4],
                [1, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]]
        self.assertEqual(c.validate_cols(grid), False)
        grid = [[1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1]]
        self.assertEqual(c.validate_cols(grid), False)
        grid = [[3, 5, 2, 1, 4],
                [5, 1, 3, 4, 2],
                [2, 4, 1, 5, 3],
                [1, 2, 4, 3, 5],
                [4, 3, 5, 2, 1]]
        self.assertEqual(c.validate_cols(grid), True)
        grid = [[3, 5, 2, 1, 4],
                [5, 1, 3, 4, 2],
                [2, 4, 1, 5, 3],
                [1, 2, 4, 3, 5],
                [3, 4, 5, 2, 1]]
        self.assertEqual(c.validate_cols(grid), False)
        grid = [[3, 5, 2, 1, 4],
                [5, 1, 3, 4, 3],
                [4, 2, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]]
        self.assertEqual(c.validate_cols(grid), True)


    def test_validate_cages(self):
        cages = [[15, 5, 0, 5, 10, 15, 20],
                 [6, 2, 1, 6],
                 [16, 4, 2, 7, 8, 13],
                 [7, 2, 3, 4],
                 [7, 4, 9, 14, 18, 19],
                 [5, 2, 11, 12],
                 [6, 2, 16, 21],
                 [6, 2, 17, 22],
                 [7, 2, 23, 24]]
        grid = [[1, 2, 5, 3, 4],
                [4, 1, 2, 5, 3],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]]
        self.assertEqual(c.validate_cages(grid, cages), False)
        cages = [[9, 3, 0, 5, 6],
                 [7, 2, 1, 2],
                 [10, 3, 3, 8, 13],
                 [14, 4, 4, 9, 14, 19],
                 [3, 1, 7],
                 [8, 3, 10, 11, 16],
                 [13, 4, 12, 17, 21, 22],
                 [5, 2, 15, 20],
                 [6, 3, 18, 23, 24]]
        grid = [[1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1]]
        self.assertEqual(c.validate_cages(grid, cages), False)
        cages = [[9, 3, 0, 5, 6],
                 [7, 2, 1, 2],
                 [10, 3, 3, 8, 13],
                 [14, 4, 4, 9, 14, 19],
                 [3, 1, 7],
                 [8, 3, 10, 11, 16],
                 [13, 4, 12, 17, 21, 22],
                 [5, 2, 15, 20],
                 [6, 3, 18, 23, 24]]
        grid = [[3, 5, 2, 1, 4],
                [5, 1, 3, 4, 2],
                [2, 4, 1, 5, 3],
                [1, 2, 4, 3, 5],
                [4, 3, 5, 2, 1]]
        self.assertEqual(c.validate_cages(grid, cages), True)
        cages = [[9, 3, 0, 5, 6],
                 [7, 2, 1, 2],
                 [10, 3, 3, 8, 13],
                 [14, 4, 4, 9, 14, 19],
                 [3, 1, 7],
                 [8, 3, 10, 11, 16],
                 [13, 4, 12, 17, 21, 22],
                 [5, 2, 15, 20],
                 [6, 3, 18, 23, 24]]
        grid = [[3, 5, 2, 1, 4],
                [5, 1, 3, 4, 2],
                [2, 4, 1, 5, 3],
                [1, 2, 4, 3, 5],
                [3, 4, 5, 2, 1]]
        self.assertEqual(c.validate_cages(grid, cages), False)
        cages = [[9, 3, 0, 5, 6],
                 [7, 2, 1, 2],
                 [10, 3, 3, 8, 13],
                 [14, 4, 4, 9, 14, 19],
                 [3, 1, 7],
                 [8, 3, 10, 11, 16],
                 [13, 4, 12, 17, 21, 22],
                 [5, 2, 15, 20],
                 [6, 3, 18, 23, 24]]
        grid = [[3, 5, 2, 1, 4],
                [5, 1, 3, 4, 3],
                [2, 4, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]]
        self.assertEqual(c.validate_cages(grid, cages), True)


    def test_validate_all(self):
        cages = [[5, 2, 0, 5],
                 [8, 3, 1, 2, 6],
                 [8, 2, 3, 8],
                 [6, 3, 4, 9, 14],
                 [13, 3, 7, 12, 13],
                 [5, 2, 10, 15],
                 [14, 4, 11, 15, 20, 21],
                 [6, 3, 17, 18, 22],
                 [10, 3, 19, 23, 24]]
        grid = [[1, 2, 5, 3, 4],
                [1, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]]
        self.assertEqual(c.validate_all(grid, cages), False)
        cages = [[9, 3, 0, 5, 6],
                 [7, 2, 1, 2],
                 [10, 3, 3, 8, 13],
                 [14, 4, 4, 9, 14, 19],
                 [3, 1, 7],
                 [8, 3, 10, 11, 16],
                 [13, 4, 12, 17, 21, 22],
                 [5, 2, 15, 20],
                 [6, 3, 18, 23, 24]]
        grid = [[1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1]]
        self.assertEqual(c.validate_all(grid, cages), False)
        cages = [[9, 3, 0, 5, 6],
                 [7, 2, 1, 2],
                 [10, 3, 3, 8, 13],
                 [14, 4, 4, 9, 14, 19],
                 [3, 1, 7],
                 [8, 3, 10, 11, 16],
                 [13, 4, 12, 17, 21, 22],
                 [5, 2, 15, 20],
                 [6, 3, 18, 23, 24]]
        grid = [[3, 5, 2, 1, 4],
                [5, 1, 3, 4, 2],
                [2, 4, 1, 5, 3],
                [1, 2, 4, 3, 5],
                [4, 3, 5, 2, 1]]
        self.assertEqual(c.validate_all(grid, cages), True)
        cages = [[9, 3, 0, 5, 6],
                 [7, 2, 1, 2],
                 [10, 3, 3, 8, 13],
                 [14, 4, 4, 9, 14, 19],
                 [3, 1, 7],
                 [8, 3, 10, 11, 16],
                 [13, 4, 12, 17, 21, 22],
                 [5, 2, 15, 20],
                 [6, 3, 18, 23, 24]]
        grid = [[3, 5, 2, 1, 4],
                [5, 1, 3, 4, 2],
                [2, 4, 1, 5, 3],
                [1, 2, 4, 3, 5],
                [3, 4, 5, 2, 1]]
        self.assertEqual(c.validate_all(grid, cages), False)
        cages = [[9, 3, 0, 5, 6],
                 [7, 2, 1, 2],
                 [10, 3, 3, 8, 13],
                 [14, 4, 4, 9, 14, 19],
                 [3, 1, 7],
                 [8, 3, 10, 11, 16],
                 [13, 4, 12, 17, 21, 22],
                 [5, 2, 15, 20],
                 [6, 3, 18, 23, 24]]
        grid = [[3, 5, 2, 1, 4],
                [5, 1, 3, 4, 2],
                [2, 4, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]]
        self.assertEqual(c.validate_all(grid, cages), True)


    def test_transpose_grid(self):
        grid = [[1, 2, 5, 3, 4],
                [1, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]]
        self.assertEqual(c.transpose_grid(grid),
                [[1, 1, 0, 0, 0],
                 [2, 0, 0, 0, 0],
                 [5, 0, 0, 0, 0],
                 [3, 0, 0, 0, 0],
                 [4, 0, 0, 0, 0]])
        grid = [[3, 5, 2, 1, 4],
                [5, 1, 3, 4, 2],
                [2, 4, 1, 5, 3],
                [1, 2, 4, 3, 5],
                [4, 3, 5, 2, 1]]
        self.assertEqual(c.transpose_grid(grid),
                [[3, 5, 2, 1, 4],
                 [5, 1, 4, 2, 3],
                 [2, 3, 1, 4, 5],
                 [1, 4, 5, 3, 2],
                 [4, 2, 3, 5, 1]])
        grid = [[3, 5, 2, 1, 4],
                [5, 1, 3, 4, 2],
                [2, 4, 1, 5, 3],
                [1, 2, 4, 3, 5],
                [3, 4, 5, 2, 1]]
        self.assertEqual(c.transpose_grid(grid),
                [[3, 5, 2, 1, 3],
                 [5, 1, 4, 2, 4],
                 [2, 3, 1, 4, 5],
                 [1, 4, 5, 3, 2],
                 [4, 2, 3, 5, 1]])
        grid = [[3, 5, 2, 1, 4],
                [5, 1, 3, 4, 2],
                [2, 4, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]]
        self.assertEqual(c.transpose_grid(grid),
                [[3, 5, 2, 0, 0],
                 [5, 1, 4, 0, 0],
                 [2, 3, 0, 0, 0],
                 [1, 4, 0, 0, 0],
                 [4, 2, 0, 0, 0]])


    def test_create_grid(self):
        self.assertEqual(c.create_grid(5),
                [[0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0]])
        self.assertEqual(c.create_grid(3),
                [[0, 0, 0],
                 [0, 0, 0],
                 [0, 0, 0]])
        self.assertEqual(c.create_grid(4),
                [[0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0]])


    def print_grid(self):
        grid = [[3, 5, 2, 1, 4],
                 [5, 1, 3, 4, 2],
                 [2, 4, 1, 5, 3],
                 [1, 2, 4, 3, 5],
                 [4, 3, 5, 2, 1]]
        self.assertEqual(c.print_grid(grid),
        """3 5 2 1 4
        5 1 3 4 2
        2 4 1 5 3
        1 2 4 3 5
        4 3 5 2 1""")
        grid = [[3, 5, 2, 1, 4],
                [5, 1, 3, 4, 2],
                [2, 4, 1, 5, 3],
                [1, 2, 4, 3, 5],
                [3, 4, 5, 2, 1]]
        self.assertEqual(c.print_grid(grid),
        """3 5 2 1 4
        5 1 3 4 2
        2 4 1 5 3
        1 2 4 3 5
        3 4 5 2 1""")
        grid = [[3, 5, 2, 1, 4],
                [5, 1, 3, 4, 2],
                [2, 4, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]]
        self.assertEqual(c.print_grid(grid),
        """3 5 2 1 4
        5 1 3 4 2
        2 4 0 0 0
        0 0 0 0 0
        0 0 0 0 0""")


if __name__ == '__main__':
    unittest.main()
