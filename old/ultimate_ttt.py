import numpy as np
from typing import List


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


class Grid:
    def __init__(self, d):
        self.w = 3
        self.d = d  # ultimate tic-tac-toe
        self.grid = None
        self.score_grid = None
        self.init_grid()
        self.init_score_grid()

    def init_grid(self):
        _tuple = tuple([self.w for _ in range(self.d)])
        self.grid = np.zeros(_tuple, dtype=int)

    def get_w(self):
        return self.w

    def get_d(self):
        return self.d

    def is_valid_position(self, x, y):
        return 0 <= x < self.w and 0 <= y < self.w

    # def place_mark(self, x, y, value):
    #     if self.grid is None:
    #         raise ValueError("Grid is not initialized")
    # 
    #     if not self.is_valid_position(x, y):
    #         raise ValueError(
    #             f"Position ({x}, {y}) is out of bounds. Valid range: 0-{self.w-1}"
    #         )
    # 
    #     self.grid[x][y] = value

    def init_score_grid(self):
        n = self.w ** (self.d // 2 - 1)
        print(f"{n}x{n} matrix")
        score_grid_d = np.zeros((n, n))
        self._score_grid = score_grid_d

    def show_index_grid(self):
        """get matrix of 3x3 grids"""
        n = self.w ** (self.d // 2 - 1)
        num_of_grids = n * n
        matrix = np.arange(num_of_grids).reshape(n, n)
        return matrix


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

        # if self.get_dim() > 2:
        #     self.init_score_grid()
        self.sum_to_win = self.get_width() ** (self.get_dim() // 2)
        self.init_score_grid()

    def init_score_grid(self):
        _d = self.get_dim() - 2
        _list = []
        for _ in range(_d):
            _list.append(3)
        _tuple = tuple(_list)

        self.score_grid = np.zeros(_tuple, dtype=int)

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


    def play(self, x, y):
        if self.get_dim() == 2:
            # classic tic-tac-toe
            self.play_move_in_3x3_grid(x, y)

        elif self.get_dim() == 4:
            # ultimate tic-tac-toe
            self.play_move_in_9x9_grid(x, y)
        else:
            raise ValueError("there are only two types of tic-tac-toe: classic and ultimate")

    def place_mark_3x3_grid(self, x, y, value):
        if self.grid is None:
            raise ValueError("Grid is not initialized")

        if not self.grid.is_valid_position(x, y):
            raise ValueError(
                f"Position ({x}, {y}) is out of bounds. Valid range: 0-{self.w-1}"
            )

        self.grid.grid[x][y] = value









    def place_mark_9x9_grid(self, tuple, value):
        
        meta_x_y = [tuple[0], tuple[1]]
        mini_x_y = [tuple[2], tuple[3]]
        
        if self.grid is None:
            raise ValueError("Grid is not initialized")

        if not self.grid.is_valid_position(meta_x_y[0], meta_x_y[1]):
            # raise ValueError(
            #     f"Position ({x}, {y}) is out of bounds. Valid range: 0-{self.w-1}"
            # )
            return 
        if not self.grid.is_valid_position(mini_x_y[0], mini_x_y[1]):
            # raise ValueError(
            #     f"Position ({x}, {y}) is out of bounds. Valid range: 0-{self.w-1}"
            # )
            return

        self.grid.grid[tuple] = self.active_turn



    def play_move_in_9x9_grid(self, x, y):
        """
        grid[(0, 0, 0, 0)] = -1
        #     │  │  │  └── 4th dimension index
        #     │  │  └──── 3rd dimension index  
        #     │  └────── 2nd dimension index
        #     └──────── 1st dimension index
        
        grid[(2,1,0,2)] = 5   
        # 2 => 3rd (bottom) floor (index 2 = third in 0-indexed system)
        # 1 => 2nd building (index 1 = second building)  
        # 0 => 1st row (index 0 = first row)
        # 2 => 3rd column (index 2 = third column)
        """
        dims = self.get_dim()
        k = dims // 2
        
        indices = []
        for i in reversed(range(k)):
            div = 3 ** i
            indices.append(x // div % 3)  # row at level i
            indices.append(y // div % 3)  # col at level i
        
        _tuple = tuple(indices)
        
        
        print(
            f"player {self._players[self.get_player()].name} is placing: {self.active_turn}"
        )
        self.place_mark_9x9_grid(_tuple, self.active_turn)
        active_turn = self.switch_turn()
        
        check_win = self.check_win_in_9x9_grid(_tuple)
        
        if check_win:
            self._game_over = True
            
        # draw
        if 0 not in self.grid.grid and self._game_over is False:
            print("draw")
            self._game_over = True

            
            
    
    
    def check_win_in_9x9_grid(self, tuple):
        """ check win in meta board"""
        
        meta_board_position = (tuple[0], tuple[1])
        
        mini_grid = self.grid.grid[meta_board_position]
        
        all_sum = self.check_all_sums(mini_grid)

        if 3 in all_sum:
            self.score_grid[meta_board_position] = 3
        elif -3 in all_sum:
            self.score_grid[meta_board_position] = -3
    
    
    
        all_meta_board_sum = self.check_all_sums(self.score_grid)
        
        if 9 in all_meta_board_sum:
            print(f"{self.players[1].name} wins")
            return True
        elif -9 in all_meta_board_sum:
            print(f"{self.players[0].name} wins")
            return True

    def play_move_in_3x3_grid(self, x, y):
        """play move in a 3x3 grid"""

        # check if already placed
        if self.grid.grid[x][y] != 0:
            # raise ValueError("error, already placed")
            # print("error, already placed")
            return "error, already placed"

        
        print(
            f"player {self._players[self.get_player()].name} is placing: {self.active_turn}"
        )
        self.place_mark_3x3_grid(x, y, self.active_turn)
        active_turn = self.switch_turn()
        print(self.grid.grid)

        check_win = self.check_win(self.grid.grid)
        if check_win:
            self._game_over = True

        # draw
        if 0 not in self.grid.grid and self._game_over is False:
            print("draw")
            self._game_over = True

    def check_all_sums(self, matrix):
        sums = []
        # matrix = self.grid.grid

        row_sums = np.sum(matrix, axis=1)
        col_sums = np.sum(matrix, axis=0)
        main_diag_sum = np.trace(matrix)
        anti_diag_sum = np.trace(np.fliplr(matrix))

        sums.extend(row_sums)
        sums.extend(col_sums)
        sums.append(main_diag_sum)
        sums.append(anti_diag_sum)

        return sums

    def check_win(self, matrix):
        all_sum = self.check_all_sums(matrix)

        if 3 in all_sum:
            print(f"{self.players[1].name} wins")
            return True
        elif -3 in all_sum:
            print(f"{self.players[0].name} wins")
            return True


if __name__ == "__main__":

    import random

    d = 2
    n = 3 ** (d // 2)
    print(d, n)

    grid = Grid(d)
    game = Game(grid, ["p1", "p2"])

    while game._game_over is False:
        x = random.randrange(n)
        y = random.randrange(n)
        game.play(x, y)

    # for i in range(80):
    #     x = random.randrange(n)
    #     y = random.randrange(n)
    #     game.play(x, y)
        
    print(game.grid.grid)

    print(game.score_grid)
