import turtle

def Espiral(angulo, aumento):
    """Crear una espiral que aunmenta de grosor."""
    lado = 1
    grosor = 1
    for t in range(800):
        w.forward(lado)
        w.left(angulo)
        lado = lado + i
        w.pensize(grosor)
        grosor = grosor + 0.05

wn = turtle.Screen()
w = turtle.Turtle()

i = float(input("Incremento? (Ej: 0.05): " ))
ang = int(input("Ángulo?: " ))

Espiral(ang, i)

wn.exitonclick()

