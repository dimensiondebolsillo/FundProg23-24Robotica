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

def move(tortuga, x, y):
    """
    Permite que la tortuga se mueva a ciertas coordenadas (x, y) sin dibujar.
    """
    
    tortuga.penup()
    tortuga.goto(x, y)
    tortuga.pendown()
 
def cuadrilatero(tortuga, ancho, alto, esquina_cor_x, esquina_cor_y):
    """
    Dibuja cuadrilateros de un cierto ancho y alto.
    """
    
    x = tortuga.xcor()
    y = tortuga.ycor()
    head = tortuga.heading()
    
    move(tortuga, esquina_cor_x, esquina_cor_y)
    
    for _ in range(2):
        tortuga.forward(ancho)
        tortuga.left(90)
        tortuga.forward(alto)
        tortuga.left(90)
    
    tortuga.penup()
    tortuga.setpos(x, y)
    tortuga.setheading(head)  
    tortuga.pendown()  
    return
        
def tortugaSet(color, grosor, forma):
    """
    Ayuda a configurar la tortuga con los parámetros que se le den.
    """
    
    tortuga = turtle.Turtle()
    
    tortuga.color(color)
    tortuga.shape(forma)
    tortuga.pensize(grosor)
    
    return tortuga
    
        
    
