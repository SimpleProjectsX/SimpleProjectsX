print("Hack Started...")
import pyautogui
from pynput import keyboard
import win32api


def chathack():
    pyautogui.click(clicks=150, interval=0.00001)

    



#while True:
#    with keyboard.Events() as events:
#
#        for event in events:
#        
            
#            if str(event.key) == "'f'":
                
#                chathack("/balloon")
                
#            break



state_left = win32api.GetKeyState(0x01)  # Left button down = 0 or 1. Button up = -127 or -128
state_right = win32api.GetKeyState(0x02)  # Right button down = 0 or 1. Button up = -127 or -128





while True:

    a = win32api.GetKeyState(0x01)
    b = win32api.GetKeyState(0x02)

    if b != state_right:  # Button state changed
        state_right = b
        # print(b)
        if b < 0:
            chathack()
        else:
            pass








        


