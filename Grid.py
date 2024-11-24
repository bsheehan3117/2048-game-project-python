import random
import turtle
from Square import Square

'''
    Brendan Sheehan
    CS5001
    Project 2048
    
    This program creates a Grid class with the following parameters:
    x coordinate, y coordinate, size, number, color.
'''

class Grid:

    '''
    class Grid: defines the game grid
    Attributes:
    size (int) -- size of grid
    numbers(lst) -- grid in list form
    squares (lst) -- list of Squares
    colors(dict) -- dictionary of keys (num) and
        values (colors)
    score int) -- score of game
    
    Methods: create_squares, move_left,
    move_right, move_down, move_up,
    combine_squares, shift_squares, add_number,
    new_game, end_game
    '''
    
    def __init__(self, size, numbers):
        '''Constructor -- creates new instances of grid
        Parameters:
            self -- the current object
            size -- the size of the game grid
            numbers -- a list representing the grid
        '''
        
        # provide values to grid parameters, create an
        # empty list of squares
        self.size = size
        self.numbers = numbers
        self.squares = []
        
        # use a dictionary to assign each number found
        # in the game to a color
        self.colors = {
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
        }
        
        # use create_squares to build the grid using square objects
        self.create_squares()

        # create a scoreboard using turtle write
        self.score = 0
        self.score_pen = turtle.Turtle()
        self.score_pen.hideturtle()
        self.score_pen.speed(0)
        self.score_pen.penup()
        self.score_pen.goto(0, 200)
        self.score_pen.write("Score: {}".format(self.score), align="center", font=("Arial", 24, "normal"))

        # create a message on the turtle
        # screen that tells the user how to
        # start a new game or end the game
        self.new_game_pen = turtle.Turtle()
        self.new_game_pen.hideturtle()
        self.new_game_pen.speed(0)
        self.new_game_pen.penup()
        self.new_game_pen.goto(0, -200)
        self.new_game_pen.write("Press the n key at anytime to start a new game", align="center", font=("Arial", 16, "normal"))
        self.new_game_pen.penup()
        self.new_game_pen.goto(0, -240)
        self.new_game_pen.write("Press the x key at anytime to end the game", align="center", font=("Arial", 16, "normal"))
        
    def create_squares(self):
        '''
        loops thru the grid to create a list of Square objects.  
        
        Returns: nothing
        '''
        # loop through rows and columns of grid
        for i in range(self.size):

            for j in range(self.size):

                # determine x and y coords of square
                # leaving 10 in between each 
                x = j * 60 - 150
                y = i * 60 - 150

                # determine number of current square
                number = self.numbers[i][j]

                # determine color of square based on its number
                color = self.colors[number]

                # make new Square object using parameters
                # determined above
                square = Square(x, y, 50, number, color)

                # add Square to squares list
                self.squares.append(square)

        # after creating new squares check if any
        # squares are 2048, display You win if so
        if any(square.number == 2048 for square in self.squares):
            self.score_pen.clear()
            self.score_pen.goto(0, 200)
            self.score_pen.write("YOU WIN!", align="center", font=("Arial", 50, "normal"))
            turtle.done()

    def move_left(self):
        '''
        moves all squares in the grid to the leftmost
        location and merges Squares of the same
        number that contact eachother in that direction.
        
        Returns: nothing
        '''
        # loop through rows
        for i in range(self.size):

            # determine current row
            row = self.numbers[i]

            # combine touching squares of the same number 
            row = self.combine_squares(row)

            # shift squares left
            row = self.shift_squares(row)

            # update grid
            self.numbers[i] = row

        # add a 2 or 4 to an empty location in the grid
        self.add_number()
            
        # create new grid with updated squares
        self.create_squares()

    def move_right(self):
        '''
        moves all squares in the grid to the rightmost
        location and merges Squares of the same
        number that contact eachother in that direction.
        
        Returns: nothing
        '''
        # loop through rows
        for i in range(self.size):

            # reverse row towards right
            row = self.numbers[i][::-1]

            # combine touching squares of the same number
            row = self.combine_squares(row)

            # shift squares right
            row = self.shift_squares(row)

            # reverse row back to original
            row = row[::-1]

            # update row in grid
            self.numbers[i] = row

        # add a 2 or 4 to an empty location in the grid
        self.add_number()
            
        # create new grid with updated squares
        self.create_squares()

    def move_down(self):
        '''
        moves all squares in the grid to the bottom most
        location and merges Squares of the same
        number that contact eachother in that direction.
        
        Returns: nothing
        '''
        # loop through rows for columns
        for i in range(self.size):

            # get column
            col = [row[i] for row in self.numbers]

            # combine touching squares of same number in column
            col = self.combine_squares(col)

            # shift squares down
            col = self.shift_squares(col)

            # update column in grid
            for j in range(self.size):
                self.numbers[j][i] = col[j]

        # add a 2 or 4 to an empty location in the grid
        self.add_number()
                
        # create new grid with updated squares
        self.create_squares()

    def move_up(self):
        '''
        moves all squares in the grid to the top most
        location and merges Squares of the same
        number that contact eachother in that direction.
        
        Returns: nothing
        '''
        
        # loop thru rows for columns
        for i in range(self.size):

            # get column and reverse it to go up
            col = [row[i] for row in self.numbers][::-1]

            # combine touching squares of the same number
            col = self.combine_squares(col)

            # shift squares up
            col = self.shift_squares(col)

            # reverse column back to original
            col = col[::-1]

            # update the column in the grid
            for j in range(self.size):
                self.numbers[j][i] = col[j]

        # add a 2 or 4 to an empty location in the grid
        self.add_number()
                
        # create new grid with updated squares
        self.create_squares()

    def combine_squares(self, squares):
        '''
        Method to merge touching
        squares of the same number
        in the grid.

        Returns: a list of squares
        '''
        # remove all zeros from the list
        squares = [square for square in squares if square != 0]

        # loop thru list of squars
        for i in range(len(squares) - 1):

            # if touching squares have same value
            if squares[i] == squares[i+1]:

                # multiply initial sq by 2
                squares[i] *= 2

                # add to score
                self.score += squares[i]

                # other square = 0
                squares[i+1] = 0

        # remove all zeros from the list again
        squares = [square for square in squares if square != 0]

        # add zeros to the end of the list 
        while len(squares) < self.size:
            squares.append(0)

        return squares


    def shift_squares(self, squares):
        '''
        Method to shift squares in a list of squares
        to the left and fills empty spaces with 0's.

        Parameters:
        Self
        A list of squares
        Returns: list of shifted squares.
        '''
        # create an empty list for shifted squares
        shifted_squares = []

        # loop through list of squares
        for square in squares:

            # if square num is not 0, add to shifted squares list
            if square != 0:
                shifted_squares.append(square)

        # fill empty squares with 0's while the length of the list
        # is less than the number of squares in the grid
        while len(shifted_squares) < self.size:
            shifted_squares.append(0)

        # return list of shifted squares
        return shifted_squares

    def add_number(self):
        '''
        Method to add a 2 or 4 to the grid
        after squares are moved.  If there is no room to
        add a number, display Game over msg.

        Returns: nothing
        '''
        # create an empty list for the empty squares
        empty_squares = []
        
        # loop thru grid to find squares with 0's
        for i in range(self.size):
            for j in range(self.size):
                if self.numbers[i][j] == 0:
                    
                    # add the empty squares to the list
                    empty_squares.append((i, j))
                    
        # if there are squares in the empty squares list,
        # randomly choose one and make it a 2 or 4
        if empty_squares:
            i, j = random.choice(empty_squares)
            self.numbers[i][j] = random.choice([2, 4])

            # add to score and update scoreboard
            self.score += self.numbers[i][j]
            self.score_pen.clear()
            self.score_pen.write("Score: {}".format(self.score), align="center", font=("Arial", 24, "normal"))

        else:

            # assign boolean to game over
            game_over = True

            # check if there are any ways to combine squares
            for i in range(self.size):
                for j in range(self.size):
                    if (j != self.size - 1 and self.numbers[i][j] == self.numbers[i][j+1]) or \
                    (i != self.size - 1 and self.numbers[i][j] == self.numbers[i+1][j]):
                        game_over = False
                        break

            # end the game if there are no empty squares
            # or ways to combine numbers
            if game_over:
                self.score_pen.clear()
                self.score_pen.goto(0, 0)
                self.score_pen.write("GAME OVER", align="center", font=("Arial", 50, "normal"))
                turtle.done()        

    def new_game(self):
        '''
        Method to start a new game at anytime.

        Returns: nothing.
        '''
        
        for square in self.squares:
            square.pen.clear()
        self.squares = []

        # reset score
        self.score = 0
        self.score_pen.clear()
        self.score_pen.write("Score: {}".format(self.score), align="center", font=("Arial", 24, "normal"))

        # pop list to fill all 16 locations in the grid
        # randomly with empty spaces and two 2's
        self.numbers = [[0] * self.size for i in range(self.size)]
        random_numbers = [2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        random.shuffle(random_numbers)
        self.numbers[0][0] = random_numbers.pop()
        self.numbers[0][1] = random_numbers.pop()
        self.numbers[0][2] = random_numbers.pop()
        self.numbers[0][3] = random_numbers.pop()
        self.numbers[1][0] = random_numbers.pop()
        self.numbers[1][1] = random_numbers.pop()
        self.numbers[1][2] = random_numbers.pop()
        self.numbers[1][3] = random_numbers.pop()
        self.numbers[2][0] = random_numbers.pop()
        self.numbers[2][1] = random_numbers.pop()
        self.numbers[2][2] = random_numbers.pop()
        self.numbers[2][3] = random_numbers.pop()
        self.numbers[3][0] = random_numbers.pop()
        self.numbers[3][1] = random_numbers.pop()
        self.numbers[3][2] = random_numbers.pop()
        self.numbers[3][3] = random_numbers.pop()

        # create new list of Squares
        self.create_squares()

    def end_game(self):
        '''
        Method to end the game at anytime.
        Displays "GAME OVER" msg on screen
        and ends turtle
        Returns: Nothing
        '''
        self.score_pen.clear()
        self.score_pen.goto(0, 0)
        self.score_pen.write("GAME OVER", align="center", font=("Arial", 50, "normal"))
        turtle.done() 
