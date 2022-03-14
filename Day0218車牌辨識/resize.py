import PIL
from PIL import Image
import glob
import shutil, os
from time import sleep

def emptydir(dirname):
    if os.path.isdir(dirname):
        shutil.rmtree(dirname)
        sleep(2)
    os.mkdir(dirname)

def dirResize(src, dst):
    myfiles = glob.glob(src +'/*.JPG')
    emptydir(dst)
    print(src + '資料夾:')
    print('開始轉換圖形尺寸!')
    for i ,f in enumerate(myfiles):
        img = Image.open(f)
        img_new = img.resize((300,225), PIL.Image.ANTIALIAS)
        outname = str("resizejpg") + str('{:0>3d}').format(i+1)+'.jpg'
        img_new.save(dst+'/'+outname)
    print('轉換圖形尺寸完成!\n')
    
dirResize('carPlate_sr', 'carPlate')
dirResize('realPlate_sr', 'realPlate')
     