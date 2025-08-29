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

class TestMinimax(TestCase):
    def test_x_wins(self):
        self.assertEqual(Position("xxx      ").minimax(), 6)

    def test_o_wins(self):
        self.assertEqual(Position("ooo      ").minimax(), -6)

    def test_draw(self):
        self.assertEqual(Position("xoxxoxoxo").minimax(), 0)

    def test_x_wins_in_one(self):
        self.assertEqual(Position("xx       ").minimax(), 6)

    def test_o_wins_in_one(self):
        self.assertEqual(Position("oo       ", "o").minimax(), -6)

    def test_cache(self):
        self.assertEqual(Position().minimax(), 0)


class TestBestMove(TestCase):
    def test_x(self):
        self.assertEqual(Position("xx       ", "x").best_move(), 2)

    def test_o(self):
        self.assertEqual(Position("oo       ", "o").best_move(), 2)

class TestIsGameEnd(TestCase):
    def test_not_end(self):
        self.assertFalse(Position().is_game_end())

    def test_x_wins(self):
        self.assertTrue(Position("xxx      ").is_game_end())

    def test_o_wins(self):
        self.assertTrue(Position("ooo      ").is_game_end())

    def test_draw(self):
        self.assertTrue(Position("xoxxoxoxo").is_game_end())

