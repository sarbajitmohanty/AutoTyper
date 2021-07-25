from pynput.keyboard import Key, Controller
import time

keyboard = Controller()
time.sleep(5)
with open('code.txt','r') as file:
    for line in file:
        for char in line:
            keyboard.press(char)
            keyboard.release(char)
            time.sleep(0.1)
        #keyboard.press(Key.enter)
        #keyboard.release(Key.enter)
