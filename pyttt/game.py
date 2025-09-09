from pyttt.board import Board
from pyttt.player import Player
from copy import deepcopy

# default 3x3 board size (classic tic-tac-toe)
DIM = 3
SIZE = DIM * DIM


class Game:
    def __init__(self, board: Board | str | None = None, turn: str = "x", players: list[Player] = []) -> None:
        self.board: Board = board
        if board is None:
            self.board = Board()
        if board is not None and isinstance(board, str):
            self.board = Board(board_str=board)
        self.board_list = self.board.to_list()
        self.players = players
        self.turn = turn
        
    def t3n(self):
        """
        tic-tac-toe game notation
        
        components:
            - current player's turn
            - allowed box to place piece
            - board string
            
        example:
            - ultimate tic-tac-toe:
                - "O;@........;X.OO...../X..X.O.O./X.X...O.O/.X.OXO.../O.O.X..../.XX....O./......X.O/.O.X.X.../.O.....XX" (example from ultimattt)
        """

        

    def __repr__(self):
        return "(%s, %s)" % (repr("".join(self.board_list)), repr(self.turn))

    def __eq__(self, other):
        return self.board_list == other.board_list and self.turn == other.turn

    def choose(self, x, o):
        return x if self.turn == "x" else o

    def move(self, index):
        self.board_list[index] = self.turn
        self.turn = self.choose("o", "x")
        return self

    def possible_moves(self):
        return [index for index, piece in enumerate(self.board_list) if piece == "."]

    def is_win_for(self, piece):
        """checks 3x3 board if the given piece has won"""
        is_match = lambda line: line.count(piece) == DIM
        
        rows = [is_match(self.board_list[i: i + DIM]) for i in range(0, SIZE, DIM)]
        cols = [is_match(self.board_list[i:SIZE:DIM]) for i in range(0, DIM)]
        maj_diag = is_match(self.board_list[0: SIZE: DIM + 1])
        min_diag = is_match(self.board_list[DIM - 1: SIZE - 1: DIM - 1])
        return any(rows) or any(cols) or maj_diag or min_diag

    # this cache variable memoize  
    # note: this should not be encapsulated since it makes it slower
    cache = {}
    def minimax(self):
        key = repr(self)
        value = self.cache.get(key)
        if value is not None:
            # if the value is 0, then the value is considered False. so we need to check if it's None.
            return value
        if self.is_win_for("x"):
            return self.board_list.count(".")
        if self.is_win_for("o"):
            return -self.board_list.count(".")
        if self.board_list.count(".") == 0:
            return 0

        # TODO: find a way not to use deepcopy()
        values = [
            deepcopy(self).move(index).minimax() for index in self.possible_moves()
        ]
        value = self.choose(max, min)(values)
        self.cache[key] = value
        return value

    def best_move(self):
        fn = self.choose(max, min)
        return fn(
            self.possible_moves(),
            key=lambda index: deepcopy(self).move(index).minimax(),
        )

    def is_game_end(self):
        return (
                self.is_win_for("x") or self.is_win_for("o") or self.board_list.count(".") == 0
        )
