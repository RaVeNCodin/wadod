import cv2
import pyautogui
import time
import numpy as np
from pywinauto import Application
from pywinauto.mouse import click
import pytesseract
from PIL import ImageGrab





# Start the application
app = Application().connect(title='FINAL FANTASY XIV')

# Select the main window
main_window = app.top_window()


time.sleep (3)
pyautogui.hotkey('alt', 'tab') #this will switch the active window to the game window

time.sleep (3)
# Read the haystack image (the image you want to search in)
screenshot = pyautogui.screenshot()
screenshot.save('bell.png')

screenshot_numpy = np.array(screenshot)
haystack_img = cv2.cvtColor(screenshot_numpy, cv2.COLOR_BGR2RGB)


haystack_img = cv2.imread('bell.png', cv2.IMREAD_UNCHANGED)


# Read the needle image (the image you want to find within the haystack)
needle_img = cv2.imread('sum.png', cv2.IMREAD_UNCHANGED)


# Convert the images to grayscale
gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# Use cv2.matchTemplate() to find the needle in the haystack
result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# Find the coordinates of the top-left corner of the best match
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc

# Draw a rectangle around the match
cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)



# Calculate the center of the match
center_x = top_left[0] + (needle_img.shape[1] / 2)
center_y = top_left[1] + (needle_img.shape[0] / 2)

# Move the mouse cursor to the center of the match
pyautogui.moveTo(center_x, center_y, duration=3.0)




# Move the mouse cursor to the top-left corner of the match
#pyautogui.moveTo(top_left[0], top_left[1], duration=3.0)

time.sleep (1)
#pyautogui.click(button='right')


# Right click on the main window
main_window.right_click()


# retaner 1

time.sleep(3)
screenshot = pyautogui.screenshot()
screenshot.save('r1.png')

screenshot_numpy = np.array(screenshot)
haystack_img = cv2.cvtColor(screenshot_numpy, cv2.COLOR_BGR2RGB)


haystack_img = cv2.imread('r1.png', cv2.IMREAD_UNCHANGED)


# Read the needle image (the image you want to find within the haystack)
needle_img = cv2.imread('aaa.png', cv2.IMREAD_UNCHANGED)



# Convert the images to grayscale
gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# Use cv2.matchTemplate() to find the needle in the haystack
result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# Find the coordinates of the top-left corner of the best match
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc

# Draw a rectangle around the match
cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)



# Calculate the center of the match
center_x = top_left[0] + (needle_img.shape[1] / 2)
center_y = top_left[1] + (needle_img.shape[0] / 2)

# Move the mouse cursor to the center of the match
pyautogui.moveTo(center_x, center_y, duration=3.0)




# Move the mouse cursor to the top-left corner of the match
#pyautogui.moveTo(top_left[0], top_left[1], duration=3.0)

time.sleep (1)
#pyautogui.click(button='left')


# Right click on the main window
main_window.right_click()

time.sleep(2)

main_window.right_click()

time.sleep(1)
main_window.right_click()

# list

time.sleep(3)
screenshot = pyautogui.screenshot()
screenshot.save('l1.png')

screenshot_numpy = np.array(screenshot)
haystack_img = cv2.cvtColor(screenshot_numpy, cv2.COLOR_BGR2RGB)


haystack_img = cv2.imread('l1.png', cv2.IMREAD_UNCHANGED)


# Read the needle image (the image you want to find within the haystack)
needle_img = cv2.imread('lis.png', cv2.IMREAD_UNCHANGED)



# Convert the images to grayscale
gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# Use cv2.matchTemplate() to find the needle in the haystack
result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# Find the coordinates of the top-left corner of the best match
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc

# Draw a rectangle around the match
cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)



# Calculate the center of the match
center_x = top_left[0] + (needle_img.shape[1] / 2)
center_y = top_left[1] + (needle_img.shape[0] / 2)

# Move the mouse cursor to the center of the match
pyautogui.moveTo(center_x, center_y, duration=3.0)




# Move the mouse cursor to the top-left corner of the match
#pyautogui.moveTo(top_left[0], top_left[1], duration=3.0)

time.sleep (1)
#pyautogui.click(button='left')

main_window.right_click()
    
time.sleep(2)

# # Define the coordinates of the area you want to capture
# left = 1022
# top = 745
# right = 1022 + 90
# bottom = 754 + 35


# # Take the screenshot
# screenshot = ImageGrab.grab(bbox=(left, top, right, bottom))

# # Save the screenshot
# screenshot.save("ttestt.png")

# img = cv2.imread('ttestt.png')

# # Convert to grayscale
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# # Apply Otsu threshold
# thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# # Pass the image to tesseract OCR
# number_string = pytesseract.image_to_string(thresh, lang='eng', config='--psm 10')

# # Convert the string to an integer
# number_int = (number_string)

# # Print the integer variable
# #print(number_int)

# string_num = number_int

# # Split the string by the "/" character
# parts = string_num.split("/")

# # Get the first part (the numerator) and convert it to an integer
# numerator = int(parts[0])

# Print the result
print(numerator)
for i in range(numerator):

# Set the coordinates to move the cursor
    pyautogui.moveTo(675 , 410)
    time.sleep(2)
    main_window.click()
import cv2
import pyautogui
import time
import numpy as np
from pywinauto import Application
from pywinauto.mouse import click
import pytesseract
from PIL import ImageGrab
import re
from pywinauto import Application
from pywinauto.mouse import click
import pytesseract
from PIL import ImageGrab
from pymouse import PyMouse

import keyboard



# Select the main window


time.sleep(2)
app = Application().connect(title='FINAL FANTASY XIV')

# Select the main window
main_window = app.top_window()
# Set a list of coordinates to move the cursor
coordinates = [(577, 272), (611 , 328), (543, 378), (613, 406) , (613, 443), (554, 492), (554, 492), ( 637, 573), ( 637, 573), (558, 675)]
class Task:
    def __init__(self):
        pass
    def do_task(self):
    
     main_window.right_click()

     

task = Task()
task.do_task()

# # # Use a for loop to click on the coordinates 10 times
i = 10
if i >= 1:
    # perform task
    pyautogui.moveTo(577, 272, duration=1)
    task.do_task()
time.sleep(5)



screenshot = pyautogui.screenshot()

haystack_img = cv2.imread('adjustfull.png', cv2.IMREAD_UNCHANGED)


# Read the needle image (the image you want to find within the haystack)
needle_img = cv2.imread('adjust.png', cv2.IMREAD_UNCHANGED)


screenshot_numpy = np.array(screenshot)
haystack_img = cv2.cvtColor(screenshot_numpy, cv2.COLOR_BGR2RGB)


# Convert the images to grayscale
gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# Use cv2.matchTemplate() to find the needle in the haystack
result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# Find the coordinates of the top-left corner of the best match
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc

# Draw a rectangle around the match
cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)



# Calculate the center of the match
center_x = top_left[0] + (needle_img.shape[1] / 2)
center_y = top_left[1] + (needle_img.shape[0] / 2)

# Move the mouse cursor to the center of the match
pyautogui.moveTo(center_x, center_y, duration=1.0)

main_window.right_click()
time.sleep(1)
screenshot = pyautogui.screenshot()

haystack_img = cv2.imread('comparefull.png', cv2.IMREAD_UNCHANGED)


# Read the needle image (the image you want to find within the haystack)
needle_img = cv2.imread('compare.png', cv2.IMREAD_UNCHANGED)


screenshot_numpy = np.array(screenshot)
haystack_img = cv2.cvtColor(screenshot_numpy, cv2.COLOR_BGR2RGB)


# Convert the images to grayscale
gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# Use cv2.matchTemplate() to find the needle in the haystack
result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# Find the coordinates of the top-left corner of the best match
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc

# Draw a rectangle around the match
cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)



# Calculate the center of the match
center_x = top_left[0] + (needle_img.shape[1] / 2)
center_y = top_left[1] + (needle_img.shape[0] / 2)

# Move the mouse cursor to the center of the match
pyautogui.moveTo(center_x, center_y, duration=1.0)
time.sleep(1)

x, y = pyautogui.position()
print("Mouse coordinates: ", x, y)
x = x
y = y 
import pyautogui
import pydirectinput
pydirectinput.moveTo(x, y)
pydirectinput.click()
pydirectinput.click()


time.sleep(2)
screenshot = pyautogui.screenshot()

haystack_img = cv2.imread('fullSEARCH.png', cv2.IMREAD_UNCHANGED)


# Read the needle image (the image you want to find within the haystack)
needle_img = cv2.imread('SREACH.png', cv2.IMREAD_UNCHANGED)


screenshot_numpy = np.array(screenshot)
haystack_img = cv2.cvtColor(screenshot_numpy, cv2.COLOR_BGR2RGB)


# Convert the images to grayscale
gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# Use cv2.matchTemplate() to find the needle in the haystack
result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# Find the coordinates of the top-left corner of the best match
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc

# Draw a rectangle around the match
cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)



# Calculate the center of the match
center_x = top_left[0] + (needle_img.shape[1] / 2)
center_y = top_left[1] + (needle_img.shape[0] / 2)

# Move the mouse cursor to the center of the match
pyautogui.moveTo(center_x, center_y, duration=1.0)
time.sleep(1)

pydirectinput.click()
pydirectinput.click()
time.sleep(1)
screenshot = pyautogui.screenshot()

haystack_img = cv2.imread('FullTEM.png', cv2.IMREAD_UNCHANGED)


# Read the needle image (the image you want to find within the haystack)
needle_img = cv2.imread('item.png', cv2.IMREAD_UNCHANGED)


screenshot_numpy = np.array(screenshot)
haystack_img = cv2.cvtColor(screenshot_numpy, cv2.COLOR_BGR2RGB)


# Convert the images to grayscale
gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# Use cv2.matchTemplate() to find the needle in the haystack
result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# Find the coordinates of the top-left corner of the best match
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc

# Draw a rectangle around the match
cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)



# Calculate the center of the match
center_x = top_left[0] + (needle_img.shape[1] / 2)
center_y = top_left[1] + (needle_img.shape[0] / 2)

# Move the mouse cursor to the center of the match
pyautogui.moveTo(center_x, center_y, duration=1.0)
time.sleep(1)

pydirectinput.click()
pydirectinput.click()

screenshot = pyautogui.screenshot()

haystack_img = cv2.imread('Fullsea.png', cv2.IMREAD_UNCHANGED)


# Read the needle image (the image you want to find within the haystack)
needle_img = cv2.imread('sea.png', cv2.IMREAD_UNCHANGED)


screenshot_numpy = np.array(screenshot)
haystack_img = cv2.cvtColor(screenshot_numpy, cv2.COLOR_BGR2RGB)


# Convert the images to grayscale
gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# Use cv2.matchTemplate() to find the needle in the haystack
result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# Find the coordinates of the top-left corner of the best match
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc

# Draw a rectangle around the match
cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)



# Calculate the center of the match
center_x = top_left[0] + (needle_img.shape[1] / 2)
center_y = top_left[1] + (needle_img.shape[0] / 2)

# Move the mouse cursor to the center of the match
pyautogui.moveTo(center_x, center_y, duration=1.0)
time.sleep(1)

pydirectinput.click()
pydirectinput.click()

# read the haystack and needle images
haystack_img = cv2.imread('FULLHQ.png', cv2.IMREAD_UNCHANGED)
needle_img = cv2.imread('HQ.png', cv2.IMREAD_UNCHANGED)

gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# perform template matching
result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# find the coordinates of the best match
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc

cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)

# center_x = top_left[0] + (needle_img.shape[1] / 2)
# center_y = top_left[1] + (needle_img.shape[0] / 2)

# check if the match is above a certain threshold
threshold = 0.8
if max_val > threshold:
  center_x = top_left[0] + (needle_img.shape[1] / 2)
  center_y = top_left[1] + (needle_img.shape[0] / 2)

  pyautogui.moveTo(center_x, center_y, duration=1.0)


  time.sleep(1)
  keyboard.press("alt")
  time.sleep(2)
  pyautogui.moveRel(0, 20)
  time.sleep(0.5)
  pyautogui.moveRel(200, 0)
  time.sleep(5)
  keyboard.release("alt")
  x, y = pyautogui.position()

  x = x 
  y = y
  print("Mouse coordinates: ", x, y)




  left, top, width, height = (x - 83, y - 17, 110, 30)
  screenshot = pyautogui.screenshot(region=(left, top, width, height))
  screenshot.save("p1.png")
