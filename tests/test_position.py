from iuttt import Position
from unittest import TestCase

class TestPosisition(TestCase):
    def test_init(self):
        position = Position()
        self.assertEqual(position.board, list(" " * 9))
        self.assertEqual(position.turn, "x")
