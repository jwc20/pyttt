def insert_char_every_n(original_string, char_to_insert, n):
    new_string = []
    for i, char in enumerate(original_string):
        new_string.append(char)
        if (i + 1) % n == 0 and (i + 1) != len(original_string):
            new_string.append(char_to_insert)
    return "".join(new_string)



#########################################################
# board utils ###########################################
#########################################################
def get_dimension(board_str) -> int:
    return int(len(board_str) ** (1 / 2))


def get_coordinates(dim: int) -> list:
    # return "".join([str(i) for i in range(dim)])
    return [str(i) for i in range(dim)]

def cross(vector_a, vector_b) -> tuple:
    """
    get 3x3 boards from board string
    (does not work for non-square matrices) -> TODO
    do cross product of rows and columns to get all possible 3x3 boards
    """

    return tuple(a + "," + b for a in vector_a for b in vector_b)

def get_three_by_three(coords: list) -> tuple:
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

def get_all_boxes(rows, cols) -> list:
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
    return [cross(rs, cs) for rs in rows for cs in cols]

def display_board(coords, grid, t: str | None = None):
    """
    t: type
    convert board string to grid
    """
    if t is None:
        t = "value"
    rows, cols = coords, coords
    if grid is None:
        return "None"
    result_row = []
    result = []
    for c in cols:
        result_row.append("\n")
        for r in rows:
            if t == "coordinate":
                result_row.append(str(r + "," + c).center(10))
            else:
                result_row.append(grid[r + "," + c])
    result.append(" ".join(result_row))
    return "".join(result)


def get_box_index_from_coordinate(xy: str, boxes: tuple) -> int | None:
    """
    get box number from coordinate
    :param xy: 
    :return: int

    :example:
        - xy = "0,0"
        - return = 0
    """
    for box in boxes:
        if xy in box:
            return boxes.index(box)

def get_box_from_coordinate(xy: str, boxes: tuple) -> tuple:
    """
    get box from coordinate
    :param xy: 
    :return: tuple

    :example:
        - xy = "0,0"
        - return = ('0,0', '0,1', '0,2', '1,0', '1,1', '1,2', '2,0', '2,1', '2,2')
    """
    return boxes[get_box_index_from_coordinate(xy)]


def get_square_value(xy, grid):
    """get square value from coordinates"""
    return grid[xy]

def get_board_str_from_box(box, grid) -> str:
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
        square_value = get_square_value(xy, grid)
        result.append(square_value)
    return "".join(result)


def convert_to_grid(board_str, squares):
    """Convert a string to a Tic-Tac-Toe grid."""
    import re

    vals = re.findall(r"[.XOxo]", board_str)
    return {
        s: v.lower() if v.lower() in "xo" else "." for s, v in zip(squares, vals)
    }

def place_mark(grid, mark, xy):
    grid[xy] = mark
    
    return grid