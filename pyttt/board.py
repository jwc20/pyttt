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
    partition_board_string,
    get_all_squares,
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
        # for initializing board
        self._config = {
            "variant": variant,
            "dimension": dimension,
            "rows": rows,
            "columns": columns,
        }

        self.board_str = board_str
        if board_str is None:
            self.board_str = self._init_board()

        
        # TODO:
        self.boxes = get_all_boxes(self.board_str)
        self.board_map = convert_to_grid(self.board_str, get_all_squares(self.board_str))
        # self.partitioned_board = self.partition_board_string(self.board_str)

        #############################
        # TODO: implement board state
        self.next = None
        self.prev = None
        self.mark_history = []
        self.history = []
        #############################

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

    def to_list(self):
        return list(self.board_str)

    def place_mark(self, mark, xy):
        self.board_map[xy] = mark
        self.board_str = "".join(self.board_map.values())

    def get_legal_move(self):
        pass

    def get_allowed_boxes(self):
        if self.config is None or self.config["variant"] != "ultimate" or len(self.board_str) != 81:
            return ""
        return