# Take the screenshot
#   screenshot = ImageGrab.grab(bbox=(left, top, right, bottom))

# # Save the screenshot
#   screenshot.save("p1.png")

  img = cv2.imread('p1.png')

# Convert to grayscale
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Otsu threshold
  thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# Pass the image to tesseract OCR
  number_string = pytesseract.image_to_string(thresh, lang='eng', config='--psm 10')
  number_string = number_string.replace('—___—\n', '')
  number_string = number_string.replace('\n', '')

  number_int = int(number_string)


# Print the integer variable
  print(number_int)

  number_int -= 1
  print(number_int)
  time.sleep(3)
  haystack_img = cv2.imread('fullX.png', cv2.IMREAD_UNCHANGED)
  needle_img = cv2.imread('X.png', cv2.IMREAD_UNCHANGED)

  gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
  gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# perform template matching
  result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# find the coordinates of the best match
  min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
  top_left = max_loc

  cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)
  center_x = top_left[0] + (needle_img.shape[1] / 2)
  center_y = top_left[1] + (needle_img.shape[0] / 2)


# Move the mouse cursor to the center of the match
  pyautogui.moveTo(center_x, center_y, duration=1.0)
  pydirectinput.click()
  pydirectinput.click()
  haystack_img = cv2.imread('fullASK.png', cv2.IMREAD_UNCHANGED)
  needle_img = cv2.imread('ASK.png', cv2.IMREAD_UNCHANGED)

  gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
  gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# perform template matching
  result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# find the coordinates of the best match
  min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
  top_left = max_loc

  cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)
  center_x = top_left[0] + (needle_img.shape[1] / 2)
  center_y = top_left[1] + (needle_img.shape[0] / 2)


# Move the mouse cursor to the center of the match
  pyautogui.moveTo(center_x, center_y, duration=1.0)
  pyautogui.moveRel(100, 0)
  pydirectinput.click()
  time.sleep(1)
  keyboard.press("backspace")
  keyboard.release("backspace")
  time.sleep(1)
  pyautogui.typewrite(str(number_int))
  

  haystack_img = cv2.imread('fullCONFIRM.png', cv2.IMREAD_UNCHANGED)
  needle_img = cv2.imread('CONFIRM.png', cv2.IMREAD_UNCHANGED)

  gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
  gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# perform template matching
  result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# find the coordinates of the best match
  min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
  top_left = max_loc

  cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)
  center_x = top_left[0] + (needle_img.shape[1] / 2)
  center_y = top_left[1] + (needle_img.shape[0] / 2)
  pyautogui.moveTo(center_x, center_y, duration=1.0)
  pydirectinput.click()
  pydirectinput.click()

   
  
else:
    # perform task if needle is not found
    print("Needle not found in haystack")


if i >= 2:
  # perform task
   pyautogui.moveTo(611 ,328, duration=1)
   main_window.right_click()
   time.sleep(5)



screenshot = pyautogui.screenshot()

haystack_img = cv2.imread('adjustfull.png', cv2.IMREAD_UNCHANGED)


# Read the needle image (the image you want to find within the haystack)
needle_img = cv2.imread('adjust.png', cv2.IMREAD_UNCHANGED)


screenshot_numpy = np.array(screenshot)
haystack_img = cv2.cvtColor(screenshot_numpy, cv2.COLOR_BGR2RGB)


# Convert the images to grayscale
gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# Use cv2.matchTemplate() to find the needle in the haystack
result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# Find the coordinates of the top-left corner of the best match
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc

# Draw a rectangle around the match
cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)



# Calculate the center of the match
center_x = top_left[0] + (needle_img.shape[1] / 2)
center_y = top_left[1] + (needle_img.shape[0] / 2)

# Move the mouse cursor to the center of the match
pyautogui.moveTo(center_x, center_y, duration=1.0)

main_window.right_click()
time.sleep(1)
screenshot = pyautogui.screenshot()

haystack_img = cv2.imread('comparefull.png', cv2.IMREAD_UNCHANGED)


# Read the needle image (the image you want to find within the haystack)
needle_img = cv2.imread('compare.png', cv2.IMREAD_UNCHANGED)


screenshot_numpy = np.array(screenshot)
haystack_img = cv2.cvtColor(screenshot_numpy, cv2.COLOR_BGR2RGB)


# Convert the images to grayscale
gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# Use cv2.matchTemplate() to find the needle in the haystack
result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# Find the coordinates of the top-left corner of the best match
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc

# Draw a rectangle around the match
cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)



# Calculate the center of the match
center_x = top_left[0] + (needle_img.shape[1] / 2)
center_y = top_left[1] + (needle_img.shape[0] / 2)

# Move the mouse cursor to the center of the match
pyautogui.moveTo(center_x, center_y, duration=1.0)
time.sleep(1)

x, y = pyautogui.position()
print("Mouse coordinates: ", x, y)
x = x
y = y 
import pyautogui
import pydirectinput
pydirectinput.moveTo(x, y)
pydirectinput.click()
pydirectinput.click()


time.sleep(2)
screenshot = pyautogui.screenshot()

haystack_img = cv2.imread('fullSEARCH.png', cv2.IMREAD_UNCHANGED)


# Read the needle image (the image you want to find within the haystack)
needle_img = cv2.imread('SREACH.png', cv2.IMREAD_UNCHANGED)


screenshot_numpy = np.array(screenshot)
haystack_img = cv2.cvtColor(screenshot_numpy, cv2.COLOR_BGR2RGB)


# Convert the images to grayscale
gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# Use cv2.matchTemplate() to find the needle in the haystack
result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# Find the coordinates of the top-left corner of the best match
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc

# Draw a rectangle around the match
cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)



# Calculate the center of the match
center_x = top_left[0] + (needle_img.shape[1] / 2)
center_y = top_left[1] + (needle_img.shape[0] / 2)

# Move the mouse cursor to the center of the match
pyautogui.moveTo(center_x, center_y, duration=1.0)
time.sleep(1)

pydirectinput.click()
pydirectinput.click()
time.sleep(1)
screenshot = pyautogui.screenshot()

haystack_img = cv2.imread('FullTEM.png', cv2.IMREAD_UNCHANGED)


# Read the needle image (the image you want to find within the haystack)
needle_img = cv2.imread('item.png', cv2.IMREAD_UNCHANGED)


screenshot_numpy = np.array(screenshot)
haystack_img = cv2.cvtColor(screenshot_numpy, cv2.COLOR_BGR2RGB)


# Convert the images to grayscale
gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# Use cv2.matchTemplate() to find the needle in the haystack
result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# Find the coordinates of the top-left corner of the best match
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc

# Draw a rectangle around the match
cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)



# Calculate the center of the match
center_x = top_left[0] + (needle_img.shape[1] / 2)
center_y = top_left[1] + (needle_img.shape[0] / 2)

# Move the mouse cursor to the center of the match
pyautogui.moveTo(center_x, center_y, duration=1.0)
time.sleep(1)

pydirectinput.click()
pydirectinput.click()

screenshot = pyautogui.screenshot()

haystack_img = cv2.imread('Fullsea.png', cv2.IMREAD_UNCHANGED)


# Read the needle image (the image you want to find within the haystack)
needle_img = cv2.imread('sea.png', cv2.IMREAD_UNCHANGED)


screenshot_numpy = np.array(screenshot)
haystack_img = cv2.cvtColor(screenshot_numpy, cv2.COLOR_BGR2RGB)


# Convert the images to grayscale
gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# Use cv2.matchTemplate() to find the needle in the haystack
result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# Find the coordinates of the top-left corner of the best match
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc

# Draw a rectangle around the match
cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)



# Calculate the center of the match
center_x = top_left[0] + (needle_img.shape[1] / 2)
center_y = top_left[1] + (needle_img.shape[0] / 2)

# Move the mouse cursor to the center of the match
pyautogui.moveTo(center_x, center_y, duration=1.0)
time.sleep(1)

pydirectinput.click()
pydirectinput.click()

# read the haystack and needle images
haystack_img = cv2.imread('FULLHQ.png', cv2.IMREAD_UNCHANGED)
needle_img = cv2.imread('HQ.png', cv2.IMREAD_UNCHANGED)

gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# perform template matching
result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# find the coordinates of the best match
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc

cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)

# center_x = top_left[0] + (needle_img.shape[1] / 2)
# center_y = top_left[1] + (needle_img.shape[0] / 2)

# check if the match is above a certain threshold
threshold = 0.8
if max_val > threshold:
  center_x = top_left[0] + (needle_img.shape[1] / 2)
  center_y = top_left[1] + (needle_img.shape[0] / 2)

  pyautogui.moveTo(center_x, center_y, duration=1.0)


  time.sleep(1)
  keyboard.press("alt")
  time.sleep(2)
  pyautogui.moveRel(0, 20)
  time.sleep(0.5)
  pyautogui.moveRel(200, 0)
  time.sleep(5)
  keyboard.release("alt")
  x, y = pyautogui.position()

  x = x 
  y = y
  print("Mouse coordinates: ", x, y)




  left, top, width, height = (x - 83, y - 17, 110, 30)
  screenshot = pyautogui.screenshot(region=(left, top, width, height))
  screenshot.save("p1.png")
# Take the screenshot
#   screenshot = ImageGrab.grab(bbox=(left, top, right, bottom))

# # Save the screenshot
#   screenshot.save("p1.png")

  img = cv2.imread('p1.png')

# Convert to grayscale
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Otsu threshold
  thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# Pass the image to tesseract OCR
  number_string = pytesseract.image_to_string(thresh, lang='eng', config='--psm 10')
  number_string = number_string.replace('—___—\n', '')
  number_string = number_string.replace('\n', '')

  number_int = int(number_string)


# Print the integer variable
  print(number_int)

  number_int -= 1
  print(number_int)
  time.sleep(3)
  haystack_img = cv2.imread('fullX.png', cv2.IMREAD_UNCHANGED)
  needle_img = cv2.imread('X.png', cv2.IMREAD_UNCHANGED)

  gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
  gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# perform template matching
  result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# find the coordinates of the best match
  min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
  top_left = max_loc

  cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)
  center_x = top_left[0] + (needle_img.shape[1] / 2)
  center_y = top_left[1] + (needle_img.shape[0] / 2)


# Move the mouse cursor to the center of the match
  pyautogui.moveTo(center_x, center_y, duration=1.0)
  pydirectinput.click()
  pydirectinput.click()
  haystack_img = cv2.imread('fullASK.png', cv2.IMREAD_UNCHANGED)
  needle_img = cv2.imread('ASK.png', cv2.IMREAD_UNCHANGED)

  gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
  gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# perform template matching
  result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# find the coordinates of the best match
  min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
  top_left = max_loc

  cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)
  center_x = top_left[0] + (needle_img.shape[1] / 2)
  center_y = top_left[1] + (needle_img.shape[0] / 2)


# Move the mouse cursor to the center of the match
  pyautogui.moveTo(center_x, center_y, duration=1.0)
  pyautogui.moveRel(100, 0)
  pydirectinput.click()
  time.sleep(1)
  keyboard.press("backspace")
  keyboard.release("backspace")
  time.sleep(1)
  pyautogui.typewrite(str(number_int))
  

  haystack_img = cv2.imread('fullCONFIRM.png', cv2.IMREAD_UNCHANGED)
  needle_img = cv2.imread('CONFIRM.png', cv2.IMREAD_UNCHANGED)

  gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
  gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# perform template matching
  result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# find the coordinates of the best match
  min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
  top_left = max_loc

  cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)
  center_x = top_left[0] + (needle_img.shape[1] / 2)
  center_y = top_left[1] + (needle_img.shape[0] / 2)
  pyautogui.moveTo(center_x, center_y, duration=1.0)
  pydirectinput.click()
  pydirectinput.click()

   
  
else:
    # perform task if needle is not found
    print("Needle not found in haystack")

if i >= 3:
#     # perform another task
 pyautogui.moveTo(543, 378, duration=1)
 main_window.right_click()
 time.sleep(5)



