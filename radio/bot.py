from microbit import *
import gigglebot
import radio

def main():
    radio.on()

    # Establece la potencia de la emisión, de 0 a 7 siendo 7 la potencia máxima
    # Mira la documentación para ver otros parámetros que pueden fijarse en radio.config()
    radio.config(channel=7,  # canal, valor entre 0 y 83
                 group=87,   # grupo,valor entre 0 y 255
                 power=6,    # potencia, valor 0 y 7
                 queue=3,    # cola de mensajes
                 length=32)  # longitud máxima de los mensajes, valor entre 0 y 251)


    while True:
        sleep(1000)

        # Intenta recoger un mensaje que haya llegado al microbit
        # Si no ha llegado ningún mensaje receive_full() devuelve None
        # Si ha llegado un mensaje, receive_full() devuelve una tupla de 3 valores:
        #   - una lista de bytes con el mensaje recibido
        #   - la potencia de señal recibida, en dBm, entre 0 (potencia máxima) y -255 (potencia mínima)
        #   - una marca de tiempo con el instante en que se recibió el mensaje
        received = radio.receive_full()

        if received != None:
            # Separamos los 3 valores de la tupla. La marca de tiempo no la usaremos
            msg = received[0]
            dBm = received[1]
            ts = received[2]

            # En msg los primeros 3 bytes de la lista son una cabecera que descartamos
            # Convertimos el resto de bytes a un string con codificación UTF8
            msg = str(msg[3:], 'utf8')

            if msg == "FORWARD":
                gigglebot.drive(gigglebot.FORWARD, 100)
                sleep(1000)
            elif msg == "LEFT":
                gigglebot.turn(gigglebot.LEFT, 500)
                sleep(1000)
            elif msg == "RIGHT":
                gigglebot.turn(gigglebot.RIGHT, 500)
                sleep(1000)
            elif msg == "BACKWARDS":
                gigglebot.drive(gigglebot.BACKWARD, 100)
                sleep(1000)
            elif msg == "STOP":
                gigglebot.stop()
                sleep(1000)

            # Muestra en el display el identificador recibido y la potencia de señal
            # con la que se recibió
            # el segundo parámetro de scroll() permite variar la velocidad en que
            # se muestra el texto (por defecto 150, cuanto más bajo más rápido se
            # desplaza el texto)
            display.scroll(msg + " # " + str(dBm), 60)

if __name__ == "__main__":
    main()
