import galapagar

NUMERO_DE_ESTUDIO = 1
ANCHURA_VENTANA = 800
ALTURA_VENTANA = 800

def main():

    the_window = galapagar.init("Estudio " + str(NUMERO_DE_ESTUDIO),
                                "lightgray",
                                ANCHURA_VENTANA,
                                ALTURA_VENTANA)
                                
    kaarl = galapagar.tortugaSet("blue", 10, "turtle")
    
    accum = 0
    for i in range(3):
        accum = accum + 105
        galapagar.cuadrilatero(kaarl, 100, 100, 300 - accum, 200)
    
    accum = 0
    for i in range(3):
        accum = accum + 105
        galapagar.cuadrilatero(kaarl, 100, 100, 300 - accum, 95)
    
    galapagar.finish(the_window)


main()
