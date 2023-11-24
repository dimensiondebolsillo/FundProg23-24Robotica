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

def positionPlayer(x, y, desplazamiento_x, desplazamiento_y):
    """
    Set coordinates for player (cursor).
    """

    x = (x + desplazamiento_x) % 5
    y = (y + desplazamiento_y) % 5

    display.set_pixel(x, y, 7)

    return x, y

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
        display.show(Image.HAPPY)
        sleep(1000)
        display.scroll("score: " + str(score), delay = 300)
        sleep(1000)

        return score

def main():
    #Set mine coordinates and storages them on variables x and y.
    mine_x, mine_y = setMine()

    #Set player on the micro:bit center: (2, 2).
    cursor_x, cursor_y = positionPlayer(2, 2, 0, 0)

    score = 0
    while not button_a.is_pressed():

        #Set every LED to the brightness it had before.
        for x in range(5):
            for y in range(5):
                display.set_pixel(x, y, 4) #Aquí iría la condicion de si hay casilla en brightness 0, no cambiarlas. ELse: brightness = 4.

        #Set the player display brightness to 7.
        display.set_pixel(cursor_x, cursor_y, 7)

        if button_a.was_pressed():
            #Search for mine and return score.
            score = mineDetector(mine_x, mine_y, cursor_x, cursor_y, score)
            #Turn the searched pixel to 0 if mine not found. (This doesnt work for me... :( )
            display.set_pixel(cursor_x, cursor_y, 0)

        if accelerometer.was_gesture('right'):
            display.set_pixel(cursor_x, cursor_y, 4) #Should return the brightness the pixel had, 0 if searched, 4 if not.
            desplazamiento_x = 1
            cursor_x, cursor_y = positionPlayer(cursor_x, cursor_y, desplazamiento_x, 0) #Update player position
            print(cursor_x, cursor_y)

        if accelerometer.was_gesture('left'):
            display.set_pixel(cursor_x, cursor_y, 4) #Should return the brightness the pixel had, 0 if searched, 4 if not.
            desplazamiento_x = -1
            cursor_x, cursor_y = positionPlayer(cursor_x, cursor_y, desplazamiento_x, 0) #Update player position
            print(cursor_x, cursor_y)

        if accelerometer.was_gesture('up'):
            display.set_pixel(cursor_x, cursor_y, 4) #Should return the brightness the pixel had, 0 if searched, 4 if not.
            desplazamiento_y = -1
            cursor_x, cursor_y = positionPlayer(cursor_x, cursor_y, 0, desplazamiento_y) #Update player position
            print(cursor_x, cursor_y)

        if accelerometer.was_gesture('down'):
            display.set_pixel(cursor_x, cursor_y, 4) #Should return the brightness the pixel had, 0 if searched, 4 if not.
            desplazamiento_y = 1
            cursor_x, cursor_y = positionPlayer(cursor_x, cursor_y, 0, desplazamiento_y) #Update player position
            print(cursor_x, cursor_y)

        if score == 24:
            display.show(Image.DIAMOND)
            sleep(1000)
            display.scroll("YOU WIN!!!", delay = 300)
            sleep(1000)
            display.show(Image.SNAKE)


if __name__ == "__main__":
    main()
