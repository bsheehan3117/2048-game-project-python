Brendan Sheehan
CS5001
Project 2048

DESIGN

main.py:

Contains the main function to run the program.  

The main function takes imports from the Grid.py file, Square.py file, turtle, and random.

The main function runs the 2048 game using these imported files to create a game grid object containing 16 square objects. It provides instructions in the user window for how to play the game, start a new game, and end the game.  It operates by setting up the turtle screeen, assigning keys for user input, and listening for user key entry.  

Square.py:

Creates a Square class and
Methods for creating Square objects.  Each square represents a square on the game Grid and has a specific x coordinate, y coordinate, size, number, and color.  

Methods in this file:

__init__: square constructor
draw: uses turtle to draw a square
draw_number: uses turtle to draw a number inside a square object.

Grid.py:

Creates a Grid class and methods for creating and changing Grid objects.  Grid consists of 16 Square objects.
  
Methods in this file:

__init__: Grid constructor, builds grid based on size (length of grid in sqs) and numbers. assigns number/color key value pairs.  Provides messages on screen for ending and starting new game.

create_squares: creates list of square objects from squares within grid.  If a new 2048 square is created, writes You win message.

move_left: moves squares in grid to leftmost open location, merging like squares in contact.

move_right: moves squares in grid to rightmost open location, merging like squares in contact.

move_up: moves squares in grid to topmost open location, merging like squares in contact.

move_down: moves squares in grid to bottommost open location, merging like squares in contact.

combine_squares: merges touching squares of same number within grid.  used with move methods.

shift_squares: shifts squares in the list of squares to the left and fills empty spaces with 0's.  Used with move methods.

add_number:  adds a 2 or 4 to an empty square in the grid after each successful move.  Ends game if there are no empty squares and no possible moves.

new_game:  allows user to start a new game at anytime.  Works in main function with key assigned to n

end_game:  allows the user to end a game at any time.  Works in main function with key assigned to x.


INSTRUCTIONS:

Run main.py file.

Use arrow keys to move squares within the grid.  The goal is to combine like squares within the grid until the number 2048 appears in a square.  Squares may be combined if they are adjacent to one another and are of the same number.  Combined squares will merge into a square that is the sum of the two merged squares. 

Keys to use:

"Up" - moves squares in the grid up
"Down" - moves squares in the grid down
"Left" - moves squares in the grid left
"Right" - moves squares in the grid right
"x" - ends the game at any time
"n" - clears the board and resets the score to start a new game at any time


FEATURES:

- Colors change with numbers
- Arrow keys used for moving squares
- Board and numbers clearly visible
- Instructions for game play displayed in game window.
- Instructions for ending game displayed in game window.
- Instructions for starting a new game displayed in game window.
- Keys other than those indicated do nothing.
- Score board displayed on game screen
- 2 or 4 is added to the board after each successful move
- Game ends if no possible moves
-You win message is displayed if 2048 appears on board
- Like squares merge any time the correct key is pushed and there are not different squares between them.
