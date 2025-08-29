DIM = 3
SIZE = DIM * DIM


class Position:
    def __init__(self, board=" " * 9, turn="x") -> None:
        self.board = list(board)
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
        return [index for index, piece in enumerate(self.board) if piece == " "]

    def is_win_for(self, piece):
        is_match = lambda line: line.count(piece) == DIM
        rows = [is_match(self.board[i : i + DIM]) for i in range(0, SIZE, DIM)]
        cols = [is_match(self.board[i:SIZE:DIM]) for i in range(0, DIM)]
        maj_diag = is_match(self.board[0 : SIZE : DIM + 1])
        min_diag = is_match(self.board[DIM - 1 : SIZE - 1 : DIM - 1])
        return any(rows) or any(cols) or maj_diag or min_diag
