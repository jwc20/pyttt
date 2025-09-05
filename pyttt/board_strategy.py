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
        return "." * (self.config["dimension"] * self.config["dimension"])


@dataclass
class RowsColumnsStrategy:
    config: dict

    def create_board(self):
        return "." * (self.config["rows"] * self.config["columns"])
