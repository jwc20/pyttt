from pyttt.board_state import BoardState, NormalState


class Board:
    def __init__(
            self, variant: str | None = None,
            dimension: int | None = None,
            rows: int | None = None,
            columns: int | None = None
    ) -> None:
        self._variant = variant
        self._dimension = dimension
        self._rows = rows
        self._columns = columns
        self._state: BoardState = NormalState(self)
        self._init_board()

        self.next = None
        self.prev = None
        self._history_moves = []
        
        self._board = self._init_board()


    # TODO
    def __repr__(self):
        pass

    # TODO
    def __eq__(self, other):
        pass

    def _init_board(self) -> list[str]:
        """create a board either by dimension or rows and columns"""
        if self._variant:
            return self._init_variant_board()
        if not self._dimension and (self._rows and self._columns):
            return list("." * (self._rows * self._columns))
        return list("." * self._dimension)

    def _init_variant_board(self) -> list[str]:
        if self._variant == "classic":
            return list("." * 9)
        raise ValueError(f"Unknown variant: {self._variant}")

    def set_state(self):
        pass
