import galapagar

NUMERO_DE_ESTUDIO = 1
ANCHURA_VENTANA = 800
ALTURA_VENTANA = 800

def main():

    the_window = galapagar.init("Estudio " + str(NUMERO_DE_ESTUDIO),
                                "lightgray",
                                ANCHURA_VENTANA,
                                ALTURA_VENTANA)
                                
    kaarl = galapagar.tortugaSet("red", 5, "turtle")
    
    accum = 0
    for i in range(4):
        accum = accum + 100
        galapagar.cuadrilatero(kaarl, 100, 100, -300 + accum, -200)
    
    accum = 0
    for i in range(4):
        accum = accum + 100
        galapagar.cuadrilatero(kaarl, 100, 100, -300 + accum, -100)
    
    accum = 0
    for i in range(4):
        accum = accum + 100
        galapagar.cuadrilatero(kaarl, 100, 100, -300 + accum, 0)
    
    accum = 0
    for i in range(4):
        accum = accum + 100
        galapagar.cuadrilatero(kaarl, 100, 100, -300 + accum, 100)
    
    galapagar.finish(the_window)


main()
