from PIL import Image
img = Image.open("./media/img01.jpg")
img.show()
w,h=img.size
print(w,h)
filename=img.filename
print(filename)