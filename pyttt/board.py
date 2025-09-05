from pyttt.board_state import BoardState, NormalState
from pyttt.board_strategy import VariantStrategy, DimensionStrategy, RowsColumnsStrategy

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
        if (self._config["variant"]
                and (self._config["dimension"] is None
                     and (self._config["rows"] is None and self._config["columns"] is None))):
            return VariantStrategy(self._config).create_board()

        if (self._config["dimension"]
                and (self._config["variant"] is None
                     and (self._config["rows"] is None and self._config["columns"] is None))):
            return DimensionStrategy(self._config).create_board()

        if ((self._config["rows"]
             and self._config["columns"])
                and (self._config["variant"] is None and self._config["dimension"] is None)):
            return RowsColumnsStrategy(self._config).create_board()

        if not (self._config["variant"] or self._config["dimension"] or (
                self._config["rows"] and self._config["columns"])):
            return "." * 9

    # TODO
    def set_state(self):
        pass

    # TODO
    def __repr__(self):
        pass

    # TODO
    def __eq__(self, other):
        pass
