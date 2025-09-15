"""
pyttt/board.py
"""

from pyttt.board_strategy import DimensionStrategy, RowsColumnsStrategy, VariantStrategy
from pyttt.utils import (
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

        self.board_str = board_str
        if board_str is None:
            self.board_str = self._init_board()

        self.dimension = self.get_dimension()
        self.coords = get_coordinates(self.dimension)
        self.squares = cross(vector_a=self.coords, vector_b=self.coords)
        self.coords_3 = get_three_by_three(self.coords)
        self.boxes = get_all_boxes(rows=self.coords_3, cols=self.coords_3)

        self.grid = convert_to_grid(self.board_str, self.squares)

        self.level = self.get_level()
        self.partitioned_board = self.partition_board_string(self.board_str)

        # TODO: implement board state
        self.next = None
        self.prev = None
        self.mark_history = []
        self.history = []

    def get_level(self):
        board_length = len(self.board_str)
        return (int(math.log(board_length, 3)) // 2) - 1

    def __str__(self):
        return self.board_str

    def __repr__(self):
        return self.board_str

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

    def partition_board_string(self, board_string: str):
        partitioned_board = []
        dimension = self.get_dimension()

        if dimension > 3:
            for i in range(0, len(board_string), dimension):
                partitioned_board.append(board_string[i: i + 9])
                partitioned_board.append("/")
        else:
            partitioned_board = board_string

        if partitioned_board[-1] == "/":
            partitioned_board.pop()

        return "".join(partitioned_board)
