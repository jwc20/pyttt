from unittest import TestCase
from iuttt import Game, Position


class TestGame(TestCase):
    def set_up(self):
        self.game = Game()

    def test_init(self):
        self.set_up()
        self.assertEqual(self.game.position, Position())
