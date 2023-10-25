"""Código para realizar los ejercicios de la asignatura Fundamentos de
Programación del grado en Ingeniería de Robótica Software de nombre:
"Estudios sobre abstracción funcional para Python y cuarteto de galápagos"
"""

import turtle

def init(title, color, width, height):
    """
    Crea una ventana para poder dibujar con el módulo de python turtle

    Parámetros: título, color de fondo, ancho, alto de la ventana creada y nombre de la tortuga.
    Devuelve: la ventana creada.
    """

    window = turtle.Screen()
    turtle.setup(width, height)
    window.bgcolor(color)
    window.title(title)

    return window

def finish(window):
    """
    Espera a que se haga click en window para cerrar la ventana.
    Se debe llamar al final de un programa que use turtle.

    Parámetros: una ventana creada por init()
    """

    window.exitonclick()
    
def drawSquare(name, X):
    """
    Draw squares of X side calling the turtle.
    """
    
    for _ in range(4):
        name.forward(X)
        name.left(90)
        
def MOVE(name, u, v):
    """
    put penup to move using goto function from turtle module.
    """
    name.penup()
    name.goto(u, v)
    name.pendown()
    
def drawRectangle(name, X, Y):
    """
    Draw rectangles of X alto and Y ancho.
    """
    
    for _ in range(2):
        name.forward(Y)
        name.left(90)
        name.forward(X)
        name.left(90)
    
