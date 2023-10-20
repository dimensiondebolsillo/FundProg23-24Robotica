import turtle

def drawPoly(t, somesides, somesize):
    """Get turtle t to draw a regular polygon X side and Y size"""

    for i in range(somesides):
        t.forward(somesize)
        t.left(360/somesides)

def PolyWHOLE(h):
    """Draw polygon and move."""
    tess.pendown()
    tess.color(h)
    drawPoly(tess, t, z)
    tess.penup()

wn = turtle.Screen()
tess = turtle.Turtle()

t = int(input("How many sides?" ))
z = int(input("Side lenght?" ))

tess.goto(0, 0)
PolyWHOLE("red")
tess.goto(0, 3 * z)
PolyWHOLE("yellow")
tess.goto(3 * z, 3 * z)
PolyWHOLE("blue")
tess.goto(3 * z, 0)
PolyWHOLE("green")

wn.exitonclick()
