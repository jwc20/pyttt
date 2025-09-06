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
            columns: int | None = None,
    ) -> None:
        self._config = {
            "variant": variant,
            "dimension": dimension,
            "rows": rows,
            "columns": columns,
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
        if self._config["variant"] and (
                self._config["dimension"] is None
                and (self._config["rows"] is None and self._config["columns"] is None)
        ):
            return VariantStrategy(self._config).create_board()

        if self._config["dimension"] and (
                self._config["variant"] is None
                and (self._config["rows"] is None and self._config["columns"] is None)
        ):
            return DimensionStrategy(self._config).create_board()

        if (self._config["rows"] and self._config["columns"]) and (
                self._config["variant"] is None and self._config["dimension"] is None
        ):
            return RowsColumnsStrategy(self._config).create_board()

        if not (
                self._config["variant"]
                or self._config["dimension"]
                or (self._config["rows"] and self._config["columns"])
        ):
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

    def get_three_by_three(self, board_str) -> tuple:
        return tuple([board_str[i: i + 3] for i in range(0, len(board_str), 3)])

    def get_all_boxes(self, rows, cols) -> list:
        """
        get all possible 3x3 boxes
        """
        return [self.cross(rs, cs) for rs in rows for cs in cols]

    def get_all_units(self, rows, cols, boxes) -> list:
        return (
                [self.cross(rows, c) for c in cols]
                + [self.cross(r, cols) for r in rows]
                + boxes
        )

    def get_units(self, squares, all_units) -> dict:
        """
        get all units that contain each square

        a unit is a row, column, or box; each unit is a tuple of 9(or more) squares
        """
        return {s: tuple(u for u in all_units if s in u) for s in squares}

    def get_peers(self, squares, units) -> dict:
        """the squares that share a unit are called peers."""
        return {s: set().union(*units[s]) - {s} for s in squares}

    def parse(self, board_str, squares):
        """Convert a string to a Tic-Tac-Toe grid."""
        import re
        vals = re.findall(r"[.XOxo]", board_str)
        return {
            s: v.lower() if v.lower() in "xo" else "." for s, v in zip(squares, vals)
        }

    def picture(self, grid, rows, cols):
        """
        convert board string to grid

        TODO:
        (works only for 3x3 and 9x9 boards)
        """
        if grid is None:
            return "None"

        width = 1 + max(len(grid[s]) for s in grid)
        line = "+".join(["-" * (width * 3)] * (len(cols) // 3))

        result = []
        for r in rows:
            row_str = "".join(
                grid[r + "," + c].center(width)
                + ("|" if (int(c) + 1) % 3 == 0 and int(c) + 1 < len(cols) else "")
                for c in cols
            )
            result.append(row_str)
            if (int(r) + 1) % 3 == 0 and int(r) + 1 < len(rows):
                result.append(line)

        return "\n".join(result)
