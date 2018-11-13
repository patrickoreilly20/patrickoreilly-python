#from turtle import *
#color('red', 'yellow')
#begin_fill()
#while True:
#    forward(200)
#    left(170)
#    if abs(pos()) < 1:
#        break
#end_fill()
#done()

import turtle

turtle.bgcolor('black')

def line():

    turtle.penup()

    turtle.goto(-50,0)

    turtle.pendown()

    turtle.color('orange')

    turtle.forward(100)

line()

def square():

    turtle.color('red')

    turtle.penup()

    turtle.goto(-100,-100)

    turtle.pendown()

    turtle.forward(200)

    turtle.left(90)

    turtle.forward(200)

    turtle.left(90)

    turtle.forward(200)

    turtle.left(90)

    turtle.forward(200)

    turtle.left(90)

square()
def circle():

    turtle.color('blue')

    turtle.penup()

    turtle.goto(0,-300)

    turtle.pendown()

    turtle.circle(300)

circle()

def triangle():

    turtle.color('white')

    turtle.penup()

    turtle.goto(-200,-150)

    turtle.pendown()

    turtle.forward(400)

    turtle.left(120)

    turtle.forward(400)

    turtle.left(120)

    turtle.forward(400)

    turtle.left(120)

    turtle.exitonclick()

triangle()
