# Program to show what keys are pressed. It is stopped by CTRL+C
from pynput.keyboard import Listener
import time

def on_press(key):
    try:
        print(f"Key {key.char} pressed")
    except AttributeError:
        print(f"{key} is pressed")

# Start the listener
listener = Listener(on_press=on_press)
listener.start()

try:
    # we didn't use join as it would have blocked the main thread preventing keyboardinterrupt  from working.
    while listener.running:  
        pass
except KeyboardInterrupt:
    print("\nStopped by user (Ctrl + C)")
    # stops the execution of listener
    listener.stop()  
    # exits the thread
    listener.join()
