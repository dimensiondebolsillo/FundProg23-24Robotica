import galapagar

NUMERO_DE_ESTUDIO = 1
ANCHURA_VENTANA = 800
ALTURA_VENTANA = 800

def main():

    the_window = galapagar.init("Estudio " + str(NUMERO_DE_ESTUDIO),
                                "lightgray",
                                ANCHURA_VENTANA,
                                ALTURA_VENTANA)
                                
    name = galapagar.turtle.Turtle()
    name.color("green")
    name.shape("turtle")
    name.pensize(5)
    
    galapagar.MOVE(name, -200, -200)
    galapagar.drawRectangle(name, 100, 50)
    galapagar.MOVE(name, -200, 200)
    galapagar.drawRectangle(name, 100, 50)
    galapagar.MOVE(name, 200, 200)
    galapagar.drawRectangle(name, 100, 50)
    galapagar.MOVE(name, 200, -200)
    galapagar.drawRectangle(name, 100, 50)
    
    name.color("blue")
    name.shape("triangle")
    name.pensize(2)
    
    galapagar.MOVE(name, -200, -200)
    galapagar.drawSquare(name, 60)
    galapagar.MOVE(name, -200, 200)
    galapagar.drawSquare(name, 60)
    galapagar.MOVE(name, 200, 200)
    galapagar.drawSquare(name, 60)
    galapagar.MOVE(name, 200, -200)
    galapagar.drawSquare(name, 60)
    
    galapagar.finish(the_window)


main()
