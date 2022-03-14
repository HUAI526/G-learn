import cv2
from PIL import Image
import numpy as np
gray = cv2.imread("./media/img01.jpg",0)
_,thresh = cv2.threshold(gray, 99, 255, cv2.THRESH_BINARY)
cv2.imwrite("./media/thresh1.jpg", thresh)

img = Image.open("./media/img01.jpg")
w, h=img.size
img = img.convert('L')
for i in range(w):
    for j in range(h):
        if img.getpixel((i,j)) < 99:
            img.putpixel((i,j),(0))
        else:
            img.putpixel((i,j),(255))
img.save("./media/thresh2.jpg")