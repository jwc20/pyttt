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
        
        # TODO: 
        # self.t3n: str = self.t3n()
        self.score_board_str: str | None = None
     
       
    def init_score_board(self) -> str:
        """
        initialize score board
        
        output:
        - if the board is 3x3, return ""
        - if the board is 9x9, return "........."
        - if the board is 27x27, return ".........;........./........./........./........./........./........./........./........./........."
        - and so on
        """
        # print(self.board.get_dimension())
        _dim = self.board.get_dimension()
        # print("\n", _dim)
        if _dim < 9:
            return ""
        
        _result = []
        
        _boxes = self.board.boxes
        _squares_count = len(self.board.squares)
        
        
        
        # print(_squares_count)
        # print("\n", _boxes)
        
        import math 
        
        _squares_exponent = int(math.log(_squares_count, 3))
        print("\n squares exponent", _squares_exponent)
        
        for i in range(2, _squares_exponent, 2):
            _result.append("." * (3 ** i))
            print(i)

        _new_result = []
        
        for s in _result:
            if len(s) > 9:
                _new_result.append(self.insert_char_every_n(s, "/", 9))
            else:
                _new_result.append(s)
        
            
        print("\n result: ", _new_result)
        
        # while _dim > 1:
            # _dim //= 9
            # for i in range(_dim):
            #     _result.append("." * 9)
            #     if self.board.get_dimension() != 9:
            #         _result.append("/")

        print("\n")
        print("\n$$", ";".join(_new_result))
        print("\n")
        return ";".join(_new_result)

    def insert_char_every_n(self, original_string, char_to_insert, n):
        new_string = []
        for i, char in enumerate(original_string):
            new_string.append(char)
            if (i + 1) % n == 0 and (i + 1) != len(original_string):
                new_string.append(char_to_insert)
        return "".join(new_string)

    def t3n(self):
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
        
        _partitioned_board = []
        for i in range(0, len(self.board_list), self.board.get_dimension()):
            _partitioned_board.append(self.board_list[i: i + self.board.get_dimension()])
            _partitioned_board.append("/")
            
        _board = [] 
        for row in _partitioned_board:
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

    def switch_turn(self, x, o):
        return x if self.turn == "x" else o
    
    def place_mark(self):
        # if self.board.config["variant"] == "ultimate":
        return

    def place_mark_in_box(self, index):
        """places a mark in the given box(3x3 board)"""
        self.board_list[index] = self.turn
        self.turn = self.switch_turn("o", "x")
        return self

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
        value = self.switch_turn(max, min)(values)
        self.cache[key] = value
        return value

    def best_move(self):
        fn = self.switch_turn(max, min)
        return fn(
            self.possible_moves_in_box(),
            key=lambda index: deepcopy(self).place_mark_in_box(index).minimax(),
        )

    def is_game_end(self):
        return (
                self.check_win_in_box("x") or self.check_win_in_box("o") or self.board_list.count(".") == 0
        )
