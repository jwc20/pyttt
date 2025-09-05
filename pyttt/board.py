from pyttt.board_state import BoardState, NormalState


class BoardCreateStrategy:
    """
    strategy to create a board string
    """
    pass

class VariantStrategy:
    pass

class DimensionStrategy:
    pass

class RowsColumnsStrategy:

class BoardCreateContext:
    pass



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
        self._variant = variant
        self._dimension = dimension
        self._rows = rows
        self._columns = columns

        self.next = None
        self.prev = None
        self._history_moves = []

        self._board = self._init_board()

        # TODO
        # self._state: BoardState = NormalState(self)

    def _init_board(self) -> str | None:
        """
        create a board by: 
            - variant
            - dimension (width of matrix)
            - rows and columns
        """
        if self._variant and not (self._dimension or (self._rows and self._columns)):
            return self._init_variant_board()

        if self._dimension and not (self._variant or (self._rows and self._columns)):
            return "." * self._dimension

        if (self._rows and self._columns) and not (self._variant or self._dimension):
            return "." * (self._rows * self._columns)
        
        if not (self._variant or self._dimension or (self._rows and self._columns)):
            raise ValueError("Invalid board initialization")

    def _init_variant_board(self) -> str:
        if self._variant == "classic":
            return "." * 9
        raise ValueError(f"Unknown variant: {self._variant}")

    # TODO
    def set_state(self):
        pass

    # TODO
    def __repr__(self):
        pass

    # TODO
    def __eq__(self, other):
        pass