screenshot = pyautogui.screenshot()

haystack_img = cv2.imread('adjustfull.png', cv2.IMREAD_UNCHANGED)


# Read the needle image (the image you want to find within the haystack)
needle_img = cv2.imread('adjust.png', cv2.IMREAD_UNCHANGED)


screenshot_numpy = np.array(screenshot)
haystack_img = cv2.cvtColor(screenshot_numpy, cv2.COLOR_BGR2RGB)


# Convert the images to grayscale
gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# Use cv2.matchTemplate() to find the needle in the haystack
result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# Find the coordinates of the top-left corner of the best match
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc

# Draw a rectangle around the match
cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)



# Calculate the center of the match
center_x = top_left[0] + (needle_img.shape[1] / 2)
center_y = top_left[1] + (needle_img.shape[0] / 2)

# Move the mouse cursor to the center of the match
pyautogui.moveTo(center_x, center_y, duration=1.0)

main_window.right_click()
time.sleep(1)
screenshot = pyautogui.screenshot()

haystack_img = cv2.imread('comparefull.png', cv2.IMREAD_UNCHANGED)


# Read the needle image (the image you want to find within the haystack)
needle_img = cv2.imread('compare.png', cv2.IMREAD_UNCHANGED)


screenshot_numpy = np.array(screenshot)
haystack_img = cv2.cvtColor(screenshot_numpy, cv2.COLOR_BGR2RGB)


# Convert the images to grayscale
gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# Use cv2.matchTemplate() to find the needle in the haystack
result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# Find the coordinates of the top-left corner of the best match
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc

# Draw a rectangle around the match
cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)



# Calculate the center of the match
center_x = top_left[0] + (needle_img.shape[1] / 2)
center_y = top_left[1] + (needle_img.shape[0] / 2)

# Move the mouse cursor to the center of the match
pyautogui.moveTo(center_x, center_y, duration=1.0)
time.sleep(1)

x, y = pyautogui.position()
print("Mouse coordinates: ", x, y)
x = x
y = y 
import pyautogui
import pydirectinput
pydirectinput.moveTo(x, y)
pydirectinput.click()
pydirectinput.click()


time.sleep(2)
screenshot = pyautogui.screenshot()

haystack_img = cv2.imread('fullSEARCH.png', cv2.IMREAD_UNCHANGED)


# Read the needle image (the image you want to find within the haystack)
needle_img = cv2.imread('SREACH.png', cv2.IMREAD_UNCHANGED)


screenshot_numpy = np.array(screenshot)
haystack_img = cv2.cvtColor(screenshot_numpy, cv2.COLOR_BGR2RGB)


# Convert the images to grayscale
gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# Use cv2.matchTemplate() to find the needle in the haystack
result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# Find the coordinates of the top-left corner of the best match
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc

# Draw a rectangle around the match
cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)



# Calculate the center of the match
center_x = top_left[0] + (needle_img.shape[1] / 2)
center_y = top_left[1] + (needle_img.shape[0] / 2)

# Move the mouse cursor to the center of the match
pyautogui.moveTo(center_x, center_y, duration=1.0)
time.sleep(1)

pydirectinput.click()
pydirectinput.click()
time.sleep(1)
screenshot = pyautogui.screenshot()

haystack_img = cv2.imread('FullTEM.png', cv2.IMREAD_UNCHANGED)


# Read the needle image (the image you want to find within the haystack)
needle_img = cv2.imread('item.png', cv2.IMREAD_UNCHANGED)


screenshot_numpy = np.array(screenshot)
haystack_img = cv2.cvtColor(screenshot_numpy, cv2.COLOR_BGR2RGB)


# Convert the images to grayscale
gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# Use cv2.matchTemplate() to find the needle in the haystack
result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# Find the coordinates of the top-left corner of the best match
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc

# Draw a rectangle around the match
cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)



# Calculate the center of the match
center_x = top_left[0] + (needle_img.shape[1] / 2)
center_y = top_left[1] + (needle_img.shape[0] / 2)

# Move the mouse cursor to the center of the match
pyautogui.moveTo(center_x, center_y, duration=1.0)
time.sleep(1)

pydirectinput.click()
pydirectinput.click()

screenshot = pyautogui.screenshot()

haystack_img = cv2.imread('Fullsea.png', cv2.IMREAD_UNCHANGED)


# Read the needle image (the image you want to find within the haystack)
needle_img = cv2.imread('sea.png', cv2.IMREAD_UNCHANGED)


screenshot_numpy = np.array(screenshot)
haystack_img = cv2.cvtColor(screenshot_numpy, cv2.COLOR_BGR2RGB)


# Convert the images to grayscale
gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# Use cv2.matchTemplate() to find the needle in the haystack
result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# Find the coordinates of the top-left corner of the best match
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc

# Draw a rectangle around the match
cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)



# Calculate the center of the match
center_x = top_left[0] + (needle_img.shape[1] / 2)
center_y = top_left[1] + (needle_img.shape[0] / 2)

# Move the mouse cursor to the center of the match
pyautogui.moveTo(center_x, center_y, duration=1.0)
time.sleep(1)

pydirectinput.click()
pydirectinput.click()

# read the haystack and needle images
haystack_img = cv2.imread('FULLHQ.png', cv2.IMREAD_UNCHANGED)
needle_img = cv2.imread('HQ.png', cv2.IMREAD_UNCHANGED)

gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# perform template matching
result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# find the coordinates of the best match
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc

cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)

# center_x = top_left[0] + (needle_img.shape[1] / 2)
# center_y = top_left[1] + (needle_img.shape[0] / 2)

# check if the match is above a certain threshold
threshold = 0.8
if max_val > threshold:
  center_x = top_left[0] + (needle_img.shape[1] / 2)
  center_y = top_left[1] + (needle_img.shape[0] / 2)

  pyautogui.moveTo(center_x, center_y, duration=1.0)


  time.sleep(1)
  keyboard.press("alt")
  time.sleep(2)
  pyautogui.moveRel(0, 20)
  time.sleep(0.5)
  pyautogui.moveRel(200, 0)
  time.sleep(5)
  keyboard.release("alt")
  x, y = pyautogui.position()

  x = x 
  y = y
  print("Mouse coordinates: ", x, y)




  left, top, width, height = (x - 83, y - 17, 110, 30)
  screenshot = pyautogui.screenshot(region=(left, top, width, height))
  screenshot.save("p1.png")
# Take the screenshot
#   screenshot = ImageGrab.grab(bbox=(left, top, right, bottom))

# # Save the screenshot
#   screenshot.save("p1.png")

  img = cv2.imread('p1.png')

# Convert to grayscale
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Otsu threshold
  thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# Pass the image to tesseract OCR
  number_string = pytesseract.image_to_string(thresh, lang='eng', config='--psm 10')
  number_string = number_string.replace('—___—\n', '')
  number_string = number_string.replace('\n', '')

  number_int = int(number_string)


# Print the integer variable
  print(number_int)

  number_int -= 1
  print(number_int)
  time.sleep(3)
  haystack_img = cv2.imread('fullX.png', cv2.IMREAD_UNCHANGED)
  needle_img = cv2.imread('X.png', cv2.IMREAD_UNCHANGED)

  gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
  gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# perform template matching
  result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# find the coordinates of the best match
  min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
  top_left = max_loc

  cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)
  center_x = top_left[0] + (needle_img.shape[1] / 2)
  center_y = top_left[1] + (needle_img.shape[0] / 2)


# Move the mouse cursor to the center of the match
  pyautogui.moveTo(center_x, center_y, duration=1.0)
  pydirectinput.click()
  pydirectinput.click()
  haystack_img = cv2.imread('fullASK.png', cv2.IMREAD_UNCHANGED)
  needle_img = cv2.imread('ASK.png', cv2.IMREAD_UNCHANGED)

  gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
  gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# perform template matching
  result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# find the coordinates of the best match
  min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
  top_left = max_loc

  cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)
  center_x = top_left[0] + (needle_img.shape[1] / 2)
  center_y = top_left[1] + (needle_img.shape[0] / 2)


# Move the mouse cursor to the center of the match
  pyautogui.moveTo(center_x, center_y, duration=1.0)
  pyautogui.moveRel(100, 0)
  pydirectinput.click()
  time.sleep(1)
  keyboard.press("backspace")
  keyboard.release("backspace")
  time.sleep(1)
  pyautogui.typewrite(str(number_int))
  

  haystack_img = cv2.imread('fullCONFIRM.png', cv2.IMREAD_UNCHANGED)
  needle_img = cv2.imread('CONFIRM.png', cv2.IMREAD_UNCHANGED)

  gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
  gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# perform template matching
  result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# find the coordinates of the best match
  min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
  top_left = max_loc

  cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)
  center_x = top_left[0] + (needle_img.shape[1] / 2)
  center_y = top_left[1] + (needle_img.shape[0] / 2)
  pyautogui.moveTo(center_x, center_y, duration=1.0)
  pydirectinput.click()
  pydirectinput.click()

   
  
else:
    # perform task if needle is not found
    print("Needle not found in haystack")

if i >= 4: 
  pyautogui.moveTo(634, 402, duration=1)
  main_window.right_click()
  time.sleep(5)



screenshot = pyautogui.screenshot()

haystack_img = cv2.imread('adjustfull.png', cv2.IMREAD_UNCHANGED)


# Read the needle image (the image you want to find within the haystack)
needle_img = cv2.imread('adjust.png', cv2.IMREAD_UNCHANGED)


screenshot_numpy = np.array(screenshot)
haystack_img = cv2.cvtColor(screenshot_numpy, cv2.COLOR_BGR2RGB)


# Convert the images to grayscale
gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# Use cv2.matchTemplate() to find the needle in the haystack
result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# Find the coordinates of the top-left corner of the best match
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc

# Draw a rectangle around the match
cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)



# Calculate the center of the match
center_x = top_left[0] + (needle_img.shape[1] / 2)
center_y = top_left[1] + (needle_img.shape[0] / 2)

# Move the mouse cursor to the center of the match
pyautogui.moveTo(center_x, center_y, duration=1.0)

main_window.right_click()
time.sleep(1)
screenshot = pyautogui.screenshot()

haystack_img = cv2.imread('comparefull.png', cv2.IMREAD_UNCHANGED)


# Read the needle image (the image you want to find within the haystack)
needle_img = cv2.imread('compare.png', cv2.IMREAD_UNCHANGED)


screenshot_numpy = np.array(screenshot)
haystack_img = cv2.cvtColor(screenshot_numpy, cv2.COLOR_BGR2RGB)


# Convert the images to grayscale
gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# Use cv2.matchTemplate() to find the needle in the haystack
result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# Find the coordinates of the top-left corner of the best match
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc

# Draw a rectangle around the match
cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)



# Calculate the center of the match
center_x = top_left[0] + (needle_img.shape[1] / 2)
center_y = top_left[1] + (needle_img.shape[0] / 2)

# Move the mouse cursor to the center of the match
pyautogui.moveTo(center_x, center_y, duration=1.0)
time.sleep(1)

x, y = pyautogui.position()
print("Mouse coordinates: ", x, y)
x = x
y = y 
import pyautogui
import pydirectinput
pydirectinput.moveTo(x, y)
pydirectinput.click()
pydirectinput.click()


time.sleep(2)
screenshot = pyautogui.screenshot()

haystack_img = cv2.imread('fullSEARCH.png', cv2.IMREAD_UNCHANGED)


# Read the needle image (the image you want to find within the haystack)
needle_img = cv2.imread('SREACH.png', cv2.IMREAD_UNCHANGED)


screenshot_numpy = np.array(screenshot)
haystack_img = cv2.cvtColor(screenshot_numpy, cv2.COLOR_BGR2RGB)


# Convert the images to grayscale
gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# Use cv2.matchTemplate() to find the needle in the haystack
result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# Find the coordinates of the top-left corner of the best match
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc

# Draw a rectangle around the match
cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)



# Calculate the center of the match
center_x = top_left[0] + (needle_img.shape[1] / 2)
center_y = top_left[1] + (needle_img.shape[0] / 2)

# Move the mouse cursor to the center of the match
pyautogui.moveTo(center_x, center_y, duration=1.0)
time.sleep(1)

