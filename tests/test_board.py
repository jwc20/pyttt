from unittest import TestCase

from pyttt.board import Board


class TestBoard(TestCase):
    def test_init_no_params(self):
        board = Board()
        self.assertEqual(board.board, "." * 9)

    def test_init_variant_classic(self):
        board = Board(variant="classic")
        self.assertEqual(board.board, "." * 9)
        
    def test_init_variant_ultimate(self):
        board = Board(variant="ultimate")
        self.assertEqual(board.board, "." * 81)

    def test_init_dimension_3x3(self):
        board = Board(dimension=3)
        self.assertEqual(board.board, "." * 9)
        
    def test_init_dimension_9x9(self):
        board = Board(dimension=9)
        self.assertEqual(board.board, "." * 81)

    def test_init_rows_columns_3x3(self):
        board = Board(rows=3, columns=3)
        self.assertEqual(board.board, "." * 9)

    def test_init_rows_columns_3x4(self):
        board = Board(rows=3, columns=4)
        self.assertEqual(board.board, "." * 12)
        
    def test_cross(self):
        board = Board(dimension=3)
        dim = board.get_dimension()
        coords = board.get_coordinates_str(dim)
        self.assertEqual(board.cross(coords, coords), ("0,0", "0,1", "0,2", "1,0", "1,1", "1,2", "2,0", "2,1", "2,2"))
        