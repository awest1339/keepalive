import win32api
from time import sleep
from random import randint
import win32con

SLEEP_INTERVAL = 60


def move_mouse(x, y):
    win32api.SetCursorPos((x,y))

    
if __name__ == '__main__':

    while True:
        move_mouse(randint(100, 1400), randint(100, 700))
    
        sleep(SLEEP_INTERVAL)