pydirectinput.click()
pydirectinput.click()
time.sleep(1)
screenshot = pyautogui.screenshot()

haystack_img = cv2.imread('FullTEM.png', cv2.IMREAD_UNCHANGED)


# Read the needle image (the image you want to find within the haystack)
needle_img = cv2.imread('item.png', cv2.IMREAD_UNCHANGED)


screenshot_numpy = np.array(screenshot)
haystack_img = cv2.cvtColor(screenshot_numpy, cv2.COLOR_BGR2RGB)


# Convert the images to grayscale
gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# Use cv2.matchTemplate() to find the needle in the haystack
result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# Find the coordinates of the top-left corner of the best match
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc

# Draw a rectangle around the match
cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)



# Calculate the center of the match
center_x = top_left[0] + (needle_img.shape[1] / 2)
center_y = top_left[1] + (needle_img.shape[0] / 2)

# Move the mouse cursor to the center of the match
pyautogui.moveTo(center_x, center_y, duration=1.0)
time.sleep(1)

pydirectinput.click()
pydirectinput.click()

screenshot = pyautogui.screenshot()

haystack_img = cv2.imread('Fullsea.png', cv2.IMREAD_UNCHANGED)


# Read the needle image (the image you want to find within the haystack)
needle_img = cv2.imread('sea.png', cv2.IMREAD_UNCHANGED)


screenshot_numpy = np.array(screenshot)
haystack_img = cv2.cvtColor(screenshot_numpy, cv2.COLOR_BGR2RGB)


# Convert the images to grayscale
gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# Use cv2.matchTemplate() to find the needle in the haystack
result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# Find the coordinates of the top-left corner of the best match
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc

# Draw a rectangle around the match
cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)



# Calculate the center of the match
center_x = top_left[0] + (needle_img.shape[1] / 2)
center_y = top_left[1] + (needle_img.shape[0] / 2)

# Move the mouse cursor to the center of the match
pyautogui.moveTo(center_x, center_y, duration=1.0)
time.sleep(1)

pydirectinput.click()
pydirectinput.click()

# read the haystack and needle images
haystack_img = cv2.imread('FULLHQ.png', cv2.IMREAD_UNCHANGED)
needle_img = cv2.imread('HQ.png', cv2.IMREAD_UNCHANGED)

gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# perform template matching
result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# find the coordinates of the best match
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc

cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)

# center_x = top_left[0] + (needle_img.shape[1] / 2)
# center_y = top_left[1] + (needle_img.shape[0] / 2)

# check if the match is above a certain threshold
threshold = 0.8
if max_val > threshold:
  center_x = top_left[0] + (needle_img.shape[1] / 2)
  center_y = top_left[1] + (needle_img.shape[0] / 2)

  pyautogui.moveTo(center_x, center_y, duration=1.0)


  time.sleep(1)
  keyboard.press("alt")
  time.sleep(2)
  pyautogui.moveRel(0, 20)
  time.sleep(0.5)
  pyautogui.moveRel(200, 0)
  time.sleep(5)
  keyboard.release("alt")
  x, y = pyautogui.position()

  x = x 
  y = y
  print("Mouse coordinates: ", x, y)




  left, top, width, height = (x - 83, y - 17, 110, 30)
  screenshot = pyautogui.screenshot(region=(left, top, width, height))
  screenshot.save("p1.png")
# Take the screenshot
#   screenshot = ImageGrab.grab(bbox=(left, top, right, bottom))

# # Save the screenshot
#   screenshot.save("p1.png")

  img = cv2.imread('p1.png')

# Convert to grayscale
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Otsu threshold
  thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# Pass the image to tesseract OCR
  number_string = pytesseract.image_to_string(thresh, lang='eng', config='--psm 10')
  number_string = number_string.replace('—___—\n', '')
  number_string = number_string.replace('\n', '')

  number_int = int(number_string)


# Print the integer variable
  print(number_int)

  number_int -= 1
  print(number_int)
  time.sleep(3)
  haystack_img = cv2.imread('fullX.png', cv2.IMREAD_UNCHANGED)
  needle_img = cv2.imread('X.png', cv2.IMREAD_UNCHANGED)

  gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
  gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# perform template matching
  result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# find the coordinates of the best match
  min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
  top_left = max_loc

  cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)
  center_x = top_left[0] + (needle_img.shape[1] / 2)
  center_y = top_left[1] + (needle_img.shape[0] / 2)


# Move the mouse cursor to the center of the match
  pyautogui.moveTo(center_x, center_y, duration=1.0)
  pydirectinput.click()
  pydirectinput.click()
  haystack_img = cv2.imread('fullASK.png', cv2.IMREAD_UNCHANGED)
  needle_img = cv2.imread('ASK.png', cv2.IMREAD_UNCHANGED)

  gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
  gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# perform template matching
  result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# find the coordinates of the best match
  min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
  top_left = max_loc

  cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)
  center_x = top_left[0] + (needle_img.shape[1] / 2)
  center_y = top_left[1] + (needle_img.shape[0] / 2)


# Move the mouse cursor to the center of the match
  pyautogui.moveTo(center_x, center_y, duration=1.0)
  pyautogui.moveRel(100, 0)
  pydirectinput.click()
  time.sleep(1)
  keyboard.press("backspace")
  keyboard.release("backspace")
  time.sleep(1)
  pyautogui.typewrite(str(number_int))
  

  haystack_img = cv2.imread('fullCONFIRM.png', cv2.IMREAD_UNCHANGED)
  needle_img = cv2.imread('CONFIRM.png', cv2.IMREAD_UNCHANGED)

  gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
  gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# perform template matching
  result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# find the coordinates of the best match
  min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
  top_left = max_loc

  cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)
  center_x = top_left[0] + (needle_img.shape[1] / 2)
  center_y = top_left[1] + (needle_img.shape[0] / 2)
  pyautogui.moveTo(center_x, center_y, duration=1.0)
  pydirectinput.click()
  pydirectinput.click()

   
  
if i >= 5: 
  pyautogui.moveTo(627, 443, duration=1)
  main_window.right_click()
  time.sleep(5)



screenshot = pyautogui.screenshot()

haystack_img = cv2.imread('adjustfull.png', cv2.IMREAD_UNCHANGED)


# Read the needle image (the image you want to find within the haystack)
needle_img = cv2.imread('adjust.png', cv2.IMREAD_UNCHANGED)


screenshot_numpy = np.array(screenshot)
haystack_img = cv2.cvtColor(screenshot_numpy, cv2.COLOR_BGR2RGB)


# Convert the images to grayscale
gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# Use cv2.matchTemplate() to find the needle in the haystack
result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# Find the coordinates of the top-left corner of the best match
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc

# Draw a rectangle around the match
cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)



# Calculate the center of the match
center_x = top_left[0] + (needle_img.shape[1] / 2)
center_y = top_left[1] + (needle_img.shape[0] / 2)

# Move the mouse cursor to the center of the match
pyautogui.moveTo(center_x, center_y, duration=1.0)

main_window.right_click()
time.sleep(1)
screenshot = pyautogui.screenshot()

haystack_img = cv2.imread('comparefull.png', cv2.IMREAD_UNCHANGED)


# Read the needle image (the image you want to find within the haystack)
needle_img = cv2.imread('compare.png', cv2.IMREAD_UNCHANGED)


screenshot_numpy = np.array(screenshot)
haystack_img = cv2.cvtColor(screenshot_numpy, cv2.COLOR_BGR2RGB)


# Convert the images to grayscale
gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# Use cv2.matchTemplate() to find the needle in the haystack
result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# Find the coordinates of the top-left corner of the best match
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc

# Draw a rectangle around the match
cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)



# Calculate the center of the match
center_x = top_left[0] + (needle_img.shape[1] / 2)
center_y = top_left[1] + (needle_img.shape[0] / 2)

# Move the mouse cursor to the center of the match
pyautogui.moveTo(center_x, center_y, duration=1.0)
time.sleep(1)

x, y = pyautogui.position()
print("Mouse coordinates: ", x, y)
x = x
y = y 
import pyautogui
import pydirectinput
pydirectinput.moveTo(x, y)
pydirectinput.click()
pydirectinput.click()


time.sleep(2)
screenshot = pyautogui.screenshot()

haystack_img = cv2.imread('fullSEARCH.png', cv2.IMREAD_UNCHANGED)


# Read the needle image (the image you want to find within the haystack)
needle_img = cv2.imread('SREACH.png', cv2.IMREAD_UNCHANGED)


screenshot_numpy = np.array(screenshot)
haystack_img = cv2.cvtColor(screenshot_numpy, cv2.COLOR_BGR2RGB)


# Convert the images to grayscale
gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# Use cv2.matchTemplate() to find the needle in the haystack
result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# Find the coordinates of the top-left corner of the best match
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc

# Draw a rectangle around the match
cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)



# Calculate the center of the match
center_x = top_left[0] + (needle_img.shape[1] / 2)
center_y = top_left[1] + (needle_img.shape[0] / 2)

# Move the mouse cursor to the center of the match
pyautogui.moveTo(center_x, center_y, duration=1.0)
time.sleep(1)

pydirectinput.click()
pydirectinput.click()
time.sleep(1)
screenshot = pyautogui.screenshot()

haystack_img = cv2.imread('FullTEM.png', cv2.IMREAD_UNCHANGED)


# Read the needle image (the image you want to find within the haystack)
needle_img = cv2.imread('item.png', cv2.IMREAD_UNCHANGED)


screenshot_numpy = np.array(screenshot)
haystack_img = cv2.cvtColor(screenshot_numpy, cv2.COLOR_BGR2RGB)


# Convert the images to grayscale
gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# Use cv2.matchTemplate() to find the needle in the haystack
result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# Find the coordinates of the top-left corner of the best match
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc

# Draw a rectangle around the match
cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)



# Calculate the center of the match
center_x = top_left[0] + (needle_img.shape[1] / 2)
center_y = top_left[1] + (needle_img.shape[0] / 2)

# Move the mouse cursor to the center of the match
pyautogui.moveTo(center_x, center_y, duration=1.0)
time.sleep(1)

pydirectinput.click()
pydirectinput.click()

screenshot = pyautogui.screenshot()

haystack_img = cv2.imread('Fullsea.png', cv2.IMREAD_UNCHANGED)


# Read the needle image (the image you want to find within the haystack)
needle_img = cv2.imread('sea.png', cv2.IMREAD_UNCHANGED)


screenshot_numpy = np.array(screenshot)
haystack_img = cv2.cvtColor(screenshot_numpy, cv2.COLOR_BGR2RGB)


# Convert the images to grayscale
gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# Use cv2.matchTemplate() to find the needle in the haystack
result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# Find the coordinates of the top-left corner of the best match
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc

# Draw a rectangle around the match
cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)



# Calculate the center of the match
center_x = top_left[0] + (needle_img.shape[1] / 2)
center_y = top_left[1] + (needle_img.shape[0] / 2)

# Move the mouse cursor to the center of the match
pyautogui.moveTo(center_x, center_y, duration=1.0)
time.sleep(1)

pydirectinput.click()
pydirectinput.click()

# read the haystack and needle images
haystack_img = cv2.imread('FULLHQ.png', cv2.IMREAD_UNCHANGED)
needle_img = cv2.imread('HQ.png', cv2.IMREAD_UNCHANGED)

gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# perform template matching
result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# find the coordinates of the best match
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc

cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)

# center_x = top_left[0] + (needle_img.shape[1] / 2)
# center_y = top_left[1] + (needle_img.shape[0] / 2)

# check if the match is above a certain threshold
threshold = 0.8
if max_val > threshold:
  center_x = top_left[0] + (needle_img.shape[1] / 2)
  center_y = top_left[1] + (needle_img.shape[0] / 2)

  pyautogui.moveTo(center_x, center_y, duration=1.0)


  time.sleep(1)
  keyboard.press("alt")
  time.sleep(2)
  pyautogui.moveRel(0, 20)
  time.sleep(0.5)
  pyautogui.moveRel(200, 0)
  time.sleep(5)
  keyboard.release("alt")
  x, y = pyautogui.position()

  x = x 
  y = y
  print("Mouse coordinates: ", x, y)




  left, top, width, height = (x - 83, y - 17, 110, 30)
  screenshot = pyautogui.screenshot(region=(left, top, width, height))
  screenshot.save("p1.png")
