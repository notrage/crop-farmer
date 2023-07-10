import keyboard
import time

def stop():
    
    keyboard.release('q')
    keyboard.release('d')
    keyboard.release('k')
    
    keyboard.press_and_release('F11')
    time.sleep(1)
    keyboard.press_and_release('F11')
    
    exit("CropFarmer stopped")

def pause(direction):
    
    keyboard.release(direction)
    keyboard.release('k')
    print("CropFarmer paused")
    
    keyboard.press_and_release('F11')
    time.sleep(1)
    keyboard.press_and_release('F11')
    
    for i in range(1000000):
        if keyboard.is_pressed('end'): stop()
        if keyboard.is_pressed('p'): break
        time.sleep(1)
        
    keyboard.press('k')
    time.sleep(2)
    keyboard.press(direction)
    print("CropFarmer unpaused")
    

def wait(n, direction):
    
    for i in range(n):
        if keyboard.is_pressed('end'): stop()
        if keyboard.is_pressed('p'): pause(direction)
        time.sleep(1)
        
def replace():
    
    keyboard.press('s')
    time.sleep(0.5)
    keyboard.release('s')
    keyboard.press('z')
    time.sleep(0.5)
    keyboard.release('z')
    

def left_strafe():
    
    keyboard.press('q')
    
    for i in range (2):
        
        wait(40, 'q')
        keyboard.press('z')
        time.sleep(0.5)
        keyboard.release('z')
    
    wait(40, 'q')
    keyboard.release('q')
    replace()
    
def right_strafe():
    
    keyboard.press('d')
    
    for i in range(2):
        
        wait(40, 'd')
        keyboard.press('z')
        time.sleep(0.5)
        keyboard.release('z')
    
    wait(40, 'd')
    keyboard.release('d')
    replace()
    
def front_strafe():
    
    print("todo")
    
def back_stafe():
    
    print("todo")
