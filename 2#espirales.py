import turtle

wn = turtle.Screen()
a = turtle.Turtle()

a.right(30)
def triangle():
    for i in range(60, 260, 10):
        a.forward(i)
        a.right(120)

triangle()

wn.exitonclick()