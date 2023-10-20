import turtle

def drawPoly(t, somesides, somesize):
    """Get turtle t to draw a regular polygon X side and Y size"""
    
    for i in range(somesides):
        t.forward(somesize)
        t.left(360/somesides)

wn = turtle.Screen()

tess = turtle.Turtle()

t = int(input("How many sides?" ))
z = int(input("Side lenght?" ))
drawPoly(tess, t, z)

wn.exitonclick()