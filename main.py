import keyboard
import time

def stop():
    
    keyboard.release('z')
    keyboard.release('q')
    keyboard.release('s')
    keyboard.release('d')
    keyboard.release('k')
    
    keyboard.press_and_release('F11')
    time.sleep(1)
    keyboard.press_and_release('F11')
    
    print("CropFarmer Stopping")
    wait(10, '')
    exit()

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
        if keyboard.is_pressed('home'): main()
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
       
       
        
def replace_93():
    
    keyboard.press('s')
    time.sleep(0.5)
    keyboard.release('s')
    keyboard.press('z')
    time.sleep(0.5)
    keyboard.release('z')
    
def replace_melon_pump():
    
    keyboard.press('z')
    time.sleep(1.5)
    keyboard.release('z')
    
def replace_cocoa():
    
    keyboard.press('q')
    time.sleep(1.5)
    keyboard.release('q')  
    
def left_strafe_93():
    
    #print("debug: left 93")
    keyboard.press('q')
    
    for i in range (2):
        
        wait(40, 'q')
        keyboard.press('z')
        time.sleep(0.5)
        keyboard.release('z')
    
    wait(40, 'q')
    keyboard.release('q')
    replace_93()
    
def right_strafe_93():
    
    #print("debug: right 93")
    keyboard.press('d')
    
    for i in range(2):
        
        wait(40, 'd')
        keyboard.press('z')
        time.sleep(0.5)
        keyboard.release('z')
    
    wait(40, 'd')
    keyboard.release('d')
    replace_93()
    
def left_strafe_155():
    
    #print("debug: left 155")
    keyboard.press('q')
    wait(73, 'q')
    keyboard.release('q')
    
def right_strafe_155():
    
    #print("debug: right 155")
    keyboard.press('d')
    wait(73, 'd')
    keyboard.release('d')
    
def front_diagonal_327():
    
    #print("debug: front diagonal 327")
    keyboard.press('q')
    wait(50, 'q')
    keyboard.release('q')
    
def back_diagonal_327():
    
    #print("debug: back diagonal 327")
    keyboard.press('s')
    wait(50, 's')
    keyboard.release('s')
    
def front_strafe_155():
    
    #print("debug: front 155")
    keyboard.press('z')
    wait(72, 'z')
    keyboard.release('z')
    
def back_strafe_155():
    
    #print("debug: back 155")
    keyboard.press('s')
    wait(72, 's')
    keyboard.release('s')
    
    

def wheat_or_potato():
    
    #print("debug: wheat or potato cycle")
    for i in range(2):
        left_strafe_93()
        right_strafe_93()
        
    left_strafe_93()
    
def carrot_or_wart():
    
    #print("debug: carrot or wart cycle")
    for i in range(2):
        right_strafe_93()
        left_strafe_93()

    right_strafe_93()
    
def melon_or_pumpkin():
    
    #print("debug: melon or pumpkin")
    for i in range(4):
        
        right_strafe_155()
        replace_melon_pump()
        left_strafe_155()
        replace_melon_pump()
        
    right_strafe_155()
    
def sugar_cane():
    
    #print("debug: sugar cane cycle")
    for i in range(4):
        front_diagonal_327()
        back_diagonal_327()
        
    front_diagonal_327()

def cocoa_bean():
    
    #print("debug: cocoa bean cycle")
    for i in range(8):
        
        front_strafe_155()
        replace_cocoa()
        back_strafe_155()
        replace_cocoa()

def main(): 
    
    to_farm = input("For farm wheat or potato : 1\n"
                    "For farm carrot or wart  : 2\n"
                    "For farm melon or pumpkin: 3\n"
                    "For farm sugar cane      : 4\n"
                    "For farm cocoa beans     : 5\n")
    
    wait(10, '')

    while True:
        
        #print("debug: enter the main loop")
        if keyboard.is_pressed('end'): stop()
        keyboard.press('k')
        
        match (to_farm):
            
            case '1': wheat_or_potato()
            case '2': carrot_or_wart()
            case '3': melon_or_pumpkin()
            case '4': sugar_cane()
            case '5': cocoa_bean()
            case _  : to_farm = input("For farm wheat or potato : 1\n"
                                      "For farm carrot or wart  : 2\n"
                                      "For farm melon or pumpkin: 3\n"
                                      "For farm sugar cane      : 4\n"
                                      "For farm cocoa beans     : 5\n")
            
if __name__ == '__main__':
    
    print("CropFarmer Starting\n")
    main()
    
    