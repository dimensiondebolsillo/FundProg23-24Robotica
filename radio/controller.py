from microbit import *
import radio
# from microbit import sleep, display, Image

posiciones_posibles_de_ordenes = ["FORWARD", "BACKWARDS", "RIGHT",  "LEFT", "STOP"]
posiciones_posibles_de_ordenes_contrarias = ["BACKWARDS", "FORWARD", "LEFT", "RIGHT", "STOP"]

def indiceContrario(orden_inicial):
    """
    Devuelve el indice donde aparece la orden_inicial en la lista de posibles ordenes.
    Como los indices de la lista de ordenes contrarias coinciden, tendriamos el indice del contrario.
    """

    index = 0
    for _ in range(len(posiciones_posibles_de_ordenes)):
        if orden_inicial == posiciones_posibles_de_ordenes[index]:
            index = index
        else:
            index = index + 1

    return index

def main():
    # String con un identificador del emisor, cámbialo para no coincidir con el
    # de otros microbits que puedan estar transmitiendo cerca de ti
    IDENTIFIER = "STOKI"

    # Periodo de emisión del mensaje, en milisegundos
    PERIOD = 10000

    # Enciende la radio
    radio.on()

    # Establece la potencia de la emisión, de 0 a 7 siendo 7 la potencia máxima
    # Mira la documentación para ver otros parámetros que pueden fijarse en radio.config()
    radio.config(channel=7,  # canal, valor entre 0 y 83
                 group=87,   # grupo,valor entre 0 y 255
                 power=6,    # potencia, valor 0 y 7
                 queue=3,    # cola de mensajes
                 length=32)  # longitud máxima de los mensajes, valor entre 0 y 251)

    lista_de_movimientos = ["FORWARD", "LEFT", "LEFT", "BACKWARDS"]

    posicion_actual = 0
    while True:
        # Muestra dos recuadros en pantalla para indicar que va a enviar un mensaje
        display.show(Image.SQUARE)
        sleep(500)
        display.clear()

        if button_a.was_pressed():
            message = lista_de_movimientos[posicion_actual]
            radio.send(message)
            display.scroll("message: " + message + "-sent")
            sleep(500)
            posicion_actual = (posicion_actual + 1) % len(lista_de_movimientos)
        if button_b.was_pressed():
            posicion_nueva = (posicion_actual - 1) % len(lista_de_movimientos)
            message = lista_de_movimientos[posicion_nueva]
            display.scroll(message)
            new_message_index = indiceContrario(message)
            new_message = posiciones_posibles_de_ordenes_contrarias[new_message_index]
            radio.send(new_message)
            display.scroll("message: " + new_message + "-sent")
            sleep(500)

        display.show(Image.SQUARE_SMALL)
        sleep(500)
        display.clear()
        sleep(PERIOD-1000) # ya se han esperado 1000ms al mostrar las imágenes

if __name__ == "__main__":
    main()
