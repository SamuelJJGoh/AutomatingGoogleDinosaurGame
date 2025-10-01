import pyautogui
import time
from PIL import ImageGrab    
                
print("Switch to the T-Rex game window. Starting in 3 seconds...")
time.sleep(3)
     
def is_obstacle_ahead():
    # Define the area in front of the dinosaur (adjust coordinates as needed)
    # box below is for chrome://dino/ with window screen to the left

    box = (136, 256, 255, 289) # Screenshot box = (left, top, right, bottom)
    img = ImageGrab.grab(box)
    gray = img.convert(mode="L")  # convert to grayscale
    pixels = gray.getdata() # flattens all pixel values (0=black ... 255=white)
    print(pixels)
    threshold = 100  # adjust depending on brightness

    if min(pixels) < threshold: # if any single pixel is dark, return True
        return True
    return False

print("Bot started! Press Ctrl+C to stop.")

while True:
    try:
        if is_obstacle_ahead():
            pyautogui.press("space") 
        time.sleep(0.01)  # small delay to reduce CPU usage
        
    except KeyboardInterrupt:
        print("Bot stopped.")
        break

