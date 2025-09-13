"""
pyttt/board.py
"""

from pyttt.board_strategy import DimensionStrategy, RowsColumnsStrategy, VariantStrategy
from pyttt.utils import (
    insert_char_every_n, 
    get_dimension, 
    cross, 
    get_coordinates, 
    convert_to_grid,
    get_three_by_three,
    get_all_boxes,
    display_board as display_board_util,
    get_box_index_from_coordinate,
    get_box_from_coordinate,
    get_board_str_from_box,
    get_square_value,
    get_all_units,
    get_units,
    get_peers,
)
import math


class ScoreBoard:
    def __init__(self, board_str: str = ""):
        self.score_board_str = board_str
        self.history = []
        
        if board_str:

            self.dimension = get_dimension(self.score_board_str) if self.score_board_str else 0
            self.coords = get_coordinates(self.dimension) if self.dimension > 0 else []
            self.squares = cross(vector_a=self.coords, vector_b=self.coords) if self.coords else tuple()
            self.grid = convert_to_grid(self.score_board_str, self.squares) if self.squares else {}
        else:
            self.dimension = 0
            self.coords = []
            self.squares = tuple()
            self.grid = {}

        

    def update_with_scoreboard_grid(self, grid):
        self.grid = grid 
        self.score_board_str = "".join(self.grid.values())
    
    def update(self, board_str, event: str | None = None):
        print(board_str)
        dimension = get_dimension(board_str)
        if dimension < 9:
            return ""
        
        coords = get_coordinates(dimension)
        squares = cross(vector_a=coords, vector_b=coords)

        squares_count = len(squares)
        squares_exponent = int(math.log(squares_count, 3))

        segments = []
        for i in range(2, squares_exponent, 2):
            dots = "." * (3 ** i)
            if len(dots) > 9:
                dots = insert_char_every_n(dots, "/", 9)
            segments.append(dots)
        
        self.score_board_str = ";".join(segments)
        return self.score_board_str


class Board:
    def __init__(
            self,
            variant: str | None = None,
            dimension: int | None = None,
            rows: int | None = None,
            columns: int | None = None,
            board_str: str | None = None,
    ) -> None:
        self._config = {
            "variant": variant,
            "dimension": dimension,
            "rows": rows,
            "columns": columns,
        }

        self.next = None
        self.prev = None
        self.mark_history = []
        self.history = []

        self.board_str = board_str
        if board_str is None:
            self.board_str = self._init_board()

        if dimension is None:
            dimension = self.get_dimension()
            
        self.coords = get_coordinates(dimension)
        self.squares = cross(vector_a=self.coords, vector_b=self.coords)
        self.coords_3 = get_three_by_three(self.coords)
        self.boxes = get_all_boxes(rows=self.coords_3, cols=self.coords_3)
        
        self.grid = convert_to_grid(self.board_str, self.squares)
        
        self.score_board: ScoreBoard | None = None
        
        if self.score_board is None:
            self._init_score_board()

    def _init_score_board(self) -> str:
        self.score_board = ScoreBoard()
        self.score_board.dimension = get_dimension(self.board_str)
        if self.score_board.dimension < 9:
            return ""

        self.score_board.coords = get_coordinates(self.score_board.dimension)
        self.score_board.squares = cross(vector_a=self.score_board.coords, vector_b=self.score_board.coords)
        self.score_board.grid = convert_to_grid(self.score_board.score_board_str, self.score_board.squares)
        
        squares_count = len(self.score_board.squares)
        squares_exponent = int(math.log(squares_count, 3))

        segments = []
        for i in range(2, squares_exponent, 2):
            dots = "." * (3 ** i)
            if len(dots) > 9:
                dots = insert_char_every_n(dots, "/", 9)
            segments.append(dots)

        return ";".join(segments)
    
    def __str__(self):
        return self.board_str
    
    def attach_score_board(self, score_board: ScoreBoard):
        self.score_board = score_board
        
        if len(score_board.score_board_str) == 0:
            self.score_board.update(board_str=self.board_str)
        
    def detach_score_board(self):
        self.score_board = None
        
    def notify_score_board(self, event_type: str, data):
        if self.score_board:
            self.score_board.update(event_type, self.board_str)

    @property
    def config(self) -> dict:
        return self._config

    def _init_board(self) -> str | None:
        board_str = ""

        if self._config["variant"] and (
                self._config["dimension"] is None
                and (self._config["rows"] is None and self._config["columns"] is None)
        ):
            board_str = VariantStrategy(self._config).create_board()

        if self._config["dimension"] and (
                self._config["variant"] is None
                and (self._config["rows"] is None and self._config["columns"] is None)
        ):
            board_str = DimensionStrategy(self._config).create_board()

        if (self._config["rows"] and self._config["columns"]) and (
                self._config["variant"] is None and self._config["dimension"] is None
        ):
            board_str = RowsColumnsStrategy(self._config).create_board()

        if not (
                self._config["variant"]
                or self._config["dimension"]
                or (self._config["rows"] and self._config["columns"])
        ):
            board_str = "." * 9

        return board_str

    def set_state(self):
        pass

    def __eq__(self, other):
        pass

    def get_dimension(self) -> int:
        return get_dimension(self.board_str)

    def display_board(self, t: str | None = None):
        return display_board_util(self.coords, self.grid, t)

    def get_box_index_from_coordinate(self, xy: str) -> int | None:
        return get_box_index_from_coordinate(xy, self.boxes)

    def get_box_from_coordinate(self, xy: str) -> tuple:
        return get_box_from_coordinate(xy, self.boxes)

    def get_board_str_from_box(self, box, grid) -> str:
        return get_board_str_from_box(box, grid)

    def get_square_value(self, xy, grid):
        return get_square_value(xy, grid)

    def to_list(self):
        return list(self.board_str)

    def get_all_units(self, rows, cols, boxes) -> list:
        return get_all_units(rows, cols, boxes)

    def get_units(self, squares, all_units) -> dict:
        return get_units(squares, all_units)

    def get_peers(self, squares, units) -> dict:
        return get_peers(squares, units)

    def place_mark(self, mark, xy):
        self.grid[xy] = mark
        self.board_str = "".join(self.grid.values())

    def get_legal_move(self):
        pass

    def get_allowed_boxes(self):
        if self.config is None or self.config["variant"] != "ultimate" or len(self.board_str) != 81:
            return ""
        return