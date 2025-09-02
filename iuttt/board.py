class Board:
    def __init__(self, dimension: int = 3, rows: int | None = None, columns: int | None = None) -> None:
        self._dimension = dimension
        self._rows = rows 
        self._columns = columns

        self._init_board()

    def _init_board(self):
        if self._dimension and (not self._rows or not self._columns):
            return list("." * self._dimension)

        elif not self._dimension and (self._rows and self._columns):
            return list("." * (self._rows * self._columns))


