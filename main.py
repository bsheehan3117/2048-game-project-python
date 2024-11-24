from Grid import Grid
from Square import Square
import turtle
import random

'''
    Brendan Sheehan
    CS5001
    Project 2048
    
    This program is the main function for the 2048 game.
'''
def main():

    '''
    This program runs the 2048 game using the imported files.

    -It initializes the game with 16 randomly
    filled spaces 0's and two 2's..
    -It instructs the user how to play the game
    in the turtle window.
    -It creates a Grid object with the initialized grid.
    -It sets up the turtle screen and assigns keys for
    moving numbers, ending the game, and restarting the game
    -It listens for user key entry
    '''
    # initialize game grid
    # pop list to fill all 16 locations in the grid
    # randomly with empty spaces and two 2's
    size = 4
    numbers = [[0] * size for i in range(size)]
    random_numbers = [2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    random.shuffle(random_numbers)
    numbers[0][0] = random_numbers.pop()
    numbers[0][1] = random_numbers.pop()
    numbers[0][2] = random_numbers.pop()
    numbers[0][3] = random_numbers.pop()
    numbers[1][0] = random_numbers.pop()
    numbers[1][1] = random_numbers.pop()
    numbers[1][2] = random_numbers.pop()
    numbers[1][3] = random_numbers.pop()
    numbers[2][0] = random_numbers.pop()
    numbers[2][1] = random_numbers.pop()
    numbers[2][2] = random_numbers.pop()
    numbers[2][3] = random_numbers.pop()
    numbers[3][0] = random_numbers.pop()
    numbers[3][1] = random_numbers.pop()
    numbers[3][2] = random_numbers.pop()
    numbers[3][3] = random_numbers.pop()

    # create border for game grid
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.penup()
    t.goto(-160,-160)
    t.pendown()
    
    for i in range(4):
        t.forward(250)
        t.left(90)

    # provide instructions on screen
    t.penup()
    t.goto(-275, -90)
    t.pendown()
    t.write("Use the arrow keys\nto move the numbers\non the board.\n\nUp - move numbers up\nDown - move numbers down\nLeft - move numbers left\nRight - move numbers right", align="center", font=("Arial", 12, "normal"))
        
    # creating the grid object
    game = Grid(size, numbers)

    # set up turtle screen
    window = turtle.Screen()
    window.bgcolor("white")
    window.title("2048")

    # assign arrow keys to move methods,
    # new game method and end game method
    window.onkey(game.move_left, "Left")
    window.onkey(game.move_right, "Right")
    window.onkey(game.move_up, "Up")
    window.onkey(game.move_down, "Down")
    window.onkey(game.new_game, "n")
    window.onkey(game.end_game, "x")

    # listen for key presses by user
    window.listen()
    window.mainloop()
    turtle.done()
    
if __name__ == '__main__':
    main()