# Take the screenshot
#   screenshot = ImageGrab.grab(bbox=(left, top, right, bottom))

# # Save the screenshot
#   screenshot.save("p1.png")

  img = cv2.imread('p1.png')

# Convert to grayscale
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Otsu threshold
  thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# Pass the image to tesseract OCR
  number_string = pytesseract.image_to_string(thresh, lang='eng', config='--psm 10')
  number_string = number_string.replace('—___—\n', '')
  number_string = number_string.replace('\n', '')

  number_int = int(number_string)


# Print the integer variable
  print(number_int)

  number_int -= 1
  print(number_int)
  time.sleep(3)
  haystack_img = cv2.imread('fullX.png', cv2.IMREAD_UNCHANGED)
  needle_img = cv2.imread('X.png', cv2.IMREAD_UNCHANGED)

  gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
  gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# perform template matching
  result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# find the coordinates of the best match
  min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
  top_left = max_loc

  cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)
  center_x = top_left[0] + (needle_img.shape[1] / 2)
  center_y = top_left[1] + (needle_img.shape[0] / 2)


# Move the mouse cursor to the center of the match
  pyautogui.moveTo(center_x, center_y, duration=1.0)
  pydirectinput.click()
  pydirectinput.click()
  haystack_img = cv2.imread('fullASK.png', cv2.IMREAD_UNCHANGED)
  needle_img = cv2.imread('ASK.png', cv2.IMREAD_UNCHANGED)

  gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
  gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# perform template matching
  result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# find the coordinates of the best match
  min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
  top_left = max_loc

  cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)
  center_x = top_left[0] + (needle_img.shape[1] / 2)
  center_y = top_left[1] + (needle_img.shape[0] / 2)


# Move the mouse cursor to the center of the match
  pyautogui.moveTo(center_x, center_y, duration=1.0)
  pyautogui.moveRel(100, 0)
  pydirectinput.click()
  time.sleep(1)
  keyboard.press("backspace")
  keyboard.release("backspace")
  time.sleep(1)
  pyautogui.typewrite(str(number_int))
  

  haystack_img = cv2.imread('fullCONFIRM.png', cv2.IMREAD_UNCHANGED)
  needle_img = cv2.imread('CONFIRM.png', cv2.IMREAD_UNCHANGED)

  gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
  gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# perform template matching
  result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# find the coordinates of the best match
  min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
  top_left = max_loc

  cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)
  center_x = top_left[0] + (needle_img.shape[1] / 2)
  center_y = top_left[1] + (needle_img.shape[0] / 2)
  pyautogui.moveTo(center_x, center_y, duration=1.0)
  pydirectinput.click()
  pydirectinput.click()

   
  
else:
    # perform task if needle is not found
    print("Needle not found in haystack")
if i >= 6:
  pyautogui.moveTo(554, 492, duration=1)
  main_window.right_click()
  time.sleep(5)



screenshot = pyautogui.screenshot()

haystack_img = cv2.imread('adjustfull.png', cv2.IMREAD_UNCHANGED)


# Read the needle image (the image you want to find within the haystack)
needle_img = cv2.imread('adjust.png', cv2.IMREAD_UNCHANGED)


screenshot_numpy = np.array(screenshot)
haystack_img = cv2.cvtColor(screenshot_numpy, cv2.COLOR_BGR2RGB)


# Convert the images to grayscale
gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# Use cv2.matchTemplate() to find the needle in the haystack
result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# Find the coordinates of the top-left corner of the best match
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc

# Draw a rectangle around the match
cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)



# Calculate the center of the match
center_x = top_left[0] + (needle_img.shape[1] / 2)
center_y = top_left[1] + (needle_img.shape[0] / 2)

# Move the mouse cursor to the center of the match
pyautogui.moveTo(center_x, center_y, duration=1.0)

main_window.right_click()
time.sleep(1)
screenshot = pyautogui.screenshot()

haystack_img = cv2.imread('comparefull.png', cv2.IMREAD_UNCHANGED)


# Read the needle image (the image you want to find within the haystack)
needle_img = cv2.imread('compare.png', cv2.IMREAD_UNCHANGED)


screenshot_numpy = np.array(screenshot)
haystack_img = cv2.cvtColor(screenshot_numpy, cv2.COLOR_BGR2RGB)


# Convert the images to grayscale
gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# Use cv2.matchTemplate() to find the needle in the haystack
result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# Find the coordinates of the top-left corner of the best match
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc

# Draw a rectangle around the match
cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)



# Calculate the center of the match
center_x = top_left[0] + (needle_img.shape[1] / 2)
center_y = top_left[1] + (needle_img.shape[0] / 2)

# Move the mouse cursor to the center of the match
pyautogui.moveTo(center_x, center_y, duration=1.0)
time.sleep(1)

x, y = pyautogui.position()
print("Mouse coordinates: ", x, y)
x = x
y = y 
import pyautogui
import pydirectinput
pydirectinput.moveTo(x, y)
pydirectinput.click()
pydirectinput.click()


time.sleep(2)
screenshot = pyautogui.screenshot()

haystack_img = cv2.imread('fullSEARCH.png', cv2.IMREAD_UNCHANGED)


# Read the needle image (the image you want to find within the haystack)
needle_img = cv2.imread('SREACH.png', cv2.IMREAD_UNCHANGED)


screenshot_numpy = np.array(screenshot)
haystack_img = cv2.cvtColor(screenshot_numpy, cv2.COLOR_BGR2RGB)


# Convert the images to grayscale
gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# Use cv2.matchTemplate() to find the needle in the haystack
result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# Find the coordinates of the top-left corner of the best match
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc

# Draw a rectangle around the match
cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)



# Calculate the center of the match
center_x = top_left[0] + (needle_img.shape[1] / 2)
center_y = top_left[1] + (needle_img.shape[0] / 2)

# Move the mouse cursor to the center of the match
pyautogui.moveTo(center_x, center_y, duration=1.0)
time.sleep(1)

pydirectinput.click()
pydirectinput.click()
time.sleep(1)
screenshot = pyautogui.screenshot()

haystack_img = cv2.imread('FullTEM.png', cv2.IMREAD_UNCHANGED)


# Read the needle image (the image you want to find within the haystack)
needle_img = cv2.imread('item.png', cv2.IMREAD_UNCHANGED)


screenshot_numpy = np.array(screenshot)
haystack_img = cv2.cvtColor(screenshot_numpy, cv2.COLOR_BGR2RGB)


# Convert the images to grayscale
gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# Use cv2.matchTemplate() to find the needle in the haystack
result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# Find the coordinates of the top-left corner of the best match
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc

# Draw a rectangle around the match
cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)



# Calculate the center of the match
center_x = top_left[0] + (needle_img.shape[1] / 2)
center_y = top_left[1] + (needle_img.shape[0] / 2)

# Move the mouse cursor to the center of the match
pyautogui.moveTo(center_x, center_y, duration=1.0)
time.sleep(1)

pydirectinput.click()
pydirectinput.click()

screenshot = pyautogui.screenshot()

haystack_img = cv2.imread('Fullsea.png', cv2.IMREAD_UNCHANGED)


# Read the needle image (the image you want to find within the haystack)
needle_img = cv2.imread('sea.png', cv2.IMREAD_UNCHANGED)


screenshot_numpy = np.array(screenshot)
haystack_img = cv2.cvtColor(screenshot_numpy, cv2.COLOR_BGR2RGB)


# Convert the images to grayscale
gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# Use cv2.matchTemplate() to find the needle in the haystack
result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# Find the coordinates of the top-left corner of the best match
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc

# Draw a rectangle around the match
cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)



# Calculate the center of the match
center_x = top_left[0] + (needle_img.shape[1] / 2)
center_y = top_left[1] + (needle_img.shape[0] / 2)

# Move the mouse cursor to the center of the match
pyautogui.moveTo(center_x, center_y, duration=1.0)
time.sleep(1)

pydirectinput.click()
pydirectinput.click()

# read the haystack and needle images
haystack_img = cv2.imread('FULLHQ.png', cv2.IMREAD_UNCHANGED)
needle_img = cv2.imread('HQ.png', cv2.IMREAD_UNCHANGED)

gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# perform template matching
result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# find the coordinates of the best match
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc

cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)

# center_x = top_left[0] + (needle_img.shape[1] / 2)
# center_y = top_left[1] + (needle_img.shape[0] / 2)

# check if the match is above a certain threshold
threshold = 0.8
if max_val > threshold:
  center_x = top_left[0] + (needle_img.shape[1] / 2)
  center_y = top_left[1] + (needle_img.shape[0] / 2)

  pyautogui.moveTo(center_x, center_y, duration=1.0)


  time.sleep(1)
  keyboard.press("alt")
  time.sleep(2)
  pyautogui.moveRel(0, 20)
  time.sleep(0.5)
  pyautogui.moveRel(200, 0)
  time.sleep(5)
  keyboard.release("alt")
  x, y = pyautogui.position()

  x = x 
  y = y
  print("Mouse coordinates: ", x, y)




  left, top, width, height = (x - 83, y - 17, 110, 30)
  screenshot = pyautogui.screenshot(region=(left, top, width, height))
  screenshot.save("p1.png")
# Take the screenshot
#   screenshot = ImageGrab.grab(bbox=(left, top, right, bottom))

# # Save the screenshot
#   screenshot.save("p1.png")

  img = cv2.imread('p1.png')

# Convert to grayscale
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Otsu threshold
  thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# Pass the image to tesseract OCR
  number_string = pytesseract.image_to_string(thresh, lang='eng', config='--psm 10')
  number_string = number_string.replace('—___—\n', '')
  number_string = number_string.replace('\n', '')

  number_int = int(number_string)


# Print the integer variable
  print(number_int)

  number_int -= 1
  print(number_int)
  time.sleep(3)
  haystack_img = cv2.imread('fullX.png', cv2.IMREAD_UNCHANGED)
  needle_img = cv2.imread('X.png', cv2.IMREAD_UNCHANGED)

  gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
  gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# perform template matching
  result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# find the coordinates of the best match
  min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
  top_left = max_loc

  cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)
  center_x = top_left[0] + (needle_img.shape[1] / 2)
  center_y = top_left[1] + (needle_img.shape[0] / 2)


# Move the mouse cursor to the center of the match
  pyautogui.moveTo(center_x, center_y, duration=1.0)
  pydirectinput.click()
  pydirectinput.click()
  haystack_img = cv2.imread('fullASK.png', cv2.IMREAD_UNCHANGED)
  needle_img = cv2.imread('ASK.png', cv2.IMREAD_UNCHANGED)

  gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
  gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# perform template matching
  result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# find the coordinates of the best match
  min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
  top_left = max_loc

  cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)
  center_x = top_left[0] + (needle_img.shape[1] / 2)
  center_y = top_left[1] + (needle_img.shape[0] / 2)


# Move the mouse cursor to the center of the match
  pyautogui.moveTo(center_x, center_y, duration=1.0)
  pyautogui.moveRel(100, 0)
  pydirectinput.click()
  time.sleep(1)
  keyboard.press("backspace")
  keyboard.release("backspace")
  time.sleep(1)
  pyautogui.typewrite(str(number_int))
  

  haystack_img = cv2.imread('fullCONFIRM.png', cv2.IMREAD_UNCHANGED)
  needle_img = cv2.imread('CONFIRM.png', cv2.IMREAD_UNCHANGED)

  gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
  gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# perform template matching
  result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# find the coordinates of the best match
  min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
  top_left = max_loc

  cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)
  center_x = top_left[0] + (needle_img.shape[1] / 2)
  center_y = top_left[1] + (needle_img.shape[0] / 2)
  pyautogui.moveTo(center_x, center_y, duration=1.0)
  pydirectinput.click()
  pydirectinput.click()

   
  
else:
    # perform task if needle is not found
    print("Needle not found in haystack")
if i>= 7:
  pyautogui.moveTo(618, 523 , duration=1)
  main_window.right_click()
  time.sleep(5)



screenshot = pyautogui.screenshot()

haystack_img = cv2.imread('adjustfull.png', cv2.IMREAD_UNCHANGED)


