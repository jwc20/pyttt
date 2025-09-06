from pyttt import Board

if __name__ == "__main__":
    _board_str = Board(dimension=(3 ** 2))

    _dim = _board_str.get_dimension()
    _coords = _board_str.get_coordinates_str(_dim)
    _rows, _cols = _coords, _coords
    _squares = _board_str.cross(_rows, _cols)
    _coords_3 = _board_str.get_three_by_three(_coords)
    _rows_3, _cols_3 = _coords_3, _coords_3
    _all_boxes = _board_str.get_all_boxes(_rows_3, _cols_3)
    _all_units = _board_str.get_all_units(_rows, _cols, _all_boxes)
    _units = _board_str.get_units(_squares, _all_units)
    _peers = _board_str.get_peers(_squares, _units)

    from pprintpp import pprint

    pprint(_board_str)
    # pprint(_squares)
    # pprint("coords_3", _coords_3)
    # pprint(_all_boxes)
    # pprint(_all_units)
    # pprint(_units)
    # pprint(_peers)
    # pprint(_units["0,0"])
    # pprint(_peers["0,0"])
