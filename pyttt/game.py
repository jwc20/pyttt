from copy import deepcopy

DIM = 3
SIZE = DIM * DIM


class Game:
    def __init__(self, board: str = "." * SIZE, turn: str = "x") -> None:
        self.board = list(board)
        # self.players = players
        self.turn = turn

    def __repr__(self):
        return "(%s, %s)" % (repr("".join(self.board)), repr(self.turn))

    def __eq__(self, other):
        return self.board == other.board and self.turn == other.turn

    def choose(self, x, o):
        return x if self.turn == "x" else o

    def move(self, index):
        self.board[index] = self.turn
        self.turn = self.choose("o", "x")
        return self

    def possible_moves(self):
        return [index for index, piece in enumerate(self.board) if piece == "."]

    def is_win_for(self, piece):
        """checks 3x3 board if the given piece has won"""
        is_match = lambda line: line.count(piece) == DIM
        
        rows = [is_match(self.board[i: i + DIM]) for i in range(0, SIZE, DIM)]
        cols = [is_match(self.board[i:SIZE:DIM]) for i in range(0, DIM)]
        maj_diag = is_match(self.board[0: SIZE: DIM + 1])
        min_diag = is_match(self.board[DIM - 1: SIZE - 1: DIM - 1])
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
            return self.board.count(".")
        if self.is_win_for("o"):
            return -self.board.count(".")
        if self.board.count(".") == 0:
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
                self.is_win_for("x") or self.is_win_for("o") or self.board.count(".") == 0
        )