# Read the needle image (the image you want to find within the haystack)
needle_img = cv2.imread('adjust.png', cv2.IMREAD_UNCHANGED)


screenshot_numpy = np.array(screenshot)
haystack_img = cv2.cvtColor(screenshot_numpy, cv2.COLOR_BGR2RGB)


# Convert the images to grayscale
gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# Use cv2.matchTemplate() to find the needle in the haystack
result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# Find the coordinates of the top-left corner of the best match
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc

# Draw a rectangle around the match
cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)



# Calculate the center of the match
center_x = top_left[0] + (needle_img.shape[1] / 2)
center_y = top_left[1] + (needle_img.shape[0] / 2)

# Move the mouse cursor to the center of the match
pyautogui.moveTo(center_x, center_y, duration=1.0)

main_window.right_click()
time.sleep(1)
screenshot = pyautogui.screenshot()

haystack_img = cv2.imread('comparefull.png', cv2.IMREAD_UNCHANGED)


# Read the needle image (the image you want to find within the haystack)
needle_img = cv2.imread('compare.png', cv2.IMREAD_UNCHANGED)


screenshot_numpy = np.array(screenshot)
haystack_img = cv2.cvtColor(screenshot_numpy, cv2.COLOR_BGR2RGB)


# Convert the images to grayscale
gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# Use cv2.matchTemplate() to find the needle in the haystack
result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# Find the coordinates of the top-left corner of the best match
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc

# Draw a rectangle around the match
cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)



# Calculate the center of the match
center_x = top_left[0] + (needle_img.shape[1] / 2)
center_y = top_left[1] + (needle_img.shape[0] / 2)

# Move the mouse cursor to the center of the match
pyautogui.moveTo(center_x, center_y, duration=1.0)
time.sleep(1)

x, y = pyautogui.position()
print("Mouse coordinates: ", x, y)
x = x
y = y 
import pyautogui
import pydirectinput
pydirectinput.moveTo(x, y)
pydirectinput.click()
pydirectinput.click()


time.sleep(2)
screenshot = pyautogui.screenshot()

haystack_img = cv2.imread('fullSEARCH.png', cv2.IMREAD_UNCHANGED)


# Read the needle image (the image you want to find within the haystack)
needle_img = cv2.imread('SREACH.png', cv2.IMREAD_UNCHANGED)


screenshot_numpy = np.array(screenshot)
haystack_img = cv2.cvtColor(screenshot_numpy, cv2.COLOR_BGR2RGB)


# Convert the images to grayscale
gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# Use cv2.matchTemplate() to find the needle in the haystack
result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# Find the coordinates of the top-left corner of the best match
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc

# Draw a rectangle around the match
cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)



# Calculate the center of the match
center_x = top_left[0] + (needle_img.shape[1] / 2)
center_y = top_left[1] + (needle_img.shape[0] / 2)

# Move the mouse cursor to the center of the match
pyautogui.moveTo(center_x, center_y, duration=1.0)
time.sleep(1)

pydirectinput.click()
pydirectinput.click()
time.sleep(1)
screenshot = pyautogui.screenshot()

haystack_img = cv2.imread('FullTEM.png', cv2.IMREAD_UNCHANGED)


# Read the needle image (the image you want to find within the haystack)
needle_img = cv2.imread('item.png', cv2.IMREAD_UNCHANGED)


screenshot_numpy = np.array(screenshot)
haystack_img = cv2.cvtColor(screenshot_numpy, cv2.COLOR_BGR2RGB)


# Convert the images to grayscale
gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# Use cv2.matchTemplate() to find the needle in the haystack
result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# Find the coordinates of the top-left corner of the best match
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc

# Draw a rectangle around the match
cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)



# Calculate the center of the match
center_x = top_left[0] + (needle_img.shape[1] / 2)
center_y = top_left[1] + (needle_img.shape[0] / 2)

# Move the mouse cursor to the center of the match
pyautogui.moveTo(center_x, center_y, duration=1.0)
time.sleep(1)

pydirectinput.click()
pydirectinput.click()

screenshot = pyautogui.screenshot()

haystack_img = cv2.imread('Fullsea.png', cv2.IMREAD_UNCHANGED)


# Read the needle image (the image you want to find within the haystack)
needle_img = cv2.imread('sea.png', cv2.IMREAD_UNCHANGED)


screenshot_numpy = np.array(screenshot)
haystack_img = cv2.cvtColor(screenshot_numpy, cv2.COLOR_BGR2RGB)


# Convert the images to grayscale
gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# Use cv2.matchTemplate() to find the needle in the haystack
result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# Find the coordinates of the top-left corner of the best match
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc

# Draw a rectangle around the match
cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)



# Calculate the center of the match
center_x = top_left[0] + (needle_img.shape[1] / 2)
center_y = top_left[1] + (needle_img.shape[0] / 2)

# Move the mouse cursor to the center of the match
pyautogui.moveTo(center_x, center_y, duration=1.0)
time.sleep(1)

pydirectinput.click()
pydirectinput.click()

# read the haystack and needle images
haystack_img = cv2.imread('FULLHQ.png', cv2.IMREAD_UNCHANGED)
needle_img = cv2.imread('HQ.png', cv2.IMREAD_UNCHANGED)

gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# perform template matching
result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# find the coordinates of the best match
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc

cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)

# center_x = top_left[0] + (needle_img.shape[1] / 2)
# center_y = top_left[1] + (needle_img.shape[0] / 2)

# check if the match is above a certain threshold
threshold = 0.8
if max_val > threshold:
  center_x = top_left[0] + (needle_img.shape[1] / 2)
  center_y = top_left[1] + (needle_img.shape[0] / 2)

  pyautogui.moveTo(center_x, center_y, duration=1.0)


  time.sleep(1)
  keyboard.press("alt")
  time.sleep(2)
  pyautogui.moveRel(0, 20)
  time.sleep(0.5)
  pyautogui.moveRel(200, 0)
  time.sleep(5)
  keyboard.release("alt")
  x, y = pyautogui.position()

  x = x 
  y = y
  print("Mouse coordinates: ", x, y)




  left, top, width, height = (x - 83, y - 17, 110, 30)
  screenshot = pyautogui.screenshot(region=(left, top, width, height))
  screenshot.save("p1.png")
# Take the screenshot
#   screenshot = ImageGrab.grab(bbox=(left, top, right, bottom))

# # Save the screenshot
#   screenshot.save("p1.png")

  img = cv2.imread('p1.png')

# Convert to grayscale
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Otsu threshold
  thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# Pass the image to tesseract OCR
  number_string = pytesseract.image_to_string(thresh, lang='eng', config='--psm 10')
  number_string = number_string.replace('—___—\n', '')
  number_string = number_string.replace('\n', '')

  number_int = int(number_string)


# Print the integer variable
  print(number_int)

  number_int -= 1
  print(number_int)
  time.sleep(3)
  haystack_img = cv2.imread('fullX.png', cv2.IMREAD_UNCHANGED)
  needle_img = cv2.imread('X.png', cv2.IMREAD_UNCHANGED)

  gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
  gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# perform template matching
  result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# find the coordinates of the best match
  min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
  top_left = max_loc

  cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)
  center_x = top_left[0] + (needle_img.shape[1] / 2)
  center_y = top_left[1] + (needle_img.shape[0] / 2)


# Move the mouse cursor to the center of the match
  pyautogui.moveTo(center_x, center_y, duration=1.0)
  pydirectinput.click()
  pydirectinput.click()
  haystack_img = cv2.imread('fullASK.png', cv2.IMREAD_UNCHANGED)
  needle_img = cv2.imread('ASK.png', cv2.IMREAD_UNCHANGED)

  gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
  gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# perform template matching
  result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# find the coordinates of the best match
  min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
  top_left = max_loc

  cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)
  center_x = top_left[0] + (needle_img.shape[1] / 2)
  center_y = top_left[1] + (needle_img.shape[0] / 2)


# Move the mouse cursor to the center of the match
  pyautogui.moveTo(center_x, center_y, duration=1.0)
  pyautogui.moveRel(100, 0)
  pydirectinput.click()
  time.sleep(1)
  keyboard.press("backspace")
  keyboard.release("backspace")
  time.sleep(1)
  pyautogui.typewrite(str(number_int))
  

  haystack_img = cv2.imread('fullCONFIRM.png', cv2.IMREAD_UNCHANGED)
  needle_img = cv2.imread('CONFIRM.png', cv2.IMREAD_UNCHANGED)

  gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
  gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# perform template matching
  result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# find the coordinates of the best match
  min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
  top_left = max_loc

  cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)
  center_x = top_left[0] + (needle_img.shape[1] / 2)
  center_y = top_left[1] + (needle_img.shape[0] / 2)
  pyautogui.moveTo(center_x, center_y, duration=1.0)
  pydirectinput.click()
  pydirectinput.click()

   
  
else:
    # perform task if needle is not found
    print("Needle not found in haystack")
if i >= 8:
  pyautogui.moveTo(613, 578 , duration=1)
  main_window.right_click()
  time.sleep(5)



screenshot = pyautogui.screenshot()

haystack_img = cv2.imread('adjustfull.png', cv2.IMREAD_UNCHANGED)


# Read the needle image (the image you want to find within the haystack)
needle_img = cv2.imread('adjust.png', cv2.IMREAD_UNCHANGED)


screenshot_numpy = np.array(screenshot)
haystack_img = cv2.cvtColor(screenshot_numpy, cv2.COLOR_BGR2RGB)


# Convert the images to grayscale
gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# Use cv2.matchTemplate() to find the needle in the haystack
result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# Find the coordinates of the top-left corner of the best match
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc

# Draw a rectangle around the match
cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)



# Calculate the center of the match
center_x = top_left[0] + (needle_img.shape[1] / 2)
center_y = top_left[1] + (needle_img.shape[0] / 2)

# Move the mouse cursor to the center of the match
pyautogui.moveTo(center_x, center_y, duration=1.0)

main_window.right_click()
time.sleep(1)
screenshot = pyautogui.screenshot()

haystack_img = cv2.imread('comparefull.png', cv2.IMREAD_UNCHANGED)


# Read the needle image (the image you want to find within the haystack)
needle_img = cv2.imread('compare.png', cv2.IMREAD_UNCHANGED)


screenshot_numpy = np.array(screenshot)
haystack_img = cv2.cvtColor(screenshot_numpy, cv2.COLOR_BGR2RGB)


# Convert the images to grayscale
gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# Use cv2.matchTemplate() to find the needle in the haystack
result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# Find the coordinates of the top-left corner of the best match
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc

# Draw a rectangle around the match
cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)



# Calculate the center of the match
center_x = top_left[0] + (needle_img.shape[1] / 2)
center_y = top_left[1] + (needle_img.shape[0] / 2)

# Move the mouse cursor to the center of the match
pyautogui.moveTo(center_x, center_y, duration=1.0)
time.sleep(1)

x, y = pyautogui.position()
print("Mouse coordinates: ", x, y)
x = x
y = y 
import pyautogui
import pydirectinput
pydirectinput.moveTo(x, y)
pydirectinput.click()
pydirectinput.click()


time.sleep(2)
screenshot = pyautogui.screenshot()

haystack_img = cv2.imread('fullSEARCH.png', cv2.IMREAD_UNCHANGED)


# Read the needle image (the image you want to find within the haystack)
needle_img = cv2.imread('SREACH.png', cv2.IMREAD_UNCHANGED)


screenshot_numpy = np.array(screenshot)
haystack_img = cv2.cvtColor(screenshot_numpy, cv2.COLOR_BGR2RGB)


# Convert the images to grayscale
gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# Use cv2.matchTemplate() to find the needle in the haystack
result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# Find the coordinates of the top-left corner of the best match
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc

# Draw a rectangle around the match
cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)



# Calculate the center of the match
center_x = top_left[0] + (needle_img.shape[1] / 2)
center_y = top_left[1] + (needle_img.shape[0] / 2)

# Move the mouse cursor to the center of the match
pyautogui.moveTo(center_x, center_y, duration=1.0)
time.sleep(1)

pydirectinput.click()
pydirectinput.click()
time.sleep(1)
screenshot = pyautogui.screenshot()

haystack_img = cv2.imread('FullTEM.png', cv2.IMREAD_UNCHANGED)


