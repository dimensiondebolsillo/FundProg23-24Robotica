import turtle

def drawPoly(t, somesides, somesize):
    """Get turtle t to draw a regular polygon X side and Y size"""

    for i in range(somesides):
        t.forward(somesize)
        t.left(360/somesides)

wn = turtle.Screen()
w = turtle.Turtle()

l = int(input("Side length?" ))
alpha = int(input("Degrees between polygons? "))
r = int(360 / alpha)

for _ in range(r):
    drawPoly(w, r, l)
    w.left(alpha)

wn.exitonclick()
