"""
pyttt/game.py
"""

from pyttt.board import Board
from pyttt.player import Player

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

        # TODO: deprecate
        self.board_list = self.board.to_list()
        
        self.players = players
        self.turn = turn

        # self.t3n: str = self.set_t3n()

    # def set_t3n(self):
    #     """
    #     tic-tac-toe game notation
    #     
    #     components:
    #         - current player's turn
    #         - allowed box to place mark
    #         - board string
    #         
    #     example:
    #         - ultimate tic-tac-toe:
    #             - "O;@........;X.OO...../X..X.O.O./X.X...O.O/.X.OXO.../O.O.X..../.XX....O./......X.O/.O.X.X.../.O.....XX" (example from ultimattt)
    #     """
    #     _turn = repr(self.turn)
    #     _allowed_box = None
    # 
    #     _board = []
    #     for row in self.board.partitioned_board:
    #         _board += row
    # 
    #     _board_str = "".join(_board)
    # 
    #     if self.board.config["variant"] == "ultimate":
    #         # TODO
    #         _allowed_box = "........."
    # 
    #         return "%s;%s;%s" % (_turn, _allowed_box, _board_str)
    #     return "%s;%s" % (_turn, _board_str)

    def __repr__(self):
        return "(%s, %s)" % (repr(self.turn), repr("".join(self.board_list)), )

    def __eq__(self, other):
        return self.board_list == other.board_list and self.turn == other.turn

    def switch_turn_in_box(self, x, o):
        return x if self.turn == "x" else o

    def possible_moves_in_box(self):
        return [index for index, mark in enumerate(self.board_list) if mark == "."]

    

    def check_win_in_a_box(self, box: tuple, mark: str):
        is_match = lambda line: line.count(mark) == DIM

        box_dict = {}

        for key in box:
            box_dict[key] = self.board.board_map.get(key)

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
        # print("\n")
        # print("score board: ", self.board.score_board.score_board_str)

        for box in self.board.boxes:
            # print(box)

            if self.check_win_in_a_box(box, "x"):
                return "x"
            if self.check_win_in_a_box(box, "o"):
                return "o"
        return None

    def place_mark_in_box_by_index(self, index):
        """places a mark in the given box(3x3 board)"""
        self.board_list[index] = self.turn
        self.turn = self.switch_turn_in_box("o", "x")
        return self


    def place_mark(self, player: Player, xy: str) -> None:
        if player.mark != self.turn:
            raise ValueError("Player mark does not match turn")

        self.board.place_mark(player.mark, xy)
        self.turn = self.switch_turn_in_box("o", "x")
        self.t3n = self.set_t3n()

        # curr_box = self.board.get_box_from_coordinate(xy)
        # is_win = self.check_win_in_a_box(curr_box, player.mark)
