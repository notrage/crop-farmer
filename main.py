from paterns import *

if __name__ == '__main__':

    wait(10, '')

    while True:
        
        if keyboard.is_pressed('end'): stop()
        keyboard.press('k')
        wheat_or_potato()