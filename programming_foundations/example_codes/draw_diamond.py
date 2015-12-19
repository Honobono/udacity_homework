#mini_project: draw shapes

import turtle

def draw_diamond(n, side_length):
    for i in range(n):
        turtle.left(360/n)
        for j in range(n):
            turtle.forward(side_length)
            turtle.left(360/n)
    window.exitonclick()

draw_diamond(12, 30)
