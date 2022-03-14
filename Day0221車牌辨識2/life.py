import cv2

def showbitmap(row, col, bg, h, w):
    for y in range(row,row+h):
        print(str('{:0>2d}').format(y)+":" , end="")
        for x in range(col,col+w):
            print(bg[y][x], end=",")
        print()
    print()
    
def area(row, col):
    global nn 
    if bg[row][col] != 255:
        return
    bg[row][col] = lifearea
    if col>1:
        if bg[row][col-1] == 255:
            nn += 1
            area(row,col-1)
    if col < w-1:
        if bg[row-1][col]==255:
            nn+=1
            area(row-1,col)
    if row<h-1:
        if bg[row+1][col]==255:
            nn+=1
            area(row+1,col)
            
image = cv2.imread('7.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_,thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)
h= thresh.shape[0]
w= thresh.shape[1]

bg=thresh.copy()
showbitmap(0,0,bg,h,w)
