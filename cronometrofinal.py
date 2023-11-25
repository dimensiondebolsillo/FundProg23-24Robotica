# Your new file!
from microbit import *

zero = "99999:99999"
one = "00000:99999"
two = "90999:99909"
three = "90909:99999"
four = "99900:09999"
five = "99909:90999"
six = "99999:90999"
seven = "90900:99999"
eight = "99099:99099"
nine = "99900:99999"
fonts = (zero, one, two, three, four, five, six, seven, eight, nine)
segundos = 0
minutos = 0
horas = 0




def ShowTime(time):
    if time >= 10 :
        time = dosnumeros(time)
       
    Fp = -1
    Cp = 0
    numero = fonts[time]
    numerosplit = numero.split(":")
    
     
    for x in range(3, 5):
        for y in range(0, 5): 
            Cp = Cp
            Fp = Fp +1
                
            if Fp == 5 :
                 Fp = 0
                 Cp = 1
                
            display.set_pixel(x, y, int(numerosplit[Cp][Fp]))
        
def dosnumeros(time):
    stringseg = str(time)
    a = int(stringseg[0])
    b = int(stringseg[1])
    numeroa = fonts[a]
    numeroasplit = numeroa.split(":")
    Cp = 0
    Fp = -1
    
    for x in range(0,2):
        for y in range(0, 5):
                Cp = Cp
                Fp = Fp +1
                
                if Fp == 5 :
                     Fp = 0
                     Cp = 1
                    
                display.set_pixel(x, y, int(numeroasplit[Cp][Fp]))

    time = b
    return time
    


def main():
    segundos = 0   
    minutos = 0
    horas = 0
    true = 1
    while true == 1:
        
        for x in range(0,5):
            for y in range(0,5):
                display.set_pixel(x, y, 0)
                
        if button_a.was_pressed():
            time = horas
            ShowTime(time)
            
    
        elif button_b.was_pressed():
            time = minutos
            ShowTime(time)
    
        else :
            time = segundos 
            ShowTime(time)
    
        if segundos == 60 :
            segundos = 0
            minutos = minutos +1
    
        if minutos == 60 :
            minutos = 0
            horas = horas + 1
    
        sleep(1000)
        segundos = segundos + 1
        
        
    
main()
