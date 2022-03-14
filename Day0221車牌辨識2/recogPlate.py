from Day0221.cropNum_Assember import lifearea
def emptydir(dirname):
    if os.path.isdir(dirname):
        shutil.ratree(dirname)
        sleep(2)
    os.mkdir(dirname)
    
def dirResize(src, dst):
    myfiles = glob.glob(src + '/*JPG')
    emptydir(dst)
    print(src + '資料夾:')
    print('開始轉換圖形尺寸')
    for f in myfiles:
        fname = f.split("\\")[-1]
        img = Image.open(f)
        img_new = img.resize((300,225), PIL.Image.ANTIALIAS)
        img_new.save(dst + '/' + fname)
    print('轉換圖形尺寸完成\n')

def area(row, col):
    global nn
    if bg[row][col] !=255:
        return
    bg[row][col] = lifearea
    if col>1:
        if bg[row][col] != 255:
        return
    bg[row][col] = lifearea
    if col>1:
        if bg[row][col-1]==255:
            nn += 1
            area(row,col-1)
    if col<w-1:
        if bg[row][col+1]==255:
            nn += 1
            area(row, col+1)
    if row>1:
        if bg[row-1][col]==255:
            nn+=1
            area(row-1,col)
    if row<h-1:
        if bg[row+1][col]==255:
            nn+=1
            area(row+1,col)

import cv2
import PIL
from PIL import Image
import glob
import shutil, os
from time import sleep
import numpy as np
import sys
import pyocr
import pyocr.builders
import re

dirResize('predicPlate_sr', 'predictPlate')

print('開始擷取車牌!')
print('無法擷取車牌圖片:')
dstdir = 'cropPlate'
myfiles = glob.glob('predictPlate\*.JPG')
emptydir(dstdir)
for imgname in myfiles:
    filename = (imgname.split('\\'))[-1]
    img = cv2.CascadeClassifier('haar_carplate.xml')
    signs = detector.detectMultiScale(img, scaleFactor = 1.1, minNeighbors=4, minSize=(20,20))
    