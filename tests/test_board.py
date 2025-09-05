from unittest import TestCase
from pyttt.board import Board


class TestBoard(TestCase):
    def test_init_no_params(self):
        board = Board()
        self.assertEqual(board.board, "." * 9)

    def test_init_variant_classic(self):
        board = Board(variant="classic")
        self.assertEqual(board.board, "." * 9)

    def test_init_dimension(self):
        board = Board(dimension=9)
        self.assertEqual(board.board, "." * 81)

    def test_init_rows_columns_3x3(self):
        board = Board(rows=3, columns=3)
        self.assertEqual(board.board, "." * 9)

    def test_init_rows_columns_3x4(self):
        board = Board(rows=3, columns=4)
        self.assertEqual(board.board, "." * 12)