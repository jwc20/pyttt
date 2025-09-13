"""
pyttt/utils.py
"""

def insert_char_every_n(original_string, char_to_insert, n):
    new_string = []
    for i, char in enumerate(original_string):
        new_string.append(char)
        if (i + 1) % n == 0 and (i + 1) != len(original_string):
            new_string.append(char_to_insert)
    return "".join(new_string)


def get_dimension(board_str) -> int:
    return int(len(board_str) ** (1 / 2))


def get_coordinates(dim: int) -> list:
    return [str(i) for i in range(dim)]


def cross(vector_a, vector_b) -> tuple:
    return tuple(a + "," + b for a in vector_a for b in vector_b)


def get_three_by_three(coords: list) -> tuple:
    coord_str = "".join(coords)
    return tuple([coord_str[i: i + 3] for i in range(0, len(coord_str), 3)])


def get_all_boxes(rows, cols) -> list:
    return [cross(rs, cs) for rs in rows for cs in cols]


def display_board(coords, grid, t: str | None = None):
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


def get_box_index_from_coordinate(xy: str, boxes: list) -> int | None:
    for box in boxes:
        if xy in box:
            return boxes.index(box)


def get_box_from_coordinate(xy: str, boxes: list) -> tuple:
    return boxes[get_box_index_from_coordinate(xy, boxes)]


def get_square_value(xy, grid):
    return grid[xy]


def get_board_str_from_box(box, grid) -> str:
    result = []
    for xy in box:
        square_value = get_square_value(xy, grid)
        result.append(square_value)
    return "".join(result)


def convert_to_grid(board_str, squares):
    import re
    vals = re.findall(r"[.XOxo]", board_str)
    return {
        s: v.lower() if v.lower() in "xo" else "." for s, v in zip(squares, vals)
    }


def place_mark(grid, mark, xy):
    grid[xy] = mark
    return grid


def get_all_units(rows, cols, boxes) -> list:
    return (
            [cross(rows, c) for c in cols]
            + [cross(r, cols) for r in rows]
            + boxes
    )


def get_units(squares, all_units) -> dict:
    return {s: tuple(u for u in all_units if s in u) for s in squares}


def get_peers(squares, units) -> dict:
    return {s: set().union(*units[s]) - {s} for s in squares}