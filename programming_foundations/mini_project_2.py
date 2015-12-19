# Mini project: draw flower shapes

import turtle
window = turtle.Screen()
sarah = turtle.Turtle()
sarah.speed(10)
sarah.color("blue")

for parallelogram in range(60): #repeat 10 times
    
    sarah.forward(100)
    sarah.left(60)
    sarah.forward(100)
    sarah.left(120)
    sarah.forward(100)
    sarah.left(60)
    sarah.forward(100)

    sarah.left(6)          # turn left 10 degrees

#draw stem
sarah.left(90) 
sarah.backward(250)

window.exitonclick()
