import numpy as np
from typing import List


class Grid:
    def __init__(self):
        self.n = 3
        self.d = 2
        self._grid = None
        self.init_grid()

    def init_grid(self):
        _list = []
        for x in range(self.d):
            _list.append(self.n)
        _tuple = tuple(_list)

        self._grid = np.zeros(_tuple, dtype=int)

    @property
    def grid(self):
        return self._grid

    def place_mark(self, x, y, value):
        self._grid[x][y] = value


class Player:
    def __init__(self, name, mark):
        self._name = name
        self._mark = mark

    @property
    def name(self):
        return self._name

    @property
    def mark(self):
        return self._mark


class Game:
    active_turn = -1

    def __init__(self, grid, players: List[str]):
        self._grid = grid
        self._score_grid = None
        self._game_over = False
        if len(players) == 2:
            self._players = [
                Player(players[0], -1),  # player 1 is X = -1
                Player(players[1], 1),  # player 2 is O = 1
            ]
        else:
            print("error, there must be only two players")

        if self.get_dim() > 2:
            self.init_score_grid()

    def init_score_grid(self):
        _d = self.get_dim() - 2
        _list = []
        for _ in range(_d):
            _list.append(3)
        _tuple = tuple(_list)

        self._score_grid = np.zeros(_tuple, dtype=int)

    def get_dim(self):
        return self._grid.grid.ndim

    @property
    def score_grid(self):
        return self._score_grid

    @property
    def players(self):
        return self._players

    @property
    def game_over(self):
        return self._game_over

    def switch_turn(self):
        global active_turn
        self.active_turn *= -1
        return self.active_turn

    def get_player(self):
        return 0 if self.active_turn == 1 else 1

    def play_move(self, x, y):
        # TODO: check if valid row and column

        # check if already placed
        if self._grid.grid[x][y] != 0:
            return "error, already placed"

        active_turn = self.switch_turn()
        print(
            f"player {self._players[self.get_player()].name} is placing: {active_turn}"
        )
        self._grid.place_mark(x, y, active_turn)
        print(self._grid.grid)

        check_win = self.check_win()
        if check_win:
            self._game_over = True

        # draw
        if 0 not in self._grid.grid and self._game_over is False:
            print("draw")
            self._game_over = True

    def check_all_sums(self):
        sums = []
        matrix = self._grid.grid

        # Row sums
        row_sums = np.sum(matrix, axis=1)
        print("Row sums:", row_sums)

        # Column sums
        col_sums = np.sum(matrix, axis=0)
        print("Column sums:", col_sums)

        # Main diagonal sum (top-left to bottom-right)
        main_diag_sum = np.trace(matrix)
        print("Main diagonal sum:", main_diag_sum)

        # Anti-diagonal sum (top-right to bottom-left)
        anti_diag_sum = np.trace(np.fliplr(matrix))
        print("Anti-diagonal sum:", anti_diag_sum)

        sums.extend(row_sums)
        sums.extend(col_sums)
        sums.append(main_diag_sum)
        sums.append(anti_diag_sum)

        return sums

    def check_win(self):
        all_sum = self.check_all_sums()

        if 3 in all_sum:
            print(f"{self.players[1].name} wins")
            return True
        elif -3 in all_sum:
            print(f"{self.players[0].name} wins")
            return True
