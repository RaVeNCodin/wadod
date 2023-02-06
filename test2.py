import pyautogui
import time
time.sleep (3)
# Get the current x, y coordinates of the mouse
x, y = pyautogui.position()
print("Mouse coordinates: ", x, y)

# Get the top and bottom of the screen
screen_width, screen_height = pyautogui.size()
print("Screen top: ", 0)
print("Screen bottom: ", screen_height)
