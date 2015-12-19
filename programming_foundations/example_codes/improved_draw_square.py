
import turtle

def draw_square(some_turtle):
    # draw a square using forward, and right 4 times:
    for i in range(1,5): 
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("green")

    #Create the turtle Brad
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)
    # draw multiple squares to create the intended circular shape built from squares, 36 squares
    for i in range(1,37):
        draw_square(brad)
        brad.right(10)
    window.exitonclick()

draw_art()
