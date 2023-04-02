import turtle
import random
elsa = turtle.Turtle()
turtle.Screen().bgcolor('black')
colours = ['purple', 'lightpink', 'lightblue', 'lightyellow']
elsa.color('purple')
for i in range(10):
    for i in range(2):
        elsa.forward(100)
        elsa.right(60)
        elsa.forward(100)
        elsa.right(120)
    elsa.right(36)
    elsa.color(random.choice(colours))
