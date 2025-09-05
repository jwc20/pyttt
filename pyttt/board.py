from pyttt.board_state import BoardState, NormalState

from typing import Protocol
from dataclasses import dataclass


class BoardConfigStrategy(Protocol):
    """strategy to create a board string"""

    def create_board(self): ...


class BoardConfigContext(Protocol):
    def create_board(self): ...

    def set_strategy(self, strategy: BoardConfigStrategy): ...


@dataclass
class VariantStrategy:
    config: dict
    
    def create_board(self): 
        if self.config["variant"] == "classic":
            return "." * 9
        raise ValueError(f"Unknown variant: {self.config["variant"]}")


@dataclass
class DimensionStrategy:
    config: dict
    
    def create_board(self):
        return "." * self.config["dimension"]


@dataclass
class RowsColumnsStrategy:
    config: dict 
    
    def create_board(self):
        return "." * (self.config["rows"] * self.config["columns"])


class Board:
    """
    the board can be initialized in two ways:
    - by variant (classic, ultimate, etc.)
    - by dimension 
    - by rows and columns
    """

    def __init__(
            self,
            variant: str | None = None,
            dimension: int | None = None,
            rows: int | None = None,
            columns: int | None = None
    ) -> None:
        # self._variant = variant
        # self._dimension = dimension
        # self._rows = rows
        # self._columns = columns
        
        self._config = {
            "variant": variant,
            "dimension": dimension,
            "rows": rows,
            "columns": columns
        }
        

        self.next = None
        self.prev = None
        self._history_moves = []

        self.board = self._init_board()

        # TODO
        # self._state: BoardState = NormalState(self)

    def _init_board(self) -> str | None:
        """
        create a board by: 
            - variant
            - dimension (width of matrix)
            - rows and columns
        """
        # if self._variant and not (self._dimension or (self._rows and self._columns)):
        #     return self._init_variant_board()
        # 
        # if self._dimension and not (self._variant or (self._rows and self._columns)):
        #     return "." * self._dimension
        # 
        # if (self._rows and self._columns) and not (self._variant or self._dimension):
        #     return "." * (self._rows * self._columns)
        # 
        # if not (self._variant or self._dimension or (self._rows and self._columns)):
        #     raise ValueError("Invalid board initialization")
        
        if self._config["variant"] and self._config["dimension"] is None:
            return VariantStrategy(self._config).create_board()
        
        if self._config["dimension"] and (self._config["variant"] is None and self._config["rows"] is None and self._config["columns"] is None):
            return DimensionStrategy(self._config).create_board()
        
        if (self._config["rows"] and self._config["columns"]) and (self._config["variant"] is None and self._config["dimension"] is None):
            return RowsColumnsStrategy(self._config).create_board()
        
        if not (self._config["variant"] or self._config["dimension"] or (self._config["rows"] and self._config["columns"])):
            return "." * 9
        
        # raise ValueError("Invalid board initialization")
        

    # def _init_variant_board(self) -> str:
    #     if self._variant == "classic":
    #         return "." * 9
    #     raise ValueError(f"Unknown variant: {self._variant}")

    # TODO
    def set_state(self):
        pass

    # TODO
    def __repr__(self):
        pass

    # TODO
    def __eq__(self, other):
        pass
