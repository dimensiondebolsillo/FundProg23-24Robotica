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
    name.color("red")
    
    galapagar.MOVE(name, -200, -200)
    galapagar.drawSquare(name, 50)
    galapagar.MOVE(name, -200, 200)
    galapagar.drawSquare(name, 50)
    galapagar.MOVE(name, 200, 200)
    galapagar.drawSquare(name, 50)
    galapagar.MOVE(name, 200, -200)
    galapagar.drawSquare(name, 50)
    
    galapagar.finish(the_window)


main()
