import numpy as np
import cv2
from PIL import ImageGrab
import time


print("start")


last_time = time.time()
while True:
    print_screen_pil = ImageGrab.grab(bbox=(0, 40, 800, 640))
    print(f'loop took {time.time()-last_time} sec')
    cv2.imshow('window', np.array(print_screen_pil))

    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindow()
        break
