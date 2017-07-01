#!/usr/bin/python

"""
This is a small program to draw shapes in python using the turtle module.
author: Denise Kilburg for Girls Who Code
"""

import turtle
from random import randint
import sys

"""
Below are a few basic functions for drawing the shapes.
As you go further down the line, the functions get more complex. Adding colors
and more sophisticated shapes.
"""

def square(side_length):
    """
    Draws a square : Suggested side_length > 100
    You do not need to use a for loop. You can write the .forward and .right
    commands 4 times if you wanted.
    """
    # Using a for loop
    for i in range(4):
        turtle.forward(side_length)
        turtle.right(90)

    # Using a while loop
    """
    i = 4
    while i > 0:
        turtle.forward(side_length)
        turtle.right(90)
        i -= 1
    """
    return


def equilateral_triangle(side_length):
   #Draws an equilateral Triangle : Suggested side_length > 100
    for i in range(3):
        turtle.forward(side_length)
        turtle.left(120) # External angle must be used (180 - 60)

    return


def square_with_color(side_length,color, fillIt=False):
    turtle.color(t_color) ## Makes the shape the selected color
    turtle.fill(fillIt) ## Will fill in shape with color if fillit==True
    for i in range(4):
        turtle.forward(side_length)
        turtle.left(90)

    turtle.fill(fillIt)

    return


def polygon(side_length,num_sides,t_color):
    turtle.color(t_color)
    angle = 360/float(num_sides)
    for i in range(num_sides):
        turtle.forward(side_length)
        turtle.left(angle)

    return


def cool_spiral():
    """
    Run the Spiral and see what the output is. What would you do to make
    a tighter spiral? What about the colors? Can you make a rainbow spiral
    starting from red in the middle to violet on the perimeter? 
    """
    turtle.bgcolor('black') # set background color
    turtle.speed(0) # Fastest speed available: range 0-10
    x = 1
    while x < 400:
        r = randint(0,255) #Initalize random rgb values
        g = randint(0,255)
        b = randint(0,255)
        turtle.colormode(255)
        turtle.pencolor(r,g,b) #a different way to set up colors
        turtle.fd(50 + x) # Forward
        turtle.right(90.911)
        x+=1

def triForce(large_length):
    turtle.bgcolor('black')
    turtle.speed(0)
    gold = (212,175,55)
    turtle.colormode(255)

    x = 0.0 - large_length/2.0 #set triangle in middle of screen
    y = x
    
    # First Triangle
    turtle.color(gold)
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    turtle.fill(True)
    for i in range(3):
        turtle.forward(large_length)
        turtle.left(120)
    turtle.fill(True)   
    #2nd Triangle 
    """Can you fix this to use a loop? Hint: start position must be changed"""
    turtle.up()
    turtle.color('black')
    turtle.goto(0.0,-large_length/2.0)
    turtle.down()
    turtle.fill(True)
    turtle.left(60)
    turtle.forward(large_length/2.0)
    turtle.left(120)
    turtle.forward(large_length/2.0)
    turtle.left(120)
    turtle.forward(large_length/2.0)
    turtle.fill(True)
    turtle.hideturtle()

    return



def main():
    """ Use code below if using command line user input:

    side_length = sys.argv[1]
    num_sides = sys.argv[2]
    color = sys.argv[3]
    """    
    color = 'black' # default turtle color (remove if using user input for co
    turtle.setup(800,600)
    window = turtle.Screen()

    """Draw Shape function calls"""
    
    #square_with_color(100,color,fillIt=True)
    #polygon(50,20,color)
    #cool_spiral()
    triForce(200)
    window.exitonclick() 

    
    


if __name__ == "__main__":
    main()
