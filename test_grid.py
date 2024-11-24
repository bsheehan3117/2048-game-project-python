'''
    Brendan Sheehan
    CS5001
    Project 2048

    This program tests the Grid class.  Imports from
    Grid.py and tests the Grid class by creating objects
    and calling methods on those objects, making sure
    the values of the attributes are what we expect.
'''

import unittest
from Grid import Grid

class TestGrid(unittest.TestCase):
    
    def setUp(self):
        # set up a grid
        self.grid = Grid(4,[[0 ,2 ,4 ,8 ],[16, 32, 64, 128],[256, 512, 1024, 0],[0, 0, 0, 0]])
        
    def test_create_squares(self):
        '''
        tests the create_squares method which
        creates a list of square objects.
        '''
        
        # test 1 - test squares 32 times (16 in grid,
        # 16 when checking for 2048 to win game)
        self.grid.create_squares()
        self.assertEqual(len(self.grid.squares), 32)
        
        # test 2 -  test that numbers and colors match 
        self.assertEqual(self.grid.squares[0].number, 0)
        self.assertEqual(self.grid.squares[0].color, "grey")
        self.assertEqual(self.grid.squares[1].color, "orange")
        self.assertEqual(self.grid.squares[2].color, "red")
        self.assertEqual(self.grid.squares[3].color, "blue")
        self.assertEqual(self.grid.squares[4].color, "green")
        self.assertEqual(self.grid.squares[5].color, "purple")
        self.assertEqual(self.grid.squares[6].color, "brown")
        self.assertEqual(self.grid.squares[7].color, "navy")
        self.assertEqual(self.grid.squares[8].color, "magenta")
        self.assertEqual(self.grid.squares[9].color, "lime")
        self.assertEqual(self.grid.squares[10].color, "violet")
        self.assertEqual(self.grid.squares[11].color, "grey")
        self.assertEqual(self.grid.squares[12].color, "grey")
        self.assertEqual(self.grid.squares[13].color, "grey")
        self.assertEqual(self.grid.squares[14].color, "grey")
        self.assertEqual(self.grid.squares[15].color, "grey")

        # test 3 - test positioning of squares in grid
        self.assertEqual(self.grid.squares[0].x, -150)
        self.assertEqual(self.grid.squares[0].y, -150)

    def test_init(self):
        '''
        tests the __init__ method which
        creates new Grid objects.
        '''
        
        # test 1 - test initializing a grid object with empty squares
        grid = Grid(4, [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
        self.assertEqual(grid.size, 4)
        self.assertEqual(grid.numbers, [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
        self.assertEqual(len(grid.squares), 16)
        self.assertEqual(grid.colors, {
            0: "grey",
            2: "orange",
            4: "red",
            8: "blue",
            16: "green",
            32: "purple",
            64: "brown",
            128: "navy",
            256: "magenta",
            512: "lime",
            1024: "violet",
            2048: "gold"
        })
        self.assertEqual(grid.score, 0)
        
        # test - 2 test initializing a Grid object with numbers in sqs
        grid = Grid(4,[[0 ,2 ,4 ,8 ],[16, 32, 64, 128],[256, 512, 1024, 0],[0, 0, 0, 0]])
        self.assertEqual(grid.size, 4)
        self.assertEqual(grid.numbers, [[0 ,2 ,4 ,8 ],[16, 32, 64, 128],[256, 512, 1024, 0],[0, 0, 0, 0]])
        self.assertEqual(len(grid.squares), 16)
        self.assertEqual(grid.colors, {
            0: "grey",
            2: "orange",
            4: "red",
            8: "blue",
            16: "green",
            32: "purple",
            64: "brown",
            128: "navy",
            256: "magenta",
            512: "lime",
            1024: "violet",
            2048: "gold"
        })
        self.assertEqual(grid.score, 0)
    
    def test_move_left(self):
        '''
        tests the move_left method which
        shifts square objects within the grid
        to the left.
        '''
        
        # test - 1: combine squares and shift left 
        grid = Grid(4, [[2, 2, 4, 4], [2, 2, 4, 4], [2, 2, 4, 4], [2, 2, 4, 4]])
        expected_numbers = [[4, 8, 0 , 0], [4, 8, 0 , 0], [4, 8, 0 , 0], [4, 8, 0 , 0]]
        grid.move_left()
        self.assertEqual(grid.numbers[0][0], expected_numbers[0][0])
        self.assertEqual(grid.numbers[0][1], expected_numbers[0][1])
        self.assertEqual(grid.numbers[1][0], expected_numbers[1][0])
        self.assertEqual(grid.numbers[1][1], expected_numbers[1][1])
        self.assertEqual(grid.numbers[2][0], expected_numbers[2][0])
        self.assertEqual(grid.numbers[2][1], expected_numbers[2][1])
        self.assertEqual(grid.numbers[3][0], expected_numbers[3][0])
        self.assertEqual(grid.numbers[3][1], expected_numbers[3][1])

        # test - 2: squares can be shifted to the left but not combined
        grid = Grid(4, [[2, 0, 4, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
        expected_numbers = [[2, 4, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        grid.move_left()
        self.assertEqual(grid.numbers[0][0], expected_numbers[0][0])
        self.assertEqual(grid.numbers[0][1], expected_numbers[0][1])
        
        # test - 3: squares with space in between shifted left and combined
        grid = Grid(4, [[4, 0, 0, 4], [2, 0, 0, 2], [8, 0, 0, 8], [16, 0, 16, 0]])
        expected_numbers = [[8, 0, 0, 0], [4, 0, 0, 0], [16, 0, 0, 0], [32, 0, 0, 0]]
        grid.move_left()
        self.assertEqual(grid.numbers[0][0], expected_numbers[0][0])
        self.assertEqual(grid.numbers[1][0], expected_numbers[1][0])
        self.assertEqual(grid.numbers[2][0], expected_numbers[2][0])
        self.assertEqual(grid.numbers[3][0], expected_numbers[3][0])
        
        # test - 4: all squares are already shifted to the left
        grid = Grid(4, [[2, 4, 8, 16], [2, 4, 8, 0], [2, 4, 0, 0], [2, 0, 0, 0]])
        expected_numbers = [[2, 4, 8, 16], [2, 4, 8, 0], [2, 4, 0, 0], [2, 0, 0, 0]]
        grid.move_left()
        self.assertEqual(grid.numbers[0][0], expected_numbers[0][0])
        self.assertEqual(grid.numbers[0][1], expected_numbers[0][1])
        self.assertEqual(grid.numbers[0][2], expected_numbers[0][2])
        self.assertEqual(grid.numbers[0][3], expected_numbers[0][3])
        self.assertEqual(grid.numbers[1][0], expected_numbers[1][0])
        self.assertEqual(grid.numbers[1][1], expected_numbers[1][1])
        self.assertEqual(grid.numbers[1][2], expected_numbers[1][2])
        self.assertEqual(grid.numbers[2][0], expected_numbers[2][0])
        self.assertEqual(grid.numbers[2][1], expected_numbers[2][1])
        self.assertEqual(grid.numbers[3][0], expected_numbers[3][0])
        
    def test_move_right(self):
        '''
        tests the move_right method which
        shifts square objects within the grid
        to the right.
        '''
        
        # test - 1: combine squares and shift right 
        grid = Grid(4, [[2, 2, 4, 4], [2, 2, 4, 4], [2, 2, 4, 4], [2, 2, 4, 4]])
        expected_numbers = [[0, 0, 4 , 8], [0, 0, 4 , 8], [0, 0, 4 , 8], [0, 0, 4 , 8]]
        grid.move_right()
        self.assertEqual(grid.numbers[0][2], expected_numbers[0][2])
        self.assertEqual(grid.numbers[0][3], expected_numbers[0][3])
        self.assertEqual(grid.numbers[1][2], expected_numbers[1][2])
        self.assertEqual(grid.numbers[1][3], expected_numbers[1][3])
        self.assertEqual(grid.numbers[2][2], expected_numbers[2][2])
        self.assertEqual(grid.numbers[2][3], expected_numbers[2][3])
        self.assertEqual(grid.numbers[3][2], expected_numbers[3][2])
        self.assertEqual(grid.numbers[3][3], expected_numbers[3][3])
        
        # test - 2: squares can be shifted to the right but not combined
        grid = Grid(4, [[2, 0, 4, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
        expected_numbers = [[0, 0, 2, 4], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        grid.move_right()
        self.assertEqual(grid.numbers[0][2], expected_numbers[0][2])
        self.assertEqual(grid.numbers[0][3], expected_numbers[0][3])

        # test - 3: squares with space in between shifted right and combined
        grid = Grid(4, [[4, 0, 0, 4], [2, 0, 0, 2], [8, 0, 0, 8], [16, 0, 16, 0]])
        expected_numbers = [[0, 0, 0, 8], [0, 0, 0, 4], [0, 0, 0, 16], [0, 0, 0, 32]]
        grid.move_right()
        self.assertEqual(grid.numbers[0][3], expected_numbers[0][3])
        self.assertEqual(grid.numbers[1][3], expected_numbers[1][3])
        self.assertEqual(grid.numbers[2][3], expected_numbers[2][3])
        self.assertEqual(grid.numbers[3][3], expected_numbers[3][3])
        
        # test - 4: all squares are already shifted to the right
        grid = Grid(4, [[2, 4, 8, 16], [0, 2, 4, 8], [0, 0, 2, 4], [0, 0, 0, 2]])
        expected_numbers = [[2, 4, 8, 16], [0, 2, 4, 8], [0, 0, 2, 4], [0, 0, 0, 2]]
        grid.move_right()
        self.assertEqual(grid.numbers[0][0], expected_numbers[0][0])
        self.assertEqual(grid.numbers[0][1], expected_numbers[0][1])
        self.assertEqual(grid.numbers[0][2], expected_numbers[0][2])
        self.assertEqual(grid.numbers[0][3], expected_numbers[0][3])
        self.assertEqual(grid.numbers[1][3], expected_numbers[1][3])
        self.assertEqual(grid.numbers[1][1], expected_numbers[1][1])
        self.assertEqual(grid.numbers[1][2], expected_numbers[1][2])
        self.assertEqual(grid.numbers[2][3], expected_numbers[2][3])
        self.assertEqual(grid.numbers[2][2], expected_numbers[2][2])
        self.assertEqual(grid.numbers[3][3], expected_numbers[3][3])
    
    def test_move_up(self):
        '''
        tests the move_up method which
        shifts square objects within the grid
        up.
        '''
        
        # test - 1: combine squares and shift up 
        grid = Grid(4, [[2, 2, 4, 4], [2, 2, 4, 4], [2, 2, 4, 4], [2, 2, 4, 4]])
        expected_numbers = [[0, 0, 0, 0], [0, 0, 0, 0], [4, 4, 8 , 8], [4, 4, 8 , 8]]
        grid.move_up()
        self.assertEqual(grid.numbers[2][0], expected_numbers[2][0])
        self.assertEqual(grid.numbers[2][1], expected_numbers[2][1])
        self.assertEqual(grid.numbers[2][2], expected_numbers[2][2])
        self.assertEqual(grid.numbers[2][3], expected_numbers[2][3])
        self.assertEqual(grid.numbers[3][0], expected_numbers[3][0])
        self.assertEqual(grid.numbers[3][1], expected_numbers[3][1])
        self.assertEqual(grid.numbers[3][2], expected_numbers[3][2])
        self.assertEqual(grid.numbers[3][3], expected_numbers[3][3])
        
        # test - 2: squares can be shifted up but not combined
        grid = Grid(4, [[2, 0, 4, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
        expected_numbers = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [2, 0, 4, 0]]
        grid.move_up()
        self.assertEqual(grid.numbers[3][0], expected_numbers[3][0])
        self.assertEqual(grid.numbers[3][2], expected_numbers[3][2])
        
        # test - 3: squares with space in between shifted up and combined
        grid = Grid(4, [[4, 0, 0, 4], [0, 0, 0, 0], [0, 0, 0, 0], [4, 0, 0, 4]])
        expected_numbers = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [8, 0, 0, 8]]
        grid.move_up()
        self.assertEqual(grid.numbers[3][0], expected_numbers[3][0])
        self.assertEqual(grid.numbers[3][3], expected_numbers[3][3])
        
        # test - 4: all squares are already shifted up
        grid = Grid(4, [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [2, 4, 8, 16]])
        expected_numbers = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [2, 4, 8, 16]]
        grid.move_up()
        self.assertEqual(grid.numbers[3][0], expected_numbers[3][0])
        self.assertEqual(grid.numbers[3][1], expected_numbers[3][1])
        self.assertEqual(grid.numbers[3][2], expected_numbers[3][2])
        self.assertEqual(grid.numbers[3][3], expected_numbers[3][3])
        
    def test_move_down(self):
        '''
        tests the move_down method which
        shifts square objects within the grid
        down.
        '''
        
        # test - 1: combine squares and shift up 
        grid = Grid(4, [[2, 2, 4, 4], [2, 2, 4, 4], [2, 2, 4, 4], [2, 2, 4, 4]])
        expected_numbers = [[4, 4, 8 , 8], [4, 4, 8 , 8], [0, 0, 0, 0], [0, 0, 0, 0]]
        grid.move_down()
        self.assertEqual(grid.numbers[0][0], expected_numbers[0][0])
        self.assertEqual(grid.numbers[0][1], expected_numbers[0][1])
        self.assertEqual(grid.numbers[0][2], expected_numbers[0][2])
        self.assertEqual(grid.numbers[0][3], expected_numbers[0][3])
        self.assertEqual(grid.numbers[1][0], expected_numbers[1][0])
        self.assertEqual(grid.numbers[1][1], expected_numbers[1][1])
        self.assertEqual(grid.numbers[1][2], expected_numbers[1][2])
        self.assertEqual(grid.numbers[1][3], expected_numbers[1][3])
        
        # test - 2: squares can be shifted down but not combined
        grid = Grid(4, [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [2, 0, 4, 0]])
        expected_numbers = [[2, 0, 4, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        grid.move_down()
        self.assertEqual(grid.numbers[0][0], expected_numbers[0][0])
        self.assertEqual(grid.numbers[0][2], expected_numbers[0][2])
        
        # test - 3: squares with space in between shifted down and combined
        grid = Grid(4, [[4, 0, 0, 4], [0, 0, 0, 0], [0, 0, 0, 0], [4, 0, 0, 4]])
        expected_numbers = [[8, 0, 0, 8], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        grid.move_down()
        self.assertEqual(grid.numbers[0][0], expected_numbers[0][0])
        self.assertEqual(grid.numbers[0][3], expected_numbers[0][3])
        
        # test - 4: all squares are already shifted down
        grid = Grid(4, [[2, 4, 8, 16], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
        expected_numbers = [[2, 4, 8, 16], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        grid.move_down()
        self.assertEqual(grid.numbers[0][0], expected_numbers[0][0])
        self.assertEqual(grid.numbers[0][1], expected_numbers[0][1])
        self.assertEqual(grid.numbers[0][2], expected_numbers[0][2])
        self.assertEqual(grid.numbers[0][3], expected_numbers[0][3])
        

    def test_combine_squares(self):
        '''
        tests the combine_squares method which
        merges touching squares of the same number
        in the grid.
        '''
        
        # test 1 - all squares are different
        grid = Grid(4, [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
        squares = [2, 4, 8, 16]
        combined_squares = grid.combine_squares(squares)
        self.assertEqual(combined_squares, [2, 4, 8, 16])
        
        # test 2 - two touching squares have the same number
        grid = Grid(4, [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
        squares = [2, 4, 4, 8]
        combined_squares = grid.combine_squares(squares)
        self.assertEqual(combined_squares, [2, 8, 8, 0])
        
        # test 3 - case two not touching squares are the same
        grid = Grid(4, [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
        squares = [2, 8, 4, 8]
        combined_squares = grid.combine_squares(squares)
        self.assertEqual(combined_squares, [2, 8, 4, 8])
    
    def test_shift_squares(self):
        '''
        tests the shift_squares method which
        shifts the squares in a list of sqs to the left
        and fills the remaining spaces with 0's
        '''
        
        # test 1 - squares do not need to shift
        grid = Grid(4, [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
        squares = [2, 4, 8, 16]
        shifted_squares = grid.shift_squares(squares)
        self.assertEqual(shifted_squares, [2, 4, 8, 16])

        # test 2 - squares need to shift
        grid = Grid(4, [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
        squares = [2, 0, 8, 0]
        shifted_squares = grid.shift_squares(squares)
        self.assertEqual(shifted_squares, [2, 8, 0, 0])
    
    def test_add_number(self):
        '''
        tests the add_number method which
        randomly adds a 2 or 4 to the grid after each move.
        '''
        # test 1 - a number is added to the grid
        grid = Grid(4, [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
        grid.add_number()
        self.assertNotEqual(grid.numbers, [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
        
if __name__ == '__main__':
    unittest.main()
