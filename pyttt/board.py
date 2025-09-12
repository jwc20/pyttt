from pyttt.board_strategy import DimensionStrategy, RowsColumnsStrategy, VariantStrategy
from pyttt.utils import insert_char_every_n, get_dimension, cross, get_coordinates, convert_to_grid
import math

class ScoreBoard:
    def __init__(self):
        self.score_board_str = ""
        # if self.score_board_str == "":
        #     self.score_board_str = self._init_score_board()
        
        self.history = []

        self.dimension = get_dimension(self.score_board_str)
        self.coords = get_coordinates(self.dimension)
        self.squares = cross(vector_a=self.coords, vector_b=self.coords)
        self.grid = convert_to_grid(self.score_board_str, self.squares)
        
        # self.squares = cross(self.score_board_str, )
        if len(self.score_board_str) > 0:
            self.dimension = get_dimension(self.score_board_str)
            self.coords = get_coordinates(self.dimension)
            self.squares = cross(vector_a=self.coords, vector_b=self.coords)
            self.grid = convert_to_grid(self.score_board_str, self.squares)
    

    
    def update_with_scoreboard_grid(self, grid):
        self.grid = grid 
        self.score_board_str = "".join(self.grid.values())
    
    def update(self,  board_str, event: str | None = None):
        print(board_str)
        dimension = get_dimension(board_str)
        if dimension < 9:
            return ""
        
        coords = get_coordinates(dimension)
        squares = cross(vector_a=coords, vector_b=coords)
        

        squares_count = len(squares)
        squares_exponent = int(math.log(squares_count, 3))

        segments = []
        for i in range(2, squares_exponent, 2):
            dots = "." * (3 ** i)
            if len(dots) > 9:
                dots = insert_char_every_n(dots, "/", 9)
            segments.append(dots)
        
        self.score_board_str = ";".join(segments)
        return self.score_board_str
        


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
            board_str: str | None = None,
    ) -> None:
        self._config = {
            "variant": variant,
            "dimension": dimension,
            "rows": rows,
            "columns": columns,
        }

        self.next = None
        self.prev = None
        self.mark_history = []
        self.history = []

        self.board_str = board_str
        # self.board = None
        if board_str is None:
            self.board_str = self._init_board()  # board string

        # self._squares = [Square(x, y) for x in range(self.get_dimension()) for y in range(self.get_dimension())]
        # print(self._squares)

        # TODO: implement state
        # self._state: BoardState = NormalState(self)

        if dimension is None:
            dimension = self.get_dimension()
            
        self.coords = self.get_coordinates(dimension)
        self.squares = self.cross(vector_a=self.coords, vector_b=self.coords)
        self.coords_3 = self.get_three_by_three(self.coords)
        self.boxes = self.get_all_boxes(rows=self.coords_3, cols=self.coords_3)
        
        self.grid = self.convert_to_grid(self.board_str, self.squares)
        
        self.score_board: ScoreBoard | None = None
        
        if self.score_board is None:
            self._init_score_board()



    def _init_score_board(self) -> str:
        self.score_board = ScoreBoard()
        self.score_board.dimension = get_dimension(self.board_str)
        if self.score_board.dimension < 9:
            return ""

        self.score_board.coords = get_coordinates(self.score_board.dimension)
        self.score_board.squares = cross(vector_a=self.score_board.coords, vector_b=self.score_board.coords)
        self.score_board.grid = convert_to_grid(self.score_board.score_board_str, self.score_board.squares)
        
        squares_count = len(self.score_board.squares)
        squares_exponent = int(math.log(squares_count, 3))

        segments = []
        for i in range(2, squares_exponent, 2):
            dots = "." * (3 ** i)
            if len(dots) > 9:
                dots = insert_char_every_n(dots, "/", 9)
            segments.append(dots)

        return ";".join(segments)
    
    
    def __str__(self):
        return self.board_str
    
    def attach_score_board(self, score_board: ScoreBoard):
        self.score_board = score_board
        
        if len(score_board.score_board_str) == 0:
            self.score_board.update(board_str=self.board_str)
        
        
        
    def detach_score_board(self):
        self.score_board = None
        
    def notify_score_board(self, event_type: str, data):
        if self.score_board:
            self.score_board.update(event_type, self.board_str)

    @property
    def config(self) -> dict:
        return self._config

    def _init_board(self) -> str | None:
        """
        create a board by:
            - variant
            - dimension (width of matrix)
            - rows and columns
        """

        board_str = ""

        if self._config["variant"] and (
                self._config["dimension"] is None
                and (self._config["rows"] is None and self._config["columns"] is None)
        ):
            board_str = VariantStrategy(self._config).create_board()

        if self._config["dimension"] and (
                self._config["variant"] is None
                and (self._config["rows"] is None and self._config["columns"] is None)
        ):
            board_str = DimensionStrategy(self._config).create_board()

        if (self._config["rows"] and self._config["columns"]) and (
                self._config["variant"] is None and self._config["dimension"] is None
        ):
            board_str = RowsColumnsStrategy(self._config).create_board()

        if not (
                self._config["variant"]
                or self._config["dimension"]
                or (self._config["rows"] and self._config["columns"])
        ):
            board_str = "." * 9  # classic ttt

        return board_str

    # TODO
    def set_state(self):
        pass

    # TODO
    # def __repr__(self):
    #     """
    #     returns string like "xxxxxxxxxx..x..xo.x..x..xo.ooooooooox..x..xo.x..x..xo.xoxoxoxoxx..x..xo.x..x..xo."
    #     """
    #     return self.board_str

    # TODO
    def __eq__(self, other):
        pass

    def get_dimension(self) -> int:
        return int(len(self.board_str) ** (1 / 2))

    def get_coordinates(self, dim: int) -> list:
        # return "".join([str(i) for i in range(dim)])
        return [str(i) for i in range(dim)]

    def cross(self, vector_a, vector_b) -> tuple:
        """
        get 3x3 boards from board string
        (does not work for non-square matrices) -> TODO
        do cross product of rows and columns to get all possible 3x3 boards
        """
        
        
        return tuple(a + "," + b for a in vector_a for b in vector_b)

    def get_three_by_three(self, coords: list) -> tuple:
        """
        get 3x3 boards from board string
        :param board_str: 
        :return: tuple
        
        :example:
            - 9x9 board
            - return = ('012', '345', '678')
        """
        coord_str = "".join(coords)
        return tuple([coord_str[i: i + 3] for i in range(0, len(coord_str), 3)])

    def get_all_boxes(self, rows, cols) -> list:
        """
        get all possible 3x3 boxes
        :param rows: 
        :param cols: 
        :return: list of 3x3 boxes
        
        :example:
            - rows = ('012', '345', '678')
            - cols = ('012', '345', '678')
            - return = [
                        ('0,0', '0,1', '0,2', '1,0', '1,1', '1,2', '2,0', '2,1', '2,2'),
                        ('0,3', '0,4', '0,5', '1,3', '1,4', '1,5', '2,3', '2,4', '2,5'),
                        ('0,6', '0,7', '0,8', '1,6', '1,7', '1,8', '2,6', '2,7', '2,8'),
                        ('3,0', '3,1', '3,2', '4,0', '4,1', '4,2', '5,0', '5,1', '5,2'),
                        ('3,3', '3,4', '3,5', '4,3', '4,4', '4,5', '5,3', '5,4', '5,5'),
                        ('3,6', '3,7', '3,8', '4,6', '4,7', '4,8', '5,6', '5,7', '5,8'),
                        ('6,0', '6,1', '6,2', '7,0', '7,1', '7,2', '8,0', '8,1', '8,2'),
                        ('6,3', '6,4', '6,5', '7,3', '7,4', '7,5', '8,3', '8,4', '8,5'),
                        ('6,6', '6,7', '6,8', '7,6', '7,7', '7,8', '8,6', '8,7', '8,8'),
            ]
        """
        return [self.cross(rs, cs) for rs in rows for cs in cols]

    def display_board(self, t: str | None = None):
        """
        convert board string to grid
        """
        if t is None:
            t = "value"
        rows, cols = self.coords, self.coords
        if self.grid is None:
            return "None"
        result_row = []
        result = []
        for c in cols:
            result_row.append("\n")
            for r in rows:
                if t == "coordinate":
                    result_row.append(str(r + "," + c).center(10))
                else:
                    result_row.append(self.grid[r + "," + c])
        result.append(" ".join(result_row))
        return "".join(result)

    # def display_board(self):
    #     """
    #     convert board string to grid
    # 
    #     TODO:
    #     (works only for 3x3 and 9x9 boards)
    #     """
    #     
    #     rows, cols = self.coords, self.coords
    #     
    #     if self.grid is None:
    #         return "None"
    # 
    #     width = 1 + max(len(self.grid[s]) for s in self.grid)
    #     line = "+".join(["-" * (width * 3)] * (len(cols) // 3))
    # 
    #     result = []
    #     for r in rows:
    #         row_str = "".join(
    #             self.grid[r + "," + c].center(width)
    #             + ("|" if (int(c) + 1) % 3 == 0 and int(c) + 1 < len(cols) else "")
    #             for c in cols
    #         )
    #         result.append(row_str)
    #         if (int(r) + 1) % 3 == 0 and int(r) + 1 < len(rows):
    #             result.append(line)
    # 
    #     return "\n".join(result)

    def get_box_index_from_coordinate(self, xy: str) -> int | None:
        """
        get box number from coordinate
        :param xy: 
        :return: int
        
        :example:
            - xy = "0,0"
            - return = 0
        """
        for box in self.boxes:
            if xy in box:
                return self.boxes.index(box)

    def get_box_from_coordinate(self, xy: str) -> tuple:
        """
        get box from coordinate
        :param xy: 
        :return: tuple
        
        :example:
            - xy = "0,0"
            - return = ('0,0', '0,1', '0,2', '1,0', '1,1', '1,2', '2,0', '2,1', '2,2')
        """
        return self.boxes[self.get_box_index_from_coordinate(xy)]

    def get_board_str_from_box(self, box, grid) -> str:
        """
        get board string from box
        :param box: 
        :param grid: 
        :return: string
        
        :example:
            - box = ('0,0', '0,1', '0,2', '1,0', '1,1', '1,2', '2,0', '2,1', '2,2')
            - grid = {'0,0': '.', '0,1': '.', '0,2': '.', '0,3': '.', '0,4': '.', '0,5': '.', '0,6': '.', '0,7': '.', '0,8': '.', '1,0': '.', '1,1': '.', '1,2': '.', '1,3': '.', '1,4': '.', '1,5': '.', '1,6': '.', '1,7': '.', '1,8': '.', '2,0': '.', '2,1': '.', '2,2': '.', '2,3': '.', '2,4': '.', '2,5': '.', '2,6': '.', '2,7': '.', '2,8': '.', '3,0': '.', '3,1': '.', '3,2': '.', '3,3': '.', '3,4': '.', '3,5': '.', '3,6': '.', '3,7': '.', '3,8': '.', '4,0': '.', '4,1': '.', '4,2': '.', '4,3': '.', '4,4': '.', '4,5': '.', '4,6': '.', '4,7': '.', '4,8': '.', '5,0': '.', '5,1': '.', '5,2': '.', '5,3': '.', '5,4': '.', '5,5': '.', '5,6': '.', '5,7': '.', '5,8': '.', '6,0': '.', '6,1': '.', '6,2': '.', '6,3': '.', '6,4': '.', '6,5': '.', '6,6': '.', '6,7': '.', '6,8': '.', '7,0': '.', '7,1': '.', '7,2': '.', '7,3': '.', '7,4': '.', '7,5': '.', '7,6': '.', '7,7': '.', '7,8': '.', '8,0': '.', '8,1': '.', '8,2': '.', '8,3': '.', '8,4': '.', '8,5': '.', '8,6': '.', '8,7': '.', '8,8': '.'}
            - return = "........."
        """
        result = []
        for xy in box:
            # xy is str coordinates like "0,0"
            square_value = self.get_square_value(xy, grid)
            result.append(square_value)
        return "".join(result)

    def get_square_value(self, xy, grid):
        """get square value from coordinates"""
        return grid[xy]

    def to_list(self):
        return list(self.board_str)

    ##################################################################
    # will probably not use
    ##################################################################

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

    def convert_to_grid(self, board_str, squares):
        """Convert a string to a Tic-Tac-Toe grid."""
        import re

        vals = re.findall(r"[.XOxo]", board_str)
        return {
            s: v.lower() if v.lower() in "xo" else "." for s, v in zip(squares, vals)
        }

    ##################################################################

    # TODO
    def place_mark(self, mark, xy):
        self.grid[xy] = mark
        self.board_str = "".join(self.grid.values())
        # print(self.board_str)
        # self.grid = self.convert_to_grid(self.board_str, self.squares)
        # print(self.grid)
        
        

    def get_legal_move(self):
        pass

    def get_allowed_boxes(self):
        """for ultimate tic-tac-toe"""
        if self.config is None or self.config["variant"] != "ultimate" or len(self.board_str) != 81:
            return ""

        # allowed_boxes = ""
        return



