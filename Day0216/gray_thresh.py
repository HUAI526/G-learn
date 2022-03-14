import cv2 

def show(image):
    for y in range(8,14):
        for x in range(6,10):
            print(image[y,x], end=" ")
        print()
    print()
img = cv2.imread('./media/face.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
print("gray.shape=", gray.shape)
show(gray)

_,thresh = cv2.threshold(gray, 187, 255, cv2.THRESH_BINARY)
print("thresh.shape=", thresh.shape)
show(thresh)

gray2 = cv2.imread("./media/face.jpg", 0)
print("gray2.shape=", gray.shape)
show(gray2)

_,thresh2 = cv2.threshold(gray2, 187, 200, cv2.THRESH_BINARY_INV)
print("thresh2.shape=", thresh.shape)
show(thresh2)