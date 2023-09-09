import pyautogui # pip install pyautogui
from PIL import Image, ImageGrab  # pip install pillow
import time # pip install times
import webbrowser as wb
# from numpy import asarray


def hit(key):
    pyautogui.keyDown(key)
    return


def isCollide(data):
    # Draw the rectangle for birds
    for i in range(300, 415):
        for j in range(410, 563):
            if data[i, j] < 100:
                hit("down")
                return
    # Draw the rectangle for cactus
    for i in range(300, 415):
        for j in range(563, 650):
            if data[i, j] < 100:
                hit("up")
                return

    return


if __name__ == "__main__":
    wb.open('chrome://dino')
    # print("Hey.. Dino game about to start in 3 seconds")

    time.sleep(2)
    hit("up")
    while True:
        # convert to grey scale i.e. balck and white
        image = ImageGrab.grab().convert('L')
        data = image.load()
        # print(asarray(image))
        isCollide(data)

'''
        # Draw the rectangle for cactus
        for i in range(155, 185):
            for j in range(390 ,490):
                data[i, j] = 0
        # Draw the rectangle for birds
        for i in range(155,185):
            for j in range(330, 385):
                data[i,j] = 171

        image.show()
        break
'''