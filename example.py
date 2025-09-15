"""
example.py
"""

from pprintpp import pprint
from pyttt.board import Board
from pyttt.game import Game


if __name__ == "__main__":
    pprint("hello")

    board = Board(dimension=9)
    game = Game(board)
    pprint(game)