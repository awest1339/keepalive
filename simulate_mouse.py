import win32api
from time import sleep
from random import randint
import win32con

L = [x for x in range(10, 50000, 100)]


def move_mouse(x, y):
    win32api.SetCursorPos((x,y))

    
if __name__ == '__main__':
    while True:
        move_mouse(randint(0, len(L)-1), randint(0, len(L)-1))
    
        sleep(10)
