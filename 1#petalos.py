import turtle
import random

def halfPetal(t, sz, ang):
    t.circle(sz,ang)
    t.circle(sz,ang)

def Petal(t, sz, ang):
    halfPetal(t, sz, ang)
    t.left(40)
    halfPetal(t, sz, ang)

def main():
    wn = turtle.Screen()
    jem = turtle.Turtle()

    jem.color("yellow")
    jem.pensize(2)

    t = int(input("Number of petals?" ))

    for _ in range(t):
        jem.penup()
        jem.goto(int(random.randrange(-300,300)), int(random.randrange(-300,300)))
        jem.begin_fill()
        jem.pendown()
        Petal(jem, 100,70)
        jem.end_fill()
        jem.penup()

    wn.exitonclick()

main()
