import pyautogui, time

# top left returns (left, top) and bottom right returns (right, bottom) for the box in main.py 
try:
    while True:
        x, y = pyautogui.position()
        print(f"\rMouse at: ({x}, {y})", end="")
        time.sleep(0.05)
except KeyboardInterrupt:
    print("\nDone.") 