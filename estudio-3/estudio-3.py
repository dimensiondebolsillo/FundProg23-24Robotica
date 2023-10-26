import galapagar

NUMERO_DE_ESTUDIO = 1
ANCHURA_VENTANA = 800
ALTURA_VENTANA = 800

def main():

    the_window = galapagar.init("Estudio " + str(NUMERO_DE_ESTUDIO),
                                "lightgray",
                                ANCHURA_VENTANA,
                                ALTURA_VENTANA)
                                
    kaarl = galapagar.tortugaSet("green", 5, "turtle")

    galapagar.cuadrilatero(kaarl, 50, 100, -200, -200)
    galapagar.cuadrilatero(kaarl, 50, 100, -200, 200)
    galapagar.cuadrilatero(kaarl, 50, 100, 200, 200)
    galapagar.cuadrilatero(kaarl, 50, 100, 200, -200)   

    marx = galapagar.tortugaSet("blue", 2, "turtle")
        
    galapagar.cuadrilatero(marx, 60, 60, -200, -200)
    galapagar.cuadrilatero(marx, 60, 60, -200, 200)
    galapagar.cuadrilatero(marx, 60, 60, 200, 200)
    galapagar.cuadrilatero(marx, 60, 60, 200, -200)
    
    galapagar.finish(the_window)


main()
