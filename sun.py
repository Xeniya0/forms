import turtle
import random

window = turtle.Screen()
arthur = turtle.Turtle()
window.colormode(255)
arthur.speed(20)
arthur.width(2)
arthur.pensize(1)
window.bgcolor(135, 206, 250)
arthur.pencolor(219, 112, 147)
def shape(angle, side, limit):
    reverseDirection = 200
    # 1000
    arthur.forward(side)
    if side % (reverseDirection * 2) == 0:
        angle = angle + 2
        # + 50
        print(side)

    elif side % reverseDirection == 0:
        angle = angle - 2
        # - 30
        print(side)
    arthur.right(angle)
    side = side + 2
    if side < limit:
         shape(angle, side, limit)

angle = 119
side = 0
limit = 600
shape(angle, side, limit)
turtle.done()
