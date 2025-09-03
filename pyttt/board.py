from ttt.board_state import BoardState, NormalState

class Board:
    def __init__(
        self, variant: str = "square", dimension: int | None = None, rows: int | None = None, columns: int | None = None
    ) -> None:
        self._dimension = dimension
        self._rows = rows
        self._columns = columns
        self._state: BoardState = NormalState(self)
        self._init_board()
        
        self.next = None
        self.prev = None

    def _init_board(self) -> list[str]:
        """create a board either by dimension or rows and columns"""
        if not self._dimension and (self._rows and self._columns):
            return list("." * (self._rows * self._columns))
        return list("." * self._dimension)

    def set_state(self):
        pass