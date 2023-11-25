# Imports go at the top
from microbit import *

def cronometroDisplay(time, fonts):
    """
    
    """
    if time < 10:
        digito = fonts[time]
        digito_after_split = digito.split(":")
        
        index_digito = 0
        index_digito_after_split = - 1 #Le pongo el valor - 1 para que en cada iteración, al sumarle 1, los índices vayan pasando de 0 a 4.
        
        for x in range(3, 5):
            for y in range(0, 5):
                
                index_digito_after_split = (index_digito_after_split + 1) % 5
                index_digito = (index_digito) % 5

                if ((index_digito_after_split + 1) % 5 == 0):
                    index_digito = 1
                
                display.set_pixel(x, y, int(digito_after_split[index_digito][index_digito_after_split]))

    else:

        #Divido el numero en dos digitos.
        digito_1 = time // 10
        digito_2 = time % 10
        
        #Configura el display de digito_1 en (0, 2).

        digito = fonts[digito_1]
        digito_after_split = digito.split(":")

        index_digito = 0
        index_digito_after_split = - 1 #Le pongo el valor - 1 para que en cada iteración, al sumarle 1, los índices vayan pasando de 0 a 4.
        
        for x in range(0, 2):
            for y in range(0, 5):
                
                index_digito_after_split = (index_digito_after_split + 1) % 5
                index_digito = (index_digito) % 5

                if ((index_digito_after_split + 1) % 5 == 0):
                    index_digito = 1
                
                display.set_pixel(x, y, int(digito_after_split[index_digito][index_digito_after_split]))

        #Configura el display de digito_2 en (3, 5).
        time = digito_2
        cronometroDisplay(time, fonts)

    
def main():
    zero  = "99999:99999"
    one   = "00000:99999"
    two   = "90999:99909"
    three = "90909:99999"
    four  = "99900:09999"
    five  = "99909:90999"
    six   = "99999:90999"
    seven = "90900:99999"
    eight = "99099:99099"
    nine  = "99900:99999"
    fonts = (zero, one, two, three, four, five, six, seven, eight, nine)

    segundos = 0
    while True:

        time = segundos % 60
        cronometroDisplay(time, fonts)
    
        #En horas (3600 segundos)
        if button_a.is_pressed():
            time = (segundos // 3600) % 60
            cronometroDisplay(time, fonts)
            sleep(500)

        #En minutos (60 segundos)
        if button_b.is_pressed():
            time = (segundos // 60) % 60
            cronometroDisplay(time, fonts)
            sleep(500)

        #En segundos

        sleep(1000)
        segundos = segundos + 1
            

if __name__ == "__main__":
    main()
