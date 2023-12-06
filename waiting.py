#Print waiting with incremental periods
import os
import time
from pynput import keyboard

count = 0
enter_pressed = False

def on_press(key):
    global enter_pressed
    if key == keyboard.Key.enter:
        enter_pressed = True

def on_release(key):
    pass

listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()

while count < 20:
    os.system('cls')  # 'cls' for Windows; 'clear' for Unix
    dots = "." * count
    print("Waiting" + dots)
    time.sleep(1)
    count += 1

    if enter_pressed:
        print("Congrats!")
        listener.stop()
        break

listener.join()
  