import cv2
from PIL import Image
import sys
import pyocr
import pyocr.builders
import re
from cv2 import waitKey

image =cv2.imread('assember.jpg')
tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)
tool = tools[0]

result = tool.image_to_string(
    Image.open('assember.jpg'),
    builder = pyocr.builders.TextBuilder()
)

txt=result.replace("!","1")
real_txt=re.findall(r'[A-Z]+[\d]+', txt)

txt_Plate=""
for char in real_txt:
    txt_Plate += char
print("ocr 辨識結果:", result)
print("優化後辨識結果:", txt_Plate)

cv2.imshow('image', image)
cv2.moveWindow("image", 500, 250)
key = waitKey(0)
cv2.destroyAllWindows()