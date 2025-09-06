from pyttt.board_strategy import DimensionStrategy, RowsColumnsStrategy, VariantStrategy


class Board:
    """
    the board is represented as a string of "x", "o", and "." characters
    
    ex: 
        - 3x3 board: "xoxoxoxox"
        - 9x9 board: "xxxxxxxxx x..x..xo. x..x..xo. ooooooooo x..x..xo. x..x..xo. xoxoxoxox x..x..xo. x..x..xo."
            - no whitespace in real board string
    
    the board can be initialized in three ways:
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

        # TODO: implement state
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
        return self.board

    # TODO
    def __eq__(self, other):
        pass

    def get_dimension(self) -> int:
        return int(len(self.board) ** (1 / 2))

    def get_coordinates_str(self, dim: int) -> str:
        return "".join([str(i) for i in range(dim)])

    def cross(self, vector_a, vector_b) -> tuple:
        """
        get 3x3 boards from board string
        (does not work for non-square matrices) -> TODO
        do cross product of rows and columns to get all possible 3x3 boards
        """
        return tuple(a + "," + b for a in vector_a for b in vector_b)


    def get_three_by_three(self, board_str):
        return [board_str[i:i+3] for i in range(0, len(board_str), 3)]

    def get_all_boxes(self, rows, cols):
        return [self.cross(rs, cs) for rs in rows for cs in cols]
    
    def get_all_units(self, rows, cols, boxes):
        return [self.cross(rows, c) for c in cols] + [self.cross(r, cols) for r in rows] + boxes
    
    def get_all_peers(self, units):
        return {s: set().union(*units[s]) - {s} for s in _squares}
    
    def get_units(self, squares, all_units):
        return {s: tuple(u for u in all_units if s in u) for s in squares}
    
    def get_peers(self, squares, units):
        return {s: set().union(*units[s]) - {s} for s in squares}
    
    


if __name__ == "__main__":
    _board_str = Board(dimension=(3 ** 2))
    
    
    _dim = _board_str.get_dimension()
    _coords = _board_str.get_coordinates_str(_dim)
    _rows, _cols = _coords, _coords
    _squares = _board_str.cross(_rows, _cols)
    _coords_3 = _board_str.get_three_by_three(_coords)
    _all_boxes = _board_str.get_all_boxes(_rows, _cols)
    _all_units = _board_str.get_all_units(_rows, _cols, _all_boxes)
    _units = _board_str.get_units(_squares, _all_units)
    _peers = _board_str.get_peers(_squares, _units)

    from pprintpp import pprint

    print(_board_str)
    print(_squares)
    print("coords_3", _coords_3)
    pprint(_all_boxes)
    pprint(_all_units)
    pprint(_units)
    pprint(_peers)
    pprint(_units["0,0"])
    pprint(_peers["0,0"])
