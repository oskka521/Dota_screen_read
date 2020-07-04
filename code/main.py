import numpy as np
import cv2
from PIL import ImageGrab
import time


def convert_to_gray(img):
    processed_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    return(processed_img)


def extract_image():
    print_screen_pil = ImageGrab.grab(bbox=(0, 40, 800, 640))
    org_screen = np.array(print_screen_pil)
    return(org_screen)


def show_img(img):
    cv2.imshow('window', img)


def main():

    once = 1
    img = ""
    while once == 1:
        once = 0
        img = extract_image()
        gray_img = convert_to_gray(img)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
    print(gray_img)


if __name__ == "__main__":
    print("start")
    main()
