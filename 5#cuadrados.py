import turtle

def SQUARE(sz):
    """Draw square"""
    for _ in range(4):
        w.forward(sz)
        w.left(90)
        
wn = turtle.Screen()
w = turtle.Turtle()

squares = int(input("Number of squares?: " ))
lado = int(input("Side length?: " ))
ang = int(input("ANgle between squares?: " ))

for _ in range(squares):
    SQUARE(lado)
    w.left(ang)

wn.exitonclick()
