from PIL import Image
import sys
import pyocr
import pyocr.builders

tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("No OCR tool foind")
    sys.exit(1)
tool = tools[0]

txt = tool.image_to_string(
    Image.open('test.jpg'),
    builder=pyocr.builders.TextBuilder()
)
print("result=",txt)