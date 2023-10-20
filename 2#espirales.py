import turtle

def Striangle():
    """Draw lado del triángulo 260 veces, girando para crear una espiral trinagular."""
    for i in range(60, 260, 10):
        a.forward(i)
        a.right(120)

wn = turtle.Screen()
a = turtle.Turtle()

a.right(30)
Striangle()

wn.exitonclick()
