import unittest
from chessboard import create_chessboard


class TestBoard(unittest.TestCase):
    def test_empty_board(self):
        self.assertEqual(create_chessboard(0, 0),
                         [])

    def test_one_element_board(self):
        self.assertEqual(create_chessboard(1, 1),
                         [['.']])

    def test_horizontal_board(self):
        self.assertEqual(create_chessboard(1, 5),
                         [['.', '*', '.', '*', '.']])

    def test_vertical_board(self):
        self.assertEqual(create_chessboard(5, 1),
                         [['.'],
                          ['*'],
                          ['.'],
                          ['*'],
                          ['.']])

    def test_typical_board(self):
        self.assertEqual(create_chessboard(3, 4),
                         [['.', '*', '.', '*'],
                          ['*', '.', '*', '.'],
                          ['.', '*', '.', '*']])


if __name__ == '__main__':
    unittest.main()
