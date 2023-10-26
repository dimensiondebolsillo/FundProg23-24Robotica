import galapagar

NUMERO_DE_ESTUDIO = 1
ANCHURA_VENTANA = 800
ALTURA_VENTANA = 800

def main():

    the_window = galapagar.init("Estudio " + str(NUMERO_DE_ESTUDIO),
                                "lightgray",
                                ANCHURA_VENTANA,
                                ALTURA_VENTANA)
                                
    kaarl = galapagar.tortugaSet("green", 10, "turtle")
    
    accum = 0
    for i in range(3):
        accum = accum + 103
        galapagar.cuadrilatero(kaarl, 100, 50, 157 - accum, -88)
    
    accum = 0
    for i in range(3):
        accum = accum + 103
        galapagar.cuadrilatero(kaarl, 100, 50, 157 - accum, -25)
        
    accum = 0
    for i in range(3):
        accum = accum + 103
        galapagar.cuadrilatero(kaarl, 100, 50, 157 - accum, 38)
    
    galapagar.finish(the_window)


main()
