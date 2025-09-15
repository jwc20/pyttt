from unittest import TestCase

from pyttt.game import Game


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
        self.assertEqual(Game().place_mark_in_box_by_index(1), Game(".x.......", "o"))

    def test_possible_moves(self):
        # print("\npossible moves:",Game().place_mark_in_box(1).possible_moves())
        self.assertEqual(Game().place_mark_in_box_by_index(1).possible_moves_in_box(), [0, 2, 3, 4, 5, 6, 7, 8])


class TestGamePlaceMark(TestCase):
    ...
