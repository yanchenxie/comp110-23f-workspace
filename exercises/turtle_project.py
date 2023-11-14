"""Turtle Project where I am going to draw a face looking at the starry night sky."""

from turtle import Turtle, colormode, done
from random import randint
colormode(255) 

__author__ = "730233103"


def main() -> None:
    """The entrypoint of my scene."""
    ttl: Turtle = Turtle()
    random_stars(20)
    draw_square(ttl, 0, 20, 20)
    draw_square(ttl, 40, 20, 20)
    draw_pentagon(ttl, 20, -40, 20)
    draw_circle(ttl, 30, 40, 1)
    draw_triangle(ttl, 20, -10, 20)
    done()


def draw_square(a_turtle: Turtle, x: float, y: float, width: int) -> None:
    """Draw a square of given width starting with given coordinates."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    i: int = 0 
    while i < 4: 
        a_turtle.forward(width)
        a_turtle.right(90)
        i += 1


def draw_triangle(a_turtle: Turtle, x: float, y: float, width: int) -> None:
    """Draw a triangle of given width starting with given coordinates."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    a_turtle.pencolor(0, 0, 255)
    a_turtle.fillcolor(255, 0, 0)
    a_turtle.begin_fill()
    i: int = 0 
    while i < 3: 
        a_turtle.forward(width)
        a_turtle.right(120)
        i += 1
    a_turtle.end_fill()


def draw_pentagon(a_turtle: Turtle, x: float, y: float, width: int) -> None:
    """Draw a pentagon of given width starting with given coordinates."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    i: int = 0 
    while i < 5: 
        a_turtle.forward(width)
        a_turtle.right(365 / 5)
        i += 1


def draw_circle(a_turtle: Turtle, x: float, y: float, length: int) -> None:
    """Draw a circle of given length starting with given coordinates."""
    a_turtle.speed(200)
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    i: int = 0 
    while i < 360: 
        a_turtle.forward(length)
        a_turtle.right(1)
        i += 1


def draw_star(a_turtle: Turtle, x: float, y: float, length: int, edge: int) -> None:
    """Draw a star shape with given edges using the given starting location and legnth."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    a_turtle.speed(200)
    i: int = 0
    while i < edge:
        a_turtle.hideturtle()
        a_turtle.forward(length)
        a_turtle.goto(x, y)
        a_turtle.right(360 / edge)
        i += 1


def random_stars(num_stars: int) -> None:
    """Draw multiple stars in random locations above the face shapes."""
    i: int = 0
    while i < num_stars:
        x: int = randint(-300, 300)
        y: int = randint(100, 300)
        draw_star(Turtle(), x, y, 10, 5)
        i += 1


if __name__ == "__main__":
    main()