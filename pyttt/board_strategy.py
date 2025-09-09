"""
TODO:
consider changing this to facade pattern
"""


from dataclasses import dataclass
from typing import Protocol


class BoardConfigStrategy(Protocol):
    """strategy to create a board string"""

    def create_board(self): ...


class BoardConfigContext(Protocol):
    def create_board(self): ...

    def set_strategy(self, strategy: BoardConfigStrategy): ...


@dataclass
class VariantStrategy:
    """
    note that ultimate tic-tac-toe is different from a 9x9 tic-tac-toe
        - different rules to win
        - the position where you place your mark determines which small board(3x3 grid, box) your opponent must play in next.
    """
    config: dict

    def create_board(self):
        if self.config["variant"] == "classic":
            return "." * 9
        if self.config["variant"] == "ultimate":
            return "." * 81
        raise ValueError(f"Unknown variant: {self.config["variant"]}")


@dataclass
class DimensionStrategy:
    config: dict

    def create_board(self):
        return "." * (self.config["dimension"] * self.config["dimension"])


# note: probably not needed
@dataclass
class RowsColumnsStrategy:
    config: dict

    def create_board(self):
        return "." * (self.config["rows"] * self.config["columns"])
