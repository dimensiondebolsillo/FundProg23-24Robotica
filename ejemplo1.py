
########################################################################
#
# Agita el micro:bit y observa los cambios en los leds
#
# Abre el REPL y pulsa CTRL-D para reiniciar el programa. Observa lo
# que se muestra cuando pulsas el botón B en el micro:bit
#
# Cambia la llamada a button_b.is_pressed() por button_b.was_pressed()
# y observa la diferencia para entender ambas funciones
#
# sleep(2000) suspende la ejecución del programa durante 2000ms. Prueba
# otros valores
#

from microbit import *

def main():
    number_sad = 0
    while True:
        display.show(Image.HAPPY)
        if accelerometer.was_gesture("shake"):
            display.show(Image.SAD)
            number_sad = number_sad + 1
            sleep(2000)
        if button_b.is_pressed():
            print ("number_sad: " + str(number_sad))

if __name__ == "__main__":
    main()
