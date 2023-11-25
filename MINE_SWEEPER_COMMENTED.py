from microbit import *
import random

def setMine():
    """
    Set the coordinates for the mine using random numbers, it also sets its intensity.
    """

    mine_x_coordinate = random.randrange(0, 4)
    mine_y_coordinate = random.randrange(0, 4)
    display.set_pixel(mine_x_coordinate, mine_y_coordinate, 4)

    return mine_x_coordinate, mine_y_coordinate

def brightness(cursor_x, cursor_y):
    """
    Get the brightness a certain pixel has.
    """
    
    brightness = display.get_pixel(cursor_x, cursor_y)

    return brightness

def positionPlayer(x, y, desplazamiento_x, desplazamiento_y):
    """
    Set coordinates for player (cursor).
    """
    
    x_anterior = x
    y_anterior = y
    x_posterior = (x + desplazamiento_x) % 5
    y_posterior = (y + desplazamiento_y) % 5
    
    brightness_anterior = brightness(x_anterior, y_anterior)
    if brightness_anterior == 0:
        display.set_pixel(x_anterior, y_anterior, brightness_anterior)
    else:
        display.set_pixel(x_anterior, y_anterior, 4)

    brightness_posterior = brightness(x_posterior, y_posterior)
        
    display.set_pixel(x_posterior, y_posterior, 9)

    
    
    return x_posterior, y_posterior

def mineDetector(mine_x, mine_y, cursor_x, cursor_y, score):
    """
    Determines whether or not the player position is equal to the mine position.
    If it's the case, it displays the score and a message before it ends.
    On the other hand, if it's not the case, it displays a happy face and turns off the LED.
    """

    if (mine_x, mine_y) == (cursor_x, cursor_y): #mine found.
        display.show(Image.SQUARE_SMALL)
        sleep(1000)
        display.show(Image.SQUARE)
        sleep(1000)
        display.show(Image.SKULL)
        sleep(2000)
        display.scroll("score: " + str(score), delay = 300)
        sleep(1000)
        display.scroll("~GAME OVER~", delay = 300)

        return score


    if (mine_x, mine_y) != (cursor_x, cursor_y): #mine not found.
        score = score + 1
        display.set_pixel(cursor_x, cursor_y, 2)
        sleep(200)
        display.set_pixel(cursor_x, cursor_y, 0)
        sleep(100)
        display.set_pixel(cursor_x, cursor_y, 5)
        sleep(200)
        display.set_pixel(cursor_x, cursor_y, 7)
        sleep(200)
        display.set_pixel(cursor_x, cursor_y, 3)
        sleep(200)
        display.set_pixel(cursor_x, cursor_y, 0)
        
        return score
    
def main():
    #Set mine coordinates and storages them on variables x and y.
    mine_x, mine_y = setMine()
    
    #Set player on the micro:bit center: (2, 2).
    cursor_x, cursor_y = positionPlayer(2, 2, 0, 0)

    #Set every LED to medium brightness.
    medium_brightness = 4
    for x in range(5):
        for y in range(5):
            display.set_pixel(x, y, medium_brightness) 

    #Set the player display brightness to 9.
    display.set_pixel(cursor_x, cursor_y, 9)

    score = 0
    while (score != 24):

        if button_a.was_pressed():
            #Search for mine and return score.
            score = mineDetector(mine_x, mine_y, cursor_x, cursor_y, score)
    
        if accelerometer.was_gesture('right'):
            desplazamiento_x = 1
            cursor_x, cursor_y  = positionPlayer(cursor_x, cursor_y, desplazamiento_x, 0) #Update player position

        if accelerometer.was_gesture('left'):
            desplazamiento_x = -1
            cursor_x, cursor_y = positionPlayer(cursor_x, cursor_y, desplazamiento_x, 0) #Update player position

        if accelerometer.was_gesture('up'):
            desplazamiento_y = -1
            cursor_x, cursor_y = positionPlayer(cursor_x, cursor_y, 0, desplazamiento_y) #Update player position

        if accelerometer.was_gesture('down'):
            desplazamiento_y = 1
            cursor_x, cursor_y = positionPlayer(cursor_x, cursor_y, 0, desplazamiento_y) #Update player position

        if score == 24:
            display.show(Image.DIAMOND)
            sleep(1000)
            display.scroll("YOU WIN!!!", delay = 300)
            sleep(1000)
            display.show(Image.SNAKE)

if __name__ == "__main__":
    main()
