from pyttt import Board, Game
from pprintpp import pprint

if __name__ == "__main__":
    pprint("hello")
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

    

    # pprint(_board_str)
    # pprint(_squares)
    # pprint("coords_3", _coords_3)
    # pprint(_coords_3)
    # pprint(_all_boxes)
    # pprint(_all_units)
    # pprint(_units)
    # pprint(_peers)
    # pprint(_units["0,0"])
    # pprint(_peers["0,0"])

    _grid = _board_str.parse(_board_str.board_str, _squares)
    
    # print(_grid)
    # print(_board_str.picture(_grid, _rows, _cols))




    # pprint(_all_boxes)
    print("\n")
    print("\n")
    print("\n")
    # pprint(_all_boxes[0])
    
    # def get_box_values(box):
    #     return "".join(_grid[box])
    

    # need to get box values ("x", "o", or ".") with coordinates ("0,0", "0,1", etc.)
    # returns a string of "x", "o", or ".". (example: "xoxoxoxox")
    _box_0 = _all_boxes[0]

    # _r = []
    # for s in _box_0:
    #     _r.append(_grid[s])
    # _box_0_str = "".join(_r)

    _box_0_str = _board_str.get_board_str_from_box(_box_0, _grid)
    # print("######################")
    # pprint(_box_0)
    # print("\n")
    # pprint(_grid)
    # print("board string from box: ", _box_0_str)
    # print("######################")
    # 
    # square_01 = _board_str.get_square_value("0,1", _grid)
    # print("square 0,1: ", square_01)
    # 
    # square_12 = _board_str.get_square_value("1,2", _grid)
    # print("square 1,2: ", square_12)

    
    ###############################################
    
    # game = Game()
    # 
    # print("repr: ", game)
    # print("t3n: ", game.t3n())

    game_ult = Game(Board(variant="ultimate"))
    print("repr: ", game_ult)
    print("\n")
    print("t3n: ", game_ult.t3n())


    
    


    
    
    
