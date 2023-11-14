"""Turtle Tutorial"""

from turtle import Turtle
from turtle import done
from turtle import colormode
leo: Turtle = Turtle()


colormode(255)

leo.speed(50)
leo.hideturtle()

leo.penup()
leo.goto(-200,-200)
leo.pendown()

leo.color(99, 204, 250)

leo.pencolor("pink") 
leo.fillcolor(32, 67, 93) 
leo.color("green", "yellow")

i: int = 0

leo.begin_fill()

while (i < 3):
    
    leo.forward(500) 
    leo.left(120)
    i += 1

leo.end_fill()



bob: Turtle = Turtle()

bob.pencolor(0,0,0)
bob.penup()
bob.goto(-200,-200)
bob.pendown()
bob.speed(25)


j: int = 0
side_length: int = 500
side_angle: int = 121
while (j < 100):
    bob.forward(side_length) 
    bob.left(side_angle)
    side_length = side_length * 0.95
    j += 1


done()