# Read the needle image (the image you want to find within the haystack)
needle_img = cv2.imread('item.png', cv2.IMREAD_UNCHANGED)


screenshot_numpy = np.array(screenshot)
haystack_img = cv2.cvtColor(screenshot_numpy, cv2.COLOR_BGR2RGB)


# Convert the images to grayscale
gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# Use cv2.matchTemplate() to find the needle in the haystack
result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# Find the coordinates of the top-left corner of the best match
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc

# Draw a rectangle around the match
cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)



# Calculate the center of the match
center_x = top_left[0] + (needle_img.shape[1] / 2)
center_y = top_left[1] + (needle_img.shape[0] / 2)

# Move the mouse cursor to the center of the match
pyautogui.moveTo(center_x, center_y, duration=1.0)
time.sleep(1)

pydirectinput.click()
pydirectinput.click()

screenshot = pyautogui.screenshot()

haystack_img = cv2.imread('Fullsea.png', cv2.IMREAD_UNCHANGED)


# Read the needle image (the image you want to find within the haystack)
needle_img = cv2.imread('sea.png', cv2.IMREAD_UNCHANGED)


screenshot_numpy = np.array(screenshot)
haystack_img = cv2.cvtColor(screenshot_numpy, cv2.COLOR_BGR2RGB)


# Convert the images to grayscale
gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# Use cv2.matchTemplate() to find the needle in the haystack
result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# Find the coordinates of the top-left corner of the best match
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc

# Draw a rectangle around the match
cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)



# Calculate the center of the match
center_x = top_left[0] + (needle_img.shape[1] / 2)
center_y = top_left[1] + (needle_img.shape[0] / 2)

# Move the mouse cursor to the center of the match
pyautogui.moveTo(center_x, center_y, duration=1.0)
time.sleep(1)

pydirectinput.click()
pydirectinput.click()

# read the haystack and needle images
haystack_img = cv2.imread('FULLHQ.png', cv2.IMREAD_UNCHANGED)
needle_img = cv2.imread('HQ.png', cv2.IMREAD_UNCHANGED)

gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# perform template matching
result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# find the coordinates of the best match
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc

cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)

# center_x = top_left[0] + (needle_img.shape[1] / 2)
# center_y = top_left[1] + (needle_img.shape[0] / 2)

# check if the match is above a certain threshold
threshold = 0.8
if max_val > threshold:
  center_x = top_left[0] + (needle_img.shape[1] / 2)
  center_y = top_left[1] + (needle_img.shape[0] / 2)

  pyautogui.moveTo(center_x, center_y, duration=1.0)


  time.sleep(1)
  keyboard.press("alt")
  time.sleep(2)
  pyautogui.moveRel(0, 20)
  time.sleep(0.5)
  pyautogui.moveRel(200, 0)
  time.sleep(5)
  keyboard.release("alt")
  x, y = pyautogui.position()

  x = x 
  y = y
  print("Mouse coordinates: ", x, y)




  left, top, width, height = (x - 83, y - 17, 110, 30)
  screenshot = pyautogui.screenshot(region=(left, top, width, height))
  screenshot.save("p1.png")
# Take the screenshot
#   screenshot = ImageGrab.grab(bbox=(left, top, right, bottom))

# # Save the screenshot
#   screenshot.save("p1.png")

  img = cv2.imread('p1.png')

# Convert to grayscale
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Otsu threshold
  thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# Pass the image to tesseract OCR
  number_string = pytesseract.image_to_string(thresh, lang='eng', config='--psm 10')
  number_string = number_string.replace('—___—\n', '')
  number_string = number_string.replace('\n', '')

  number_int = int(number_string)


# Print the integer variable
  print(number_int)

  number_int -= 1
  print(number_int)
  time.sleep(3)
  haystack_img = cv2.imread('fullX.png', cv2.IMREAD_UNCHANGED)
  needle_img = cv2.imread('X.png', cv2.IMREAD_UNCHANGED)

  gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
  gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# perform template matching
  result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# find the coordinates of the best match
  min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
  top_left = max_loc

  cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)
  center_x = top_left[0] + (needle_img.shape[1] / 2)
  center_y = top_left[1] + (needle_img.shape[0] / 2)


# Move the mouse cursor to the center of the match
  pyautogui.moveTo(center_x, center_y, duration=1.0)
  pydirectinput.click()
  pydirectinput.click()
  haystack_img = cv2.imread('fullASK.png', cv2.IMREAD_UNCHANGED)
  needle_img = cv2.imread('ASK.png', cv2.IMREAD_UNCHANGED)

  gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
  gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# perform template matching
  result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# find the coordinates of the best match
  min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
  top_left = max_loc

  cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)
  center_x = top_left[0] + (needle_img.shape[1] / 2)
  center_y = top_left[1] + (needle_img.shape[0] / 2)


# Move the mouse cursor to the center of the match
  pyautogui.moveTo(center_x, center_y, duration=1.0)
  pyautogui.moveRel(100, 0)
  pydirectinput.click()
  time.sleep(1)
  keyboard.press("backspace")
  keyboard.release("backspace")
  time.sleep(1)
  pyautogui.typewrite(str(number_int))
  

  haystack_img = cv2.imread('fullCONFIRM.png', cv2.IMREAD_UNCHANGED)
  needle_img = cv2.imread('CONFIRM.png', cv2.IMREAD_UNCHANGED)

  gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
  gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# perform template matching
  result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# find the coordinates of the best match
  min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
  top_left = max_loc

  cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)
  center_x = top_left[0] + (needle_img.shape[1] / 2)
  center_y = top_left[1] + (needle_img.shape[0] / 2)
  pyautogui.moveTo(center_x, center_y, duration=1.0)
  pydirectinput.click()
  pydirectinput.click()

   
  
else:
    # perform task if needle is not found
    print("Needle not found in haystack")
if i >= 9:
 pyautogui.moveTo( 572, 611, duration=1)
 main_window.right_click()
 time.sleep(5)



screenshot = pyautogui.screenshot()

haystack_img = cv2.imread('adjustfull.png', cv2.IMREAD_UNCHANGED)


# Read the needle image (the image you want to find within the haystack)
needle_img = cv2.imread('adjust.png', cv2.IMREAD_UNCHANGED)


screenshot_numpy = np.array(screenshot)
haystack_img = cv2.cvtColor(screenshot_numpy, cv2.COLOR_BGR2RGB)


# Convert the images to grayscale
gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# Use cv2.matchTemplate() to find the needle in the haystack
result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# Find the coordinates of the top-left corner of the best match
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc

# Draw a rectangle around the match
cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)



# Calculate the center of the match
center_x = top_left[0] + (needle_img.shape[1] / 2)
center_y = top_left[1] + (needle_img.shape[0] / 2)

# Move the mouse cursor to the center of the match
pyautogui.moveTo(center_x, center_y, duration=1.0)

main_window.right_click()
time.sleep(1)
screenshot = pyautogui.screenshot()

haystack_img = cv2.imread('comparefull.png', cv2.IMREAD_UNCHANGED)


# Read the needle image (the image you want to find within the haystack)
needle_img = cv2.imread('compare.png', cv2.IMREAD_UNCHANGED)


screenshot_numpy = np.array(screenshot)
haystack_img = cv2.cvtColor(screenshot_numpy, cv2.COLOR_BGR2RGB)


# Convert the images to grayscale
gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# Use cv2.matchTemplate() to find the needle in the haystack
result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# Find the coordinates of the top-left corner of the best match
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc

# Draw a rectangle around the match
cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)



# Calculate the center of the match
center_x = top_left[0] + (needle_img.shape[1] / 2)
center_y = top_left[1] + (needle_img.shape[0] / 2)

# Move the mouse cursor to the center of the match
pyautogui.moveTo(center_x, center_y, duration=1.0)
time.sleep(1)

x, y = pyautogui.position()
print("Mouse coordinates: ", x, y)
x = x
y = y 
import pyautogui
import pydirectinput
pydirectinput.moveTo(x, y)
pydirectinput.click()
pydirectinput.click()


time.sleep(2)
screenshot = pyautogui.screenshot()

haystack_img = cv2.imread('fullSEARCH.png', cv2.IMREAD_UNCHANGED)


# Read the needle image (the image you want to find within the haystack)
needle_img = cv2.imread('SREACH.png', cv2.IMREAD_UNCHANGED)


screenshot_numpy = np.array(screenshot)
haystack_img = cv2.cvtColor(screenshot_numpy, cv2.COLOR_BGR2RGB)


# Convert the images to grayscale
gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# Use cv2.matchTemplate() to find the needle in the haystack
result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# Find the coordinates of the top-left corner of the best match
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc

# Draw a rectangle around the match
cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)



# Calculate the center of the match
center_x = top_left[0] + (needle_img.shape[1] / 2)
center_y = top_left[1] + (needle_img.shape[0] / 2)

# Move the mouse cursor to the center of the match
pyautogui.moveTo(center_x, center_y, duration=1.0)
time.sleep(1)

pydirectinput.click()
pydirectinput.click()
time.sleep(1)
screenshot = pyautogui.screenshot()

haystack_img = cv2.imread('FullTEM.png', cv2.IMREAD_UNCHANGED)


# Read the needle image (the image you want to find within the haystack)
needle_img = cv2.imread('item.png', cv2.IMREAD_UNCHANGED)


screenshot_numpy = np.array(screenshot)
haystack_img = cv2.cvtColor(screenshot_numpy, cv2.COLOR_BGR2RGB)


# Convert the images to grayscale
gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# Use cv2.matchTemplate() to find the needle in the haystack
result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# Find the coordinates of the top-left corner of the best match
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc

# Draw a rectangle around the match
cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)



# Calculate the center of the match
center_x = top_left[0] + (needle_img.shape[1] / 2)
center_y = top_left[1] + (needle_img.shape[0] / 2)

# Move the mouse cursor to the center of the match
pyautogui.moveTo(center_x, center_y, duration=1.0)
time.sleep(1)

pydirectinput.click()
pydirectinput.click()

screenshot = pyautogui.screenshot()

haystack_img = cv2.imread('Fullsea.png', cv2.IMREAD_UNCHANGED)


# Read the needle image (the image you want to find within the haystack)
needle_img = cv2.imread('sea.png', cv2.IMREAD_UNCHANGED)


screenshot_numpy = np.array(screenshot)
haystack_img = cv2.cvtColor(screenshot_numpy, cv2.COLOR_BGR2RGB)


# Convert the images to grayscale
gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# Use cv2.matchTemplate() to find the needle in the haystack
result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# Find the coordinates of the top-left corner of the best match
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc

# Draw a rectangle around the match
cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)



# Calculate the center of the match
center_x = top_left[0] + (needle_img.shape[1] / 2)
center_y = top_left[1] + (needle_img.shape[0] / 2)

# Move the mouse cursor to the center of the match
pyautogui.moveTo(center_x, center_y, duration=1.0)
time.sleep(1)

pydirectinput.click()
pydirectinput.click()

# read the haystack and needle images
haystack_img = cv2.imread('FULLHQ.png', cv2.IMREAD_UNCHANGED)
needle_img = cv2.imread('HQ.png', cv2.IMREAD_UNCHANGED)

gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# perform template matching
result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# find the coordinates of the best match
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc

cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)

# center_x = top_left[0] + (needle_img.shape[1] / 2)
# center_y = top_left[1] + (needle_img.shape[0] / 2)

# check if the match is above a certain threshold
threshold = 0.8
if max_val > threshold:
  center_x = top_left[0] + (needle_img.shape[1] / 2)
  center_y = top_left[1] + (needle_img.shape[0] / 2)

  pyautogui.moveTo(center_x, center_y, duration=1.0)


  time.sleep(1)
  keyboard.press("alt")
  time.sleep(2)
  pyautogui.moveRel(0, 20)
  time.sleep(0.5)
  pyautogui.moveRel(200, 0)
  time.sleep(5)
  keyboard.release("alt")
  x, y = pyautogui.position()

  x = x 
  y = y
  print("Mouse coordinates: ", x, y)




  left, top, width, height = (x - 83, y - 17, 110, 30)
  screenshot = pyautogui.screenshot(region=(left, top, width, height))
  screenshot.save("p1.png")
# Take the screenshot
#   screenshot = ImageGrab.grab(bbox=(left, top, right, bottom))

