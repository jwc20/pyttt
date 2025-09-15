"""
tests/test_board.py
"""

from unittest import TestCase

from pyttt.board import Board
from pyttt.utils import (
    convert_to_grid, 
    cross,
    get_coordinates,
    get_three_by_three,
    get_all_boxes,
    get_all_units,
    get_units,
)


class TestBoard(TestCase):
    def test_init_no_params(self):
        board = Board()
        self.assertEqual(board.board_str, "." * 9)

    def test_init_variant_classic(self):
        board = Board(variant="classic")
        self.assertEqual(board.board_str, "." * 9)
        
    def test_init_variant_ultimate(self):
        board = Board(variant="ultimate")
        self.assertEqual(board.board_str, "." * 81)

    def test_init_dimension_3x3(self):
        board = Board(dimension=3)
        self.assertEqual(board.board_str, "." * 9)
        
    def test_init_dimension_9x9(self):
        board = Board(dimension=9)
        self.assertEqual(board.board_str, "." * 81)

    def test_init_rows_columns_3x3(self):
        board = Board(rows=3, columns=3)
        self.assertEqual(board.board_str, "." * 9)

    def test_init_rows_columns_3x4(self):
        board = Board(rows=3, columns=4)
        self.assertEqual(board.board_str, "." * 12)

    # def test_cross(self):
    #     board = Board(dimension=3)
    #     dim = board.get_dimension()
    #     coords = get_coordinates(dim)
    #     self.assertEqual(cross(coords, coords), ("0,0", "0,1", "0,2", "1,0", "1,1", "1,2", "2,0", "2,1", "2,2"))
    # 
    # def test_get_three_by_three(self):
    #     board = Board(dimension=9)
    #     dim = board.get_dimension()
    #     coords = get_coordinates(dim)
    #     self.assertEqual(get_three_by_three(coords), ("012", "345", "678"))
    # 
    # def test_get_all_boxes(self):
    #     board = Board(dimension=9)
    #     dim = board.get_dimension()
    #     coords = get_coordinates(dim)
    #     coords_3 = get_three_by_three(coords)
    #     rows, cols = coords_3, coords_3
    #     output = "[('0,0', '0,1', '0,2', '1,0', '1,1', '1,2', '2,0', '2,1', '2,2'),('0,3', '0,4', '0,5', '1,3', '1,4', '1,5', '2,3', '2,4', '2,5'),('0,6', '0,7', '0,8', '1,6', '1,7', '1,8', '2,6', '2,7', '2,8'),('3,0', '3,1', '3,2', '4,0', '4,1', '4,2', '5,0', '5,1', '5,2'),('3,3', '3,4', '3,5', '4,3', '4,4', '4,5', '5,3', '5,4', '5,5'),('3,6', '3,7', '3,8', '4,6', '4,7', '4,8', '5,6', '5,7', '5,8'),('6,0', '6,1', '6,2', '7,0', '7,1', '7,2', '8,0', '8,1', '8,2'),('6,3', '6,4', '6,5', '7,3', '7,4', '7,5', '8,3', '8,4', '8,5'),('6,6', '6,7', '6,8', '7,6', '7,7', '7,8', '8,6', '8,7', '8,8')]"
    #     self.assertEqual(get_all_boxes(rows, cols), eval(output))
    # 
    # def test_get_all_units(self):
    #     board = Board(dimension=3)
    #     dim = board.get_dimension()
    #     coords = get_coordinates(dim)
    #     coords_3 = get_three_by_three(coords)
    #     rows, cols = coords, coords
    #     rows_3, cols_3 = coords_3, coords_3
    #     boxes = get_all_boxes(rows_3, cols_3)
    #     output = "[('0,0', '1,0', '2,0'),('0,1', '1,1', '2,1'),('0,2', '1,2', '2,2'),('0,0', '0,1', '0,2'),('1,0', '1,1', '1,2'),('2,0', '2,1', '2,2'),('0,0', '0,1', '0,2', '1,0', '1,1', '1,2', '2,0', '2,1', '2,2')]"
    #     self.assertEqual(board.get_all_units(rows, cols, boxes), eval(output))
    # 
    # def test_get_units(self):
    #     board = Board(dimension=3)
    #     dim = board.get_dimension()
    #     coords = get_coordinates(dim)
    #     rows, cols = coords, coords
    #     squares = cross(rows, cols)
    #     coords_3 = get_three_by_three(coords)
    #     rows_3, cols_3 = coords_3, coords_3
    #     all_boxes = get_all_boxes(rows_3, cols_3)
    #     all_units = get_all_units(rows, cols, all_boxes)
    #     units = board.get_units(squares, all_units)
    #     output = "(('0,0', '1,0', '2,0'),('0,0', '0,1', '0,2'),('0,0', '0,1', '0,2', '1,0', '1,1', '1,2', '2,0', '2,1', '2,2'))"
    #     self.assertEqual(units["0,0"], eval(output))
    # 
    # def test_get_peers(self):
    #     board = Board(dimension=3)
    #     dim = board.get_dimension()
    #     coords = get_coordinates(dim)
    #     rows, cols = coords, coords
    #     squares = cross(rows, cols)
    #     coords_3 = get_three_by_three(coords)
    #     rows_3, cols_3 = coords_3, coords_3
    #     all_boxes = get_all_boxes(rows_3, cols_3)
    #     all_units = get_all_units(rows, cols, all_boxes)
    #     units = get_units(squares, all_units)
    #     peers = board.get_peers(squares, units)
    #     output = "{'2,2', '1,0', '0,2', '0,1', '1,2', '1,1', '2,0', '2,1'}"
    #     self.assertEqual(peers["0,0"], eval(output))
    # 
    # 
    # def test_get_board_str_from_box(self):
    #     board = Board(dimension=3)
    #     dim = board.get_dimension()
    #     coords = get_coordinates(dim)
    #     rows, cols = coords, coords
    #     squares = cross(rows, cols)
    #     coords_3 = get_three_by_three(coords)
    #     rows_3, cols_3 = coords_3, coords_3
    #     boxes = get_all_boxes(rows_3, cols_3)
    #     box_0 = boxes[0]
    #     grid = convert_to_grid(board.board_str, squares)
    #     output = "........."
    #     self.assertEqual(board.get_board_str_from_box(box_0, grid), output)
    # 
    # 
    # def test_get_square_value(self):
    #     board = Board(dimension=9)
    #     dim = board.get_dimension()
    #     coords = get_coordinates(dim)
    #     rows, cols = coords, coords
    #     squares = cross(rows, cols)
    #     grid = convert_to_grid(board.board_str, squares)
    #     square_01 = board.get_square_value("0,1", grid)
    #     self.assertEqual(square_01, ".")
    # 
    # 
    # def test_parse(self):
    #     board = Board(dimension=3)
    #     dim = board.get_dimension()
    #     coords = get_coordinates(dim)
    #     rows, cols = coords, coords
    #     squares = cross(rows, cols)
    # 
    #     grid = convert_to_grid(board.board_str, squares)
    #     output={'0,0': '.', '0,1': '.', '0,2': '.', '1,0': '.', '1,1': '.', '1,2': '.', '2,0': '.', '2,1': '.', '2,2': '.'}
    #     self.assertEqual(grid, output)
    # 
    # 
    # def test_get_box_number_from_coordinate(self):
    #     board = Board(dimension=9)
    # 
    #     self.assertEqual(board.get_box_index_from_coordinate("0,0"), 0)
    #     self.assertEqual(board.get_box_index_from_coordinate("3,1"), 3)
    #     self.assertEqual(board.get_box_index_from_coordinate("8,8"), 8)
    #     
    # def test_get_box_from_coordinate(self):
    #     board = Board(dimension=9)
    #     self.assertEqual(board.get_box_from_coordinate("0,0"), ('0,0', '0,1', '0,2', '1,0', '1,1', '1,2', '2,0', '2,1', '2,2'))