import turtle
import random

'''
    Brendan Sheehan
    CS5001
    Project 2048
    
    This program creates a Square class with the
    following attributes:
    x coordinate, y coordinate, size, number, color.
'''

class Square:
    '''
    Class Square: represents each square in the game.
    Attributes: x coordinate, y coordinate, size, number, color.
    Methods: draw, draw_number
    '''
    
    def __init__(self, x, y, size, number, color):
        '''
        Constructor -- creates new instances of squares
        Parameters:
            self -- the current object
            x -- the x coordinate of the bottom left corner
            y -- the y coordinate ot the bottom left corner
            size -- the length of a squares edge
            number -- the number on the square 
            color -- the color of the square
        '''
        # provide values to Square parameters
        self.x = x
        self.y = y
        self.size = size
        self.number = number
        self.color = color
        
        # create a turtle pen
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.hideturtle()
        
        # use draw and draw number methods
        # to create a square object
        self.draw()
        self.draw_number()

    def draw(self):
        '''
        method using turtle to draw a square object based on
        the x coordinate, y coordinate, size, and color.
        Returns: nothing
        '''
        # move pen to x,y location and assign sq. color
        self.pen.hideturtle()
        self.pen.up()
        self.pen.goto(self.x, self.y)
        self.pen.down()
        self.pen.fillcolor(self.color)
        self.pen.begin_fill()

        # draw 4 edges
        for _ in range(4):
            self.pen.forward(self.size)
            self.pen.left(90)
        self.pen.end_fill()

    def draw_number(self):
        '''
        method to draw a number inside the square object
        using turtle
        Returns: nothing
        '''

        # determine the center of the square for number
        # location, subtract a further 15 from so that center
        # of num is in center of sq
        self.pen.hideturtle()
        self.pen.up()
        x = self.x + self.size / 2
        y = self.y + self.size / 2 - 15

        # draw number at x,y coordinate
        self.pen.goto(x, y)
        self.pen.down()
        self.pen.color("white")
        if self.number != 0:
            self.pen.write(self.number, align="center", font=("Arial", 20, "bold"))
        else:
            self.pen.write("", align="center", font=("Arial", 20, "bold"))