# # Save the screenshot
#   screenshot.save("p1.png")

  img = cv2.imread('p1.png')

# Convert to grayscale
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Otsu threshold
  thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# Pass the image to tesseract OCR
  number_string = pytesseract.image_to_string(thresh, lang='eng', config='--psm 10')
  number_string = number_string.replace('—___—\n', '')
  number_string = number_string.replace('\n', '')

  number_int = int(number_string)


# Print the integer variable
  print(number_int)

  number_int -= 1
  print(number_int)
  time.sleep(3)
  haystack_img = cv2.imread('fullX.png', cv2.IMREAD_UNCHANGED)
  needle_img = cv2.imread('X.png', cv2.IMREAD_UNCHANGED)

  gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
  gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# perform template matching
  result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# find the coordinates of the best match
  min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
  top_left = max_loc

  cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)
  center_x = top_left[0] + (needle_img.shape[1] / 2)
  center_y = top_left[1] + (needle_img.shape[0] / 2)


# Move the mouse cursor to the center of the match
  pyautogui.moveTo(center_x, center_y, duration=1.0)
  pydirectinput.click()
  pydirectinput.click()
  haystack_img = cv2.imread('fullASK.png', cv2.IMREAD_UNCHANGED)
  needle_img = cv2.imread('ASK.png', cv2.IMREAD_UNCHANGED)

  gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
  gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# perform template matching
  result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# find the coordinates of the best match
  min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
  top_left = max_loc

  cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)
  center_x = top_left[0] + (needle_img.shape[1] / 2)
  center_y = top_left[1] + (needle_img.shape[0] / 2)


# Move the mouse cursor to the center of the match
  pyautogui.moveTo(center_x, center_y, duration=1.0)
  pyautogui.moveRel(100, 0)
  pydirectinput.click()
  time.sleep(1)
  keyboard.press("backspace")
  keyboard.release("backspace")
  time.sleep(1)
  pyautogui.typewrite(str(number_int))
  

  haystack_img = cv2.imread('fullCONFIRM.png', cv2.IMREAD_UNCHANGED)
  needle_img = cv2.imread('CONFIRM.png', cv2.IMREAD_UNCHANGED)

  gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
  gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# perform template matching
  result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# find the coordinates of the best match
  min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
  top_left = max_loc

  cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)
  center_x = top_left[0] + (needle_img.shape[1] / 2)
  center_y = top_left[1] + (needle_img.shape[0] / 2)
  pyautogui.moveTo(center_x, center_y, duration=1.0)
  pydirectinput.click()
  pydirectinput.click()

   
  
else:
    # perform task if needle is not found
    print("Needle not found in haystack")
if i >= 10:
 pyautogui.moveTo( 531, 657, duration=1)
 main_window.right_click()
 time.sleep(5)



screenshot = pyautogui.screenshot()

haystack_img = cv2.imread('adjustfull.png', cv2.IMREAD_UNCHANGED)


# Read the needle image (the image you want to find within the haystack)
needle_img = cv2.imread('adjust.png', cv2.IMREAD_UNCHANGED)


screenshot_numpy = np.array(screenshot)
haystack_img = cv2.cvtColor(screenshot_numpy, cv2.COLOR_BGR2RGB)


# Convert the images to grayscale
gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# Use cv2.matchTemplate() to find the needle in the haystack
result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# Find the coordinates of the top-left corner of the best match
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc

# Draw a rectangle around the match
cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)



# Calculate the center of the match
center_x = top_left[0] + (needle_img.shape[1] / 2)
center_y = top_left[1] + (needle_img.shape[0] / 2)

# Move the mouse cursor to the center of the match
pyautogui.moveTo(center_x, center_y, duration=1.0)

main_window.right_click()
time.sleep(1)
screenshot = pyautogui.screenshot()

haystack_img = cv2.imread('comparefull.png', cv2.IMREAD_UNCHANGED)


# Read the needle image (the image you want to find within the haystack)
needle_img = cv2.imread('compare.png', cv2.IMREAD_UNCHANGED)


screenshot_numpy = np.array(screenshot)
haystack_img = cv2.cvtColor(screenshot_numpy, cv2.COLOR_BGR2RGB)


# Convert the images to grayscale
gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# Use cv2.matchTemplate() to find the needle in the haystack
result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# Find the coordinates of the top-left corner of the best match
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc

# Draw a rectangle around the match
cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)



# Calculate the center of the match
center_x = top_left[0] + (needle_img.shape[1] / 2)
center_y = top_left[1] + (needle_img.shape[0] / 2)

# Move the mouse cursor to the center of the match
pyautogui.moveTo(center_x, center_y, duration=1.0)
time.sleep(1)

x, y = pyautogui.position()
print("Mouse coordinates: ", x, y)
x = x
y = y 
import pyautogui
import pydirectinput
pydirectinput.moveTo(x, y)
pydirectinput.click()
pydirectinput.click()


time.sleep(2)
screenshot = pyautogui.screenshot()

haystack_img = cv2.imread('fullSEARCH.png', cv2.IMREAD_UNCHANGED)


# Read the needle image (the image you want to find within the haystack)
needle_img = cv2.imread('SREACH.png', cv2.IMREAD_UNCHANGED)


screenshot_numpy = np.array(screenshot)
haystack_img = cv2.cvtColor(screenshot_numpy, cv2.COLOR_BGR2RGB)


# Convert the images to grayscale
gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# Use cv2.matchTemplate() to find the needle in the haystack
result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# Find the coordinates of the top-left corner of the best match
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc

# Draw a rectangle around the match
cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)



# Calculate the center of the match
center_x = top_left[0] + (needle_img.shape[1] / 2)
center_y = top_left[1] + (needle_img.shape[0] / 2)

# Move the mouse cursor to the center of the match
pyautogui.moveTo(center_x, center_y, duration=1.0)
time.sleep(1)

pydirectinput.click()
pydirectinput.click()
time.sleep(1)
screenshot = pyautogui.screenshot()

haystack_img = cv2.imread('FullTEM.png', cv2.IMREAD_UNCHANGED)


# Read the needle image (the image you want to find within the haystack)
needle_img = cv2.imread('item.png', cv2.IMREAD_UNCHANGED)


screenshot_numpy = np.array(screenshot)
haystack_img = cv2.cvtColor(screenshot_numpy, cv2.COLOR_BGR2RGB)


# Convert the images to grayscale
gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# Use cv2.matchTemplate() to find the needle in the haystack
result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# Find the coordinates of the top-left corner of the best match
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc

# Draw a rectangle around the match
cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)



# Calculate the center of the match
center_x = top_left[0] + (needle_img.shape[1] / 2)
center_y = top_left[1] + (needle_img.shape[0] / 2)

# Move the mouse cursor to the center of the match
pyautogui.moveTo(center_x, center_y, duration=1.0)
time.sleep(1)

pydirectinput.click()
pydirectinput.click()

screenshot = pyautogui.screenshot()

haystack_img = cv2.imread('Fullsea.png', cv2.IMREAD_UNCHANGED)


# Read the needle image (the image you want to find within the haystack)
needle_img = cv2.imread('sea.png', cv2.IMREAD_UNCHANGED)


screenshot_numpy = np.array(screenshot)
haystack_img = cv2.cvtColor(screenshot_numpy, cv2.COLOR_BGR2RGB)


# Convert the images to grayscale
gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# Use cv2.matchTemplate() to find the needle in the haystack
result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# Find the coordinates of the top-left corner of the best match
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc

# Draw a rectangle around the match
cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)



# Calculate the center of the match
center_x = top_left[0] + (needle_img.shape[1] / 2)
center_y = top_left[1] + (needle_img.shape[0] / 2)

# Move the mouse cursor to the center of the match
pyautogui.moveTo(center_x, center_y, duration=1.0)
time.sleep(1)

pydirectinput.click()
pydirectinput.click()

# read the haystack and needle images
haystack_img = cv2.imread('FULLHQ.png', cv2.IMREAD_UNCHANGED)
needle_img = cv2.imread('HQ.png', cv2.IMREAD_UNCHANGED)

gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# perform template matching
result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# find the coordinates of the best match
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc

cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)

# center_x = top_left[0] + (needle_img.shape[1] / 2)
# center_y = top_left[1] + (needle_img.shape[0] / 2)

# check if the match is above a certain threshold
threshold = 0.8
if max_val > threshold:
  center_x = top_left[0] + (needle_img.shape[1] / 2)
  center_y = top_left[1] + (needle_img.shape[0] / 2)

  pyautogui.moveTo(center_x, center_y, duration=1.0)


  time.sleep(1)
  keyboard.press("alt")
  time.sleep(2)
  pyautogui.moveRel(0, 20)
  time.sleep(0.5)
  pyautogui.moveRel(200, 0)
  time.sleep(5)
  keyboard.release("alt")
  x, y = pyautogui.position()

  x = x 
  y = y
  print("Mouse coordinates: ", x, y)




  left, top, width, height = (x - 83, y - 17, 110, 30)
  screenshot = pyautogui.screenshot(region=(left, top, width, height))
  screenshot.save("p1.png")
# Take the screenshot
#   screenshot = ImageGrab.grab(bbox=(left, top, right, bottom))

# # Save the screenshot
#   screenshot.save("p1.png")

  img = cv2.imread('p1.png')

# Convert to grayscale
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Otsu threshold
  thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# Pass the image to tesseract OCR
  number_string = pytesseract.image_to_string(thresh, lang='eng', config='--psm 10')
  number_string = number_string.replace('—___—\n', '')
  number_string = number_string.replace('\n', '')

  number_int = int(number_string)


# Print the integer variable
  print(number_int)

  number_int -= 1
  print(number_int)
  time.sleep(3)
  haystack_img = cv2.imread('fullX.png', cv2.IMREAD_UNCHANGED)
  needle_img = cv2.imread('X.png', cv2.IMREAD_UNCHANGED)

  gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
  gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# perform template matching
  result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# find the coordinates of the best match
  min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
  top_left = max_loc

  cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)
  center_x = top_left[0] + (needle_img.shape[1] / 2)
  center_y = top_left[1] + (needle_img.shape[0] / 2)


# Move the mouse cursor to the center of the match
  pyautogui.moveTo(center_x, center_y, duration=1.0)
  pydirectinput.click()
  pydirectinput.click()
  haystack_img = cv2.imread('fullASK.png', cv2.IMREAD_UNCHANGED)
  needle_img = cv2.imread('ASK.png', cv2.IMREAD_UNCHANGED)

  gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
  gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# perform template matching
  result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# find the coordinates of the best match
  min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
  top_left = max_loc

  cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)
  center_x = top_left[0] + (needle_img.shape[1] / 2)
  center_y = top_left[1] + (needle_img.shape[0] / 2)


# Move the mouse cursor to the center of the match
  pyautogui.moveTo(center_x, center_y, duration=1.0)
  pyautogui.moveRel(100, 0)
  pydirectinput.click()
  time.sleep(1)
  keyboard.press("backspace")
  keyboard.release("backspace")
  time.sleep(1)
  pyautogui.typewrite(str(number_int))
  

  haystack_img = cv2.imread('fullCONFIRM.png', cv2.IMREAD_UNCHANGED)
  needle_img = cv2.imread('CONFIRM.png', cv2.IMREAD_UNCHANGED)

  gray_haystack = cv2.cvtColor(haystack_img, cv2.COLOR_BGR2GRAY)
  gray_needle = cv2.cvtColor(needle_img, cv2.COLOR_BGR2GRAY)

# perform template matching
  result = cv2.matchTemplate(gray_haystack, gray_needle, cv2.TM_CCOEFF_NORMED)

# find the coordinates of the best match
  min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
  top_left = max_loc

  cv2.rectangle(haystack_img, top_left, (top_left[0] + needle_img.shape[1], top_left[1] + needle_img.shape[0]), (0, 0, 255), 2)
  center_x = top_left[0] + (needle_img.shape[1] / 2)
  center_y = top_left[1] + (needle_img.shape[0] / 2)
  pyautogui.moveTo(center_x, center_y, duration=1.0)
  pydirectinput.click()
  pydirectinput.click()

   
  
else:
    # perform task if needle is not found
    print("Needle not found in haystack")
 

``