from PIL import Image
img = Image.open("./media/img01.jpg")
w, h=img.size

img1=img.resize((w*2,h))
img1.save("./media/resize01.jpg")