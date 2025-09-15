"""
pyttt/game.py
"""

# import math

from pyttt.board import Board
from pyttt.player import Player
from copy import deepcopy

# from pyttt.utils import place_mark

# from pyttt.utils import insert_char_every_n

# default 3x3 board size (classic tic-tac-toe)
DIM = 3
SIZE = DIM * DIM


class Game:
    def __init__(self,
                 board: Board | str | None = None,
                 turn: str = "x",
                 players: list[Player] = [],
                 ) -> None:
        self.board: Board = board
        if board is None:
            self.board = Board()
        if board is not None and isinstance(board, str):
            self.board = Board(board_str=board)

        self.board_list = self.board.to_list()
        self.players = players
        self.turn = turn

        # TODO: 
        self.t3n: str = self.set_t3n()

        # TODO: this probably dont have to be a string
        # self.score_board_str: str = self._init_score_board()

    # 
    # def _init_score_board(self) -> str:
    #     dimension = self.board.get_dimension()
    #     if dimension < 9:
    #         return ""
    # 
    #     squares_count = len(self.board.squares)
    #     squares_exponent = int(math.log(squares_count, 3))
    # 
    #     segments = []
    #     for i in range(2, squares_exponent, 2):
    #         dots = "." * (3 ** i)
    #         if len(dots) > 9:
    #             dots = insert_char_every_n(dots, "/", 9)
    #         segments.append(dots)
    # 
    #     return ";".join(segments)

    def set_t3n(self):
        """
        tic-tac-toe game notation
        
        components:
            - current player's turn
            - allowed box to place mark
            - board string
            
        example:
            - ultimate tic-tac-toe:
                - "O;@........;X.OO...../X..X.O.O./X.X...O.O/.X.OXO.../O.O.X..../.XX....O./......X.O/.O.X.X.../.O.....XX" (example from ultimattt)
        """
        _turn = repr(self.turn)
        _allowed_box = None
        
        
        # _partitioned_board = []
        # _dim = self.board.get_dimension()
        # 
        # if _dim > 3:
        #     for i in range(0, len(self.board.board_str), _dim):
        #         _partitioned_board.append(self.board.board_str[i: i + 9])
        #         _partitioned_board.append("/")
        # else:
        #     _partitioned_board = self.board.board_str

        _board = []
        for row in self.board.partitioned_board:
            _board += row

        _board_str = "".join(_board)

        if self.board.config["variant"] == "ultimate":
            # TODO
            _allowed_box = "........."

            return "%s;%s;%s" % (_turn, _allowed_box, _board_str)
        return "%s;%s" % (_turn, _board_str)

    def __repr__(self):
        return "(%s, %s)" % (repr("".join(self.board_list)), repr(self.turn))

    def __eq__(self, other):
        return self.board_list == other.board_list and self.turn == other.turn

    def switch_turn_in_box(self, x, o):
        return x if self.turn == "x" else o

    def possible_moves_in_box(self):
        return [index for index, mark in enumerate(self.board_list) if mark == "."]

    def check_win_in_box(self, mark):
        """checks 3x3 board if the given mark has won"""
        is_match = lambda line: line.count(mark) == DIM

        rows = [is_match(self.board_list[i: i + DIM]) for i in range(0, SIZE, DIM)]
        cols = [is_match(self.board_list[i:SIZE:DIM]) for i in range(0, DIM)]
        maj_diag = is_match(self.board_list[0: SIZE: DIM + 1])
        min_diag = is_match(self.board_list[DIM - 1: SIZE - 1: DIM - 1])
        return any(rows) or any(cols) or maj_diag or min_diag

    def is_game_end_in_box(self):
        return (
                self.check_win_in_box("x") or self.check_win_in_box("o") or self.board_list.count(".") == 0
        )

    ########################################################################
    ########################################################################

    # this cache variable memoize  
    # note: this should not be encapsulated since it makes it slower
    cache = {}

    def minimax(self):
        key = repr(self)
        value = self.cache.get(key)
        if value is not None:
            # if the value is 0, then the value is considered False. so we need to check if it's None.
            return value
        if self.check_win_in_box("x"):
            return self.board_list.count(".")
        if self.check_win_in_box("o"):
            return -self.board_list.count(".")
        if self.board_list.count(".") == 0:
            return 0

        # TODO: find a way not to use deepcopy()
        values = [
            deepcopy(self).place_mark_in_box(index).minimax() for index in self.possible_moves_in_box()
        ]
        value = self.switch_turn_in_box(max, min)(values)
        self.cache[key] = value
        return value

    def best_move(self):
        fn = self.switch_turn_in_box(max, min)
        return fn(
            self.possible_moves_in_box(),
            key=lambda index: deepcopy(self).place_mark_in_box(index).minimax(),
        )

    ########################################################################
    ########################################################################

    # TODO: deprecate
    def place_mark_in_box(self, index):
        """places a mark in the given box(3x3 board)"""
        self.board_list[index] = self.turn
        self.turn = self.switch_turn_in_box("o", "x")
        return self

    def check_win_in_a_box(self, box: tuple, mark: str):
        is_match = lambda line: line.count(mark) == DIM

        box_dict = {}

        for key in box:
            box_dict[key] = self.board.grid.get(key)

        # print(box_dict)

        box_str = "".join(box_dict.values())
        # print(box_str)

        rows = [is_match(box_str[i: i + DIM]) for i in range(0, SIZE, DIM)]
        cols = [is_match(box_str[i:SIZE:DIM]) for i in range(0, DIM)]
        maj_diag = is_match(box_str[0: SIZE: DIM + 1])
        min_diag = is_match(box_str[DIM - 1: SIZE - 1: DIM - 1])
        return any(rows) or any(cols) or maj_diag or min_diag

    def get_game_winner(self):
        """
        boxes = [('0,0', '0,1', '0,2', '1,0', '1,1', '1,2', '2,0', '2,1', '2,2'),('0,3', '0,4', '0,5', '1,3', '1,4', '1,5', '2,3', '2,4', '2,5'),('0,6', '0,7', '0,8', '1,6', '1,7', '1,8', '2,6', '2,7', '2,8'),('3,0', '3,1', '3,2', '4,0', '4,1', '4,2', '5,0', '5,1', '5,2'),('3,3', '3,4', '3,5', '4,3', '4,4', '4,5', '5,3', '5,4', '5,5'),('3,6', '3,7', '3,8', '4,6', '4,7', '4,8', '5,6', '5,7', '5,8'),('6,0', '6,1', '6,2', '7,0', '7,1', '7,2', '8,0', '8,1', '8,2'),('6,3', '6,4', '6,5', '7,3', '7,4', '7,5', '8,3', '8,4', '8,5'),('6,6', '6,7', '6,8', '7,6', '7,7', '7,8', '8,6', '8,7', '8,8')]
        score_board.boxes
        :return: 
        """
        # print(self.board.boxes)
        print("\n")
        print("score board: ", self.board.score_board.score_board_str)
        
        for box in self.board.boxes:
            print(box)
            
            
            if self.check_win_in_a_box(box, "x"):
                return "x"
            if self.check_win_in_a_box(box, "o"):
                return "o"
        return None


    def mark(self, player: Player, xy: str) -> None:
        if player.mark != self.turn:
            raise ValueError("Player mark does not match turn")

        self.board.place_mark(player.mark, xy)
        self.turn = self.switch_turn_in_box("o", "x")
        self.t3n = self.set_t3n()

        # curr_box = self.board.get_box_from_coordinate(xy)
        # is_win = self.check_win_in_a_box(curr_box, player.mark)



    # def mark(self, player: Player, xy: str) -> None:
    #     # if self.board.config["variant"] == "ultimate":
    # 
    #     if player.mark != self.turn:
    #         raise ValueError("Player mark does not match turn")
    # 
    #     self.board.place_mark(player.mark, xy)
    #     self.turn = self.switch_turn_in_box("o", "x")
    #     # self.board_list = self.board.to_list()
    #     self.t3n = self.set_t3n()
    # 
    #     # get score of the box where the mark is placed 
    #     # and update the score board string
    # 
    #     # TODO, this will be different if the game is ultimate tic-tac-toe
    # 
    #     # curr_box = self.board.get_box_index_from_coordinate(xy)
    #     curr_box = self.board.get_box_from_coordinate(xy)
    #     # print(xy, curr_box)
    #     is_win = self.check_win_in_a_box(curr_box, player.mark)
    #     # print(is_win)
    # 
    #     if is_win:
    #         score_board_parts = self.board.score_board.score_board_str.split(";")
    #         print("score_board_parts: ", score_board_parts)
    #         # score_board_parts[-1] =  
    # 
    #         is_scored = False
    #         for p in reversed(score_board_parts):
    #             print(p)
    #             # curr_score_box = self.board.get_box_from_coordinate(xy)
    #             # print("curr_score_box: ", curr_score_box)
    # 
    #             # curr_score_box = tuple()
    # 
    #             _result = set()
    #             for c in curr_box:
    #                 cc = c.split(",")
    #                 score_board_xy = str(int(cc[0]) // 3) + "," + str(int(cc[1]) // 3)
    #                 _result.add(score_board_xy)
    # 
    #             print("_result: ", _result)
    # 
    #             if len(_result) == 1:
    #                 # update score board string
    #                 print("update")
    # 
    #                 new_scoreboard_grid = place_mark(self.board.score_board.grid, player.mark, _result.pop())
    #                 # self.board_str = "".join(self.grid.values())
    # 
    #                 self.board.score_board.update_with_scoreboard_grid(new_scoreboard_grid)
    # 
    #                 print("#########")
    #                 print(self.board.score_board.score_board_str)
    # 
    #     # boxes = self.t3n.split(";")[-1].split("/")
    #     # print(boxes)
    # 
    #     # print(game_board_list[-1])
    #     # print("\n")
    # 
    #     # for i in range(len(boxes)):
    #     #     # print(boxes[i])
    #     #     # print("\n")
        #     self.check_win_in_a_box(player.mark)

    def set_allowed_box(self, box):
        """set allowed box (only for ultimate tic-tac-toe)"""
        pass
