import cv2
from PIL import Image
import numpy as np
img = Image.open("./media/img01.jpg")
img.show()

img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
cv2.imshow("OpenCV", img)
cv2.waitKey()
cv2.destroyAllWindows()