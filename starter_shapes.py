#!/usr/bin/python

"""
Starter code for the Python shapes assignment.

(1) Draw a square
(2) Draw a triangle
(3) Draw a colorful Triangle/Square
(4) Use sys.argv[] to get user input from command line
* remember to import sys
* and sys.argv[0] is the program name. User inputs start at index 1.
(5) Draw a polygon, add color?
(6) Draw fun designs. Look up on google for ideas.
(7) Once finished. Check out solution code. There are some cool shapes to 
play with and see. Tweek them for fun!

"""

import turtle

"""Name your turtle!! 

tiffany = turtle.Turtle()

This means instead of calling turtle.forward() you use tiffany.forward() 
instead. Yay!
"""

def square(side_length):
    ## YOUR CODE GOES HERE

    return


def equilateral_triangle(side_length):
    ## YOUR CODE GOES HERE
    
    return

def polygon(side_length,num_sides):

    ## YOUR CODE GOES HERE

    return


def main():

    turtle.setup(800,600)
    window = turtle.Screen()

    """Function calls"""
    #square(side_length)
    #equilateral_triangle(side_length)
    #polygon(side_length,num_sides)

    window.exitonclick() ## What is this? Try removing it and see what happens
    return

"""The call to main"""

if __name__ == "__main__":
    main()
    
