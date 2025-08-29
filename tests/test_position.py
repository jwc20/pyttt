from iuttt import Position
from unittest import TestCase

class TestPosisition(TestCase):
    def test_init(self):
        position = Position()
        self.assertEqual(position.board, list(" " * 9))
        self.assertEqual(position.turn, "x")

    def test_init_with_args(self):
        position = Position("x        ", "o")
        self.assertEqual(position.board, list("x        "))
        self.assertEqual(position.turn, "o")

    def test_eq(self):
        self.assertEqual(Position(), Position())

    def test_move(self):
        self.assertEqual(Position().move(1), Position(" x       ", "o"))

    def test_possible_moves(self):
        self.assertEqual(Position().move(1).possible_moves(), [0,2,3,4,5,6,7,8])


class TestIsWinFor(TestCase):
    def test_no_win(self):
        self.assertFalse(Position().is_win_for("x"))

    def test_row(self):
        self.assertTrue(Position("xxx      ").is_win_for("x"))

    def test_col(self):
        self.assertTrue(Position("o  o  o  ").is_win_for("o"))

    def test_major_diagonal(self):
        self.assertTrue(Position("x   x   x").is_win_for("x"))

    def test_minor_diagonal(self):
        self.assertTrue(Position("  x x x  ").is_win_for("x"))
