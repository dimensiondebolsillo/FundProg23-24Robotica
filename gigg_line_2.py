from microbit import *
import gigglebot

strip = gigglebot.init()
gigglebot.set_speed(70, 70)

# Umbral de detección de negro
THRESHOLD = 100

def orientarBot(umbral_de_detección, side_0, side_1):
    """
    Mientras no se detecta línea negra en su totalidad debajo, comprueba los sensores izquierdos y derechos del gigglebot.
    Mientras el sensor izquierdo no detecte y el sensor derecho detecte linea, girará hacia ese lado y volvera a comprobar los sensores;
    para el otro sensor hace lo mismo.
    En el caso de que no se detecte en ningún sensor, gira y comprueba.
    """

    # Detecta línea.
    if (side_0 < umbral_de_detección) and (side_1 < umbral_de_detección):
        strip[2] = (0, 255, 0)
        strip[8] = (0, 255, 0)
        strip.show()
        gigglebot.drive(gigglebot.FORWARD, 100)
        sleep(1000)
    # Sensor izquierdo no detecta, sensor derecho sí.
    elif (side_0 > umbral_de_detección) and (side_1 < umbral_de_detección):
        strip[2] = (0, 255, 0)
        strip[8] = (0, 0, 0)
        strip.show()
        gigglebot.turn(gigglebot.RIGHT, 50)
        sleep(1000)
    # Sensor derecho no detecta, sensor izquierdo sí.
    elif (side_1 > umbral_de_detección) and (side_0 < umbral_de_detección):
        strip[2] = (0, 0, 0)
        strip[8] = (0, 255, 0)
        strip.show()
        gigglebot.turn(gigglebot.LEFT, 50)
        sleep(1000)
    else:
        gigglebot.stop()

def main():
    while True:
        strip[2] = (0, 0, 0)
        strip[8] = (0, 0, 0)
        strip.show()
        try:
            left, right = gigglebot.read_sensor(gigglebot.LINE_SENSOR, gigglebot.BOTH)
            orientarBot(THRESHOLD, right, left)
        except OSError:
            pass
        sleep(200)
        gigglebot.stop()

if __name__ == "__main__":
    main()
