
from microbit import *

def convertTime(time, unidad):
    unit = (time // unidad) % 60
    print(unit)
    time = time + 1000
            
    return unit and time

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
    
    un_segundo = 1000    #miliseconds en un segundos
    un_minuto  = 60000   #miliseconds en un minuto
    una_hora   = 3600000 #miliseconds en

    #Si a y b not pressed -- Seconds
    #Si a pressed -- Hours
    #Si b pressed -- Mins
    
    time = 0
    
    while True:
        
        while button_a.is_pressed:
            convertTime(time, una_hora)
            display.set_
        while button_b.is_pressed:
            convertTime(time, un_minuto)
        
        else:
            convertTime(time, un_segundo)

if __name__ == "__main__":
    main()
