import numpy as np
import cv2
from PIL import ImageGrab
import time


def process_img(org_img):
    processed_img = cv2.cvtColor(org_img, cv2.COLOR_RGB2GRAY)
    processed_img = cv2.Canny(processed_img, threshold1=200, threshold2=300)
    return(processed_img)


def main():
    last_time = time.time()

    while True:
        current_time = time.time()
        diff_time = current_time - last_time
        last_time = current_time
        print(f'loop took = {diff_time} sec')

        print_screen_pil = ImageGrab.grab(bbox=(0, 40, 800, 640))
        org_screen = np.array(print_screen_pil)
        edge_screen = process_img(org_screen)
        #cv2.imshow('window', org_screen)

        cv2.imshow('window', edge_screen)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindow()
            break


if __name__ == "__main__":
    print("start")
    main()
