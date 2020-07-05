from PIL import Image, ImageGrab
import cv2
import numpy

img = cv2.cvtColor(numpy.array(ImageGrab.grab()), cv2.COLOR_RGB2BGR)
template = cv2.cvtColor(numpy.array(
    Image.open('MY_HEROS/JUGG.png')), cv2.COLOR_RGB2BGR)
d, w, h = template.shape[::-1]

res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)

# all matches:
threshold = 0.75
loc = numpy.where(res >= threshold)
found = 0
for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 0, 220), 1)
    found += 1

# best match:
best = numpy.amax(res)
pt = numpy.where(res == best)[::-1]
cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

print('Found: {}\nBest: {}'.format(found, best))

Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)).show()
