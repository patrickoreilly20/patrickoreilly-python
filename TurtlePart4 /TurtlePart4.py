from turtle import Turtle, Screen
from itertools import cycle

COLOR_NAMES = ['red', 'magenta', 'blue', 'cyan', 'green', 'yellow']

colors = cycle(COLOR_NAMES)

yertle = Turtle()
yertle.speed("fastest")

for _ in range(36):
    yertle.color(next(colors))
    yertle.circle(50)
    yertle.left(10)

yertle.hideturtle()

screen = Screen()
screen.exitonclick()

Turtle.pen('green', 'blue')
Turtle.begin_fill()
Turtle.hideturtle()
while True:
    Turtle.forward(200)
    Turtle.left(170)
    if abs(Turtle.pos()) < 1:
        break
Turtle.end_fill()
Turtle.done()
Turtle.exitonclick()


COLOR_NAMES = ['red', 'magenta', 'blue', 'cyan', 'green', 'yellow']

colors = cycle(COLOR_NAMES)

yertle = Turtle()
yertle.speed("fastest")

for _ in range(36):
    yertle.color(next(colors))
    yertle.circle(50)
    yertle.left(10)

yertle.hideturtle()

screen = Screen()
screen.exitonclick()

Turtle.pen('green', 'blue')
Turtle.begin_fill()
Turtle.hideturtle()
while True:
    Turtle.forward(200)
    Turtle.left(170)
    if abs(Turtle.pos()) < 1:
        break
Turtle.end_fill()
Turtle.done()
Turtle.exitonclick()
