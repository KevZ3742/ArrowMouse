import pyautogui
import screeninfo
from pynput import keyboard
import time

pyautogui.FAILSAFE = False
screen_info = screeninfo.get_monitors()[0]
dimentions = [screen_info.width,screen_info.height]
dotLocation = [screen_info.width//2,screen_info.height//2]
sensitivity = 25
leftPressed, rightPressed, upPressed, downPressed, escPressed = False, False, False, False, False

def boundValue(dotLocation, index, operation, maxDimention, sensitivity):
    if eval(str(dotLocation[index]) + operation + str(sensitivity)) > maxDimention:
        dotLocation[index] = maxDimention
    if eval(str(dotLocation[index]) + operation + str(sensitivity)) < 0:
        dotLocation[index] = 0
    return dotLocation

def on_press(key):
    global leftPressed, rightPressed, upPressed, downPressed, escPressed
    if key == keyboard.Key.esc:
        escPressed = True
        return False   
    
    if key == keyboard.Key.left:
        leftPressed = True
        rightPressed = False
    elif key == keyboard.Key.right:
        rightPressed = True
        leftPressed = False

    if key == keyboard.Key.up:
        upPressed = True
        downPressed = False
    elif key == keyboard.Key.down:
        downPressed = True
        upPressed = False

def on_release(key):
    global leftPressed, rightPressed, upPressed, downPressed
    if key == keyboard.Key.left:
        leftPressed = False
    if key == keyboard.Key.right:
        rightPressed = False
    if key == keyboard.Key.up:
        upPressed = False
    if key == keyboard.Key.down:
        downPressed = False

def check_key_status(dotLocation, sensitivity, maxWidth, maxHeight):
    running = True
    while running:
        if leftPressed:
            dotLocation[0] -= sensitivity
            dotLocation = boundValue(dotLocation, 0, "-", maxWidth-1, sensitivity)
        if rightPressed:
            dotLocation[0] += sensitivity
            dotLocation = boundValue(dotLocation, 0, "+", maxWidth-1, sensitivity)
        if upPressed:
            dotLocation[1] -= sensitivity
            dotLocation = boundValue(dotLocation, 1, "-", maxHeight-1, sensitivity)
        if downPressed:
            dotLocation[1] += sensitivity
            dotLocation = boundValue(dotLocation, 1, "+", maxHeight-1, sensitivity)
        if escPressed:
            running = False
        pyautogui.moveTo(dotLocation[0], dotLocation[1])
        time.sleep(.01)

listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()
check_key_status(dotLocation, sensitivity, dimentions[0], dimentions[1])
listener.join()

# ToDo:
#
# Status: Not Completed - Add sensitivity changing (ctrl + up/down)
# Status: Not Completed - Add sensitivity reset (ctrl + 0)
# Status: Not Completed - Add left/right click (ctrl + left/right)