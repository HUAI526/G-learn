from PIL import Image
img = Image.open("./media/img01.jpg")
imggray = img.convert('L')

imggray.save("./media/gray01.jpg")