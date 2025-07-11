import numpy as np
from typing import List
import itertools


class Grid:
    def __init__(self, d):
        self.w = 3
        self.d = d
        self.game_grid = None
        self.position_grid = None
        self.score_grid = None
        self.init_game_grid()
        self.init_position_grid()
        self.init_score_grid()

    def init_game_grid(self):
        _tuple = tuple([self.w for _ in range(self.d)])
        self.game_grid = np.zeros(_tuple, dtype=int)

    def init_position_grid(self):
        n = self.w ** (self.d // 2)
        _tuple = (n, n)
        self.position_grid = np.zeros(_tuple, dtype=int)

    # @property
    # def game_grid(self):
    #     return self._grid

    def get_w(self):
        return self.w

    def get_d(self):
        return self.d

    def is_valid_position(self, x, y):
        n = self.w ** (self.d // 2)
        return 0 <= x < n and 0 <= y < n

    def place_mark_in_position_grid(self, x, y, value):
        if self.position_grid is None:
            raise ValueError("Grid is not initialized")

        if not self.is_valid_position(x, y):
            n = self.w ** (self.d // 2)
            raise ValueError(f"Position ({x}, {y}) is out of bounds. Valid range: 0-{n - 1}")

        self.position_grid[x][y] = value
        self.place_mark_in_game_grid(x, y, value)

    def place_mark_in_game_grid(self, x, y, value):
        # Get the number of dimensions (must be even)
        dims = self.game_grid.shape
        k = len(dims) // 2  # Number of levels (each level has 2 dims: row and col)

        # Ensure shape is valid: (3, 3, 3, 3, ..., 3)
        assert all(d == 3 for d in dims), "All dimensions must be 3"

        # Extract the path to the cell using base-3 decomposition
        indices = []
        for i in reversed(range(k)):
            div = 3 ** i
            indices.append(x // div % 3)  # row at level i
            indices.append(y // div % 3)  # col at level i

        # Convert to tuple for indexing
        self.game_grid[tuple(indices)] = value

    def init_score_grid(self):
        n = self.w ** (self.d // 2 - 1)
        # print(f"{n}x{n} matrix")
        score_grid_d = np.zeros((n, n))
        self.score_grid = score_grid_d

    def show_index_grid(self):
        """ get matrix of 3x3 grids """
        n = self.w ** (self.d // 2 - 1)
        num_of_grids = n * n
        matrix = np.arange(num_of_grids).reshape(n, n)
        return matrix

    # @property
    # def score_grid(self):
    #     return self._score_grid


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
        self.grid = grid
        self.score_grid = None
        self._game_over = False

        if len(players) == 2:
            # TODO: use dictionary instead of list
            self._players = [
                Player(players[0], -1),  # player 1 is X = -1
                Player(players[1], 1),  # player 2 is O = 1
            ]
        else:
            raise ValueError("error, there must be only two players")

        if self.get_dim() > 2:
            self.init_score_grid()
        self.sum_to_win = self.get_width() ** (self.get_dim() // 2)

    def init_score_grid(self):
        _d = self.get_dim() - 2
        _list = []
        for _ in range(_d):
            _list.append(3)
        _tuple = tuple(_list)

        self.score_grid = np.zeros(_tuple, dtype=int)
    
    # def init_score_grid(self):
    #     n = 3 ** (self.get_dim() // 2 - 1)
    #     # print(f"{n}x{n} matrix")
    #     score_grid_d = np.zeros((n, n))
    #     self.score_grid = score_grid_d

    def get_3x3_grid_position(self):
        pass

    def get_dim(self):
        return self.grid.get_d()

    def get_width(self):
        return self.grid.get_w()

    # @property
    # def score_grid(self):
    #     return self._score_grid

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

    # def play_move(self, x, y):
    #     """Play move at position (x, y) and update game state."""
    # 
    #     # Check if already placed
    #     if self.grid.position_grid[x][y] != 0:
    #         return "error, already placed"
    # 
    #     # Switch turn and get mark
    #     active_turn = self.switch_turn()
    #     current_player = self._players[self.get_player()]
    #     print(f"player {current_player.name} is placing: {active_turn} on position ({x}, {y})")
    # 
    #     # Place the mark in the flattened 2D grid
    #     self.grid.place_mark_in_position_grid(x, y, active_turn)
    # 
    #     # Update the hierarchical game grid (if using)
    #     self.grid.place_mark_in_game_grid(x, y, active_turn)
    # 
    #     final_result = self.check_win_in_3x3(self._score_grid)
    #     if final_result == 1:
    #         print(f"{self.players[1].name} wins the entire game!")
    #         self._game_over = True
    #         return
    #     elif final_result == -1:
    #         print(f"{self.players[0].name} wins the entire game!")
    #         self._game_over = True
    #         return
    # 
    #     # Check for draw — only if no zero in the full game grid
    #     if np.all(self.grid.position_grid != 0):
    #         print("draw")
    #         self._game_over = True
    #         return

    # def play_move(self, x, y):
    #     """Play move at position (x, y) and update game state."""
    # 
    #     # Check if already placed
    #     if self.grid.position_grid[x][y] != 0:
    #         return "error, already placed"
    # 
    #     # Switch turn and get mark
    #     active_turn = self.switch_turn()
    #     current_player = self._players[self.get_player()]
    #     print(f"player {current_player.name} is placing: {active_turn} on position ({x}, {y})")
    # 
    #     # Place the mark in the flattened 2D grid
    #     self.grid.place_mark_in_position_grid(x, y, active_turn)
    # 
    #     # Update the hierarchical game grid
    #     self.grid.place_mark_in_game_grid(x, y, active_turn)
    # 
    #     self.check_wins()
    # 
    #     # Check if there's a winner in the full game grid (multi-dim)
    #     # final_result = self.check_win_in_3x3(self.grid.game_grid)
    #     # if final_result == 1:
    #     #     print(f"{self.players[1].name} wins the entire game!")
    #     #     self._game_over = True
    #     #     print(game.grid.position_grid)
    #     #     print(game.grid.game_grid)
    #     #     return
    #     # elif final_result == -1:
    #     #     print(f"{self.players[0].name} wins the entire game!")
    #     #     self._game_over = True
    #     #     print(game.grid.position_grid)
    #     #     print(game.grid.game_grid)
    #     #     return
    #     # 
    #     # # Check for draw — only if no zeros in full position grid
    #     # if np.all(self.grid.position_grid != 0):
    #     #     print("draw")
    #     #     self._game_over = True
    #     #     print(game.grid.position_grid)
    #     #     print(game.grid.game_grid)
    #     #     return

    # def check_wins(self):
    #     """
    #     dimension = 4 -> 9x9 position grid, 3x3x3x3 game grid, 3x3 score grid
    #     dimension = 6 -> 27x27 position grid, 3x3x3x3x3x3 game grid, 9x9 score grid
    #     dimension = 8 -> 81x81 position grid, 3x3x3x3x3x3x3x3x3 game grid, 27x27 score grid
    #     ...
    #     
    #     must check for win in each 3x3 grid 
    #     """
    #     d = self.get_dim()
        


    def check_win_in_3x3_grid(self):
        all_sum = self.check_all_sums_in_3x3_grid()

        if 3 in all_sum:
            print(f"{self.players[1].name} wins")
            return True
        elif -3 in all_sum:
            print(f"{self.players[0].name} wins")
            return True



    def check_all_sums_in_3x3_grid(self):
        sums = []
        matrix = self.grid.game_grid

        row_sums = np.sum(matrix, axis=1)
        col_sums = np.sum(matrix, axis=0)
        main_diag_sum = np.trace(matrix)
        anti_diag_sum = np.trace(np.fliplr(matrix))

        sums.extend(row_sums)
        sums.extend(col_sums)
        sums.append(main_diag_sum)
        sums.append(anti_diag_sum)

        return sums

    def play_move(self, x, y):
        """Play move at position (x, y) and update game state."""

        if self.grid.position_grid[x][y] != 0:
            return "error, already placed"

        active_turn = self.switch_turn()
        current_player = self._players[self.get_player()]
        print(f"player {current_player.name} is placing: {active_turn} on position ({x}, {y})")

        self.grid.place_mark_in_position_grid(x, y, active_turn)
        self.grid.place_mark_in_game_grid(x, y, active_turn)

        self.check_wins()

        if np.all(self.grid.position_grid != 0):
            print("draw")
            self._game_over = True

    def check_wins(self):
        """
        Scan all 3x3 blocks in the N-dimensional game grid.
        If any block has a win, record it in the score grid.
        Then, check if the score grid has a winning line.
        """
        d = self.get_dim()
        w = self.get_width()
        grid = self.grid.game_grid

        score_shape = tuple([w] * (d // 2))
        # if self.score_grid is None:
        #     self.score_grid = np.zeros(score_shape, dtype=int)

        from itertools import product

        # Iterate over all sub-blocks of shape (3, 3) in N-dim grid
        index_ranges = [range(0, grid.shape[i], w) for i in range(d)]
        for index in product(*index_ranges):
            # Get slice for this 3x3 block
            slices = tuple(slice(i, i + w) for i in index)
            block = grid[slices]

            if any(s.stop > grid.shape[i] for i, s in enumerate(slices)):
                continue

            win_value = self.check_sum_in_block(block)
            # score_index = tuple(i // w for i in index)
            score_index = tuple(i // w for i in index[:d // 2])
            # score_index = tuple(i // w for i in index)

            if self.score_grid[score_index] == 0 and win_value != 0:
                self.score_grid[score_index] = win_value
                print(f"Block at {score_index} won by {'O' if win_value == 1 else 'X'}")

        # Check if someone has won in the score grid
        result = self.check_win_in_score_grid(self.score_grid)
        if result == 1:
            print(f"{self._players[1].name} wins the entire game!")
            self._game_over = True
        elif result == -1:
            print(f"{self._players[0].name} wins the entire game!")
            self._game_over = True

    def check_sum_in_block(self, block: np.ndarray) -> int:
        """
        Takes a small block (shape 3x3... depending on dim) and returns:
        1 if O wins, -1 if X wins, 0 otherwise.
        """
        w = self.get_width()
        d = block.ndim

        from itertools import product

        def all_lines():
            lines = []
            for start in product(range(w), repeat=d):
                for direction in product([-1, 0, 1], repeat=d):
                    if all(v == 0 for v in direction):
                        continue
                    line = []
                    for i in range(w):
                        idx = tuple(start[j] + direction[j] * i for j in range(d))
                        if all(0 <= idx[j] < w for j in range(d)):
                            line.append(block[idx])
                        else:
                            break
                    if len(line) == w:
                        lines.append(sum(line))
            return lines

        line_sums = all_lines()
        if w in line_sums:
            return 1
        elif -w in line_sums:
            return -1
        return 0

    def check_win_in_score_grid(self, board: np.ndarray):
        """
        Checks the current score grid for a win (across any line).
        """
        w = self.get_width()
        d = board.ndim

        from itertools import product

        def all_lines():
            lines = []
            for start in product(range(w), repeat=d):
                for direction in product([-1, 0, 1], repeat=d):
                    if all(v == 0 for v in direction):
                        continue
                    line = []
                    for i in range(w):
                        idx = tuple(start[j] + direction[j] * i for j in range(d))
                        if all(0 <= idx[j] < w for j in range(d)):
                            line.append(board[idx])
                        else:
                            break
                    if len(line) == w:
                        lines.append(sum(line))
            return lines

        line_sums = all_lines()
        if w in line_sums:
            return 1
        elif -w in line_sums:
            return -1
        return 0


if __name__ == "__main__":
    import random

    d = 4

    n = 3 ** (d // 2)

    grid = Grid(d)
    game = Game(grid, ["p1", "p2"])
    print(game.get_dim())


    while game.game_over is False:
        x = random.randrange(n)
        y = random.randrange(n)
        game.play_move(x, y)

    print(game.score_grid)
    print(game.grid.position_grid)
    # print(game.grid.game_grid)
    
