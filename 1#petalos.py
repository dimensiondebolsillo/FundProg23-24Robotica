import turtle
import random

def halfPetal(sz, ang):
    jem.circle(sz,ang)
    jem.circle(sz,ang)

def Petal(sz, ang):
    halfPetal(sz, ang)
    jem.left(40)
    halfPetal(sz, ang)

wn = turtle.Screen()
jem = turtle.Turtle()

jem.color("yellow")
fill_color = "yellow"
jem.pensize(2)

t = int(input("Number of petals?" ))

for _ in range(t):
    jem.penup()
    jem.goto(int(random.randrange(-300,300)), int(random.randrange(-300,300)))
    jem.begin_fill()
    jem.pendown()
    Petal(100,70)
    jem.end_fill()
    jem.penup()

wn.exitonclick()
