from unittest import TestCase

from pyttt.game import Game
# from pyttt.board import Board
# from pyttt.player import Player


class TestGame(TestCase):
    def test_init(self):
        game = Game()
        self.assertEqual(game.board_list, list("." * 9))
        self.assertEqual(game.turn, "x")

    def test_init_with_args(self):
        game = Game("x........", "o")
        self.assertEqual(game.board_list, list("x........"))
        self.assertEqual(game.turn, "o")

    def test_eq(self):
        self.assertEqual(Game(), Game())

    def test_move(self):
        self.assertEqual(Game().place_mark_in_box(1), Game(".x.......", "o"))

    def test_possible_moves(self):
        # print("\npossible moves:",Game().place_mark_in_box(1).possible_moves())
        self.assertEqual(Game().place_mark_in_box(1).possible_moves_in_box(), [0, 2, 3, 4, 5, 6, 7, 8])


class TestIsWinFor(TestCase):
    def test_no_win(self):
        self.assertFalse(Game().check_win_in_box("x"))

    def test_row(self):
        self.assertTrue(Game("xxx......").check_win_in_box("x"))

    def test_col(self):
        self.assertTrue(Game("o..o..o..").check_win_in_box("o"))

    def test_major_diagonal(self):
        self.assertTrue(Game("x...x...x").check_win_in_box("x"))

    def test_minor_diagonal(self):
        self.assertTrue(Game("..x.x.x..").check_win_in_box("x"))


class TestMinimax(TestCase):
    def test_x_wins(self):
        self.assertEqual(Game("xxx......").minimax(), 6)

    def test_o_wins(self):
        self.assertEqual(Game("ooo......").minimax(), -6)

    def test_draw(self):
        self.assertEqual(Game("xoxxoxoxo").minimax(), 0)

    def test_x_wins_in_one(self):
        self.assertEqual(Game("xx.......").minimax(), 6)

    def test_o_wins_in_one(self):
        self.assertEqual(Game("oo.......", "o").minimax(), -6)

    def test_cache(self):
        self.assertEqual(Game().minimax(), 0)


class TestBestMove(TestCase):
    def test_x(self):
        self.assertEqual(Game("xx.......", "x").best_move(), 2)

    def test_o(self):
        self.assertEqual(Game("oo.......", "o").best_move(), 2)


class TestIsGameEnd(TestCase):
    def test_not_end(self):
        self.assertFalse(Game().is_game_end())

    def test_x_wins(self):
        self.assertTrue(Game("xxx......").is_game_end())

    def test_o_wins(self):
        self.assertTrue(Game("ooo......").is_game_end())

    def test_draw(self):
        self.assertTrue(Game("xoxxoxoxo").is_game_end())
