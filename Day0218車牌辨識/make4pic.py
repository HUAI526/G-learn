from PIL import Image
import glob

path = './Haar-Training_carPlate/training/positive/'
fp = open(path + 'info.txt', 'r')
lines = fp.readlines()
count = len(glob.glob("./carPlate/*.bmp"))
if len(lines) > count:
    print("新圖片已產生")
else:
    rettext = ''
    print('開始產生圖片')
    for line in lines:
        data = line.split(' ')
        img = Image.open(path + data[0])
        x = int(data[2])
        y = int(data[3])
        w = int(data[4])
        h = int(data[5])
        reduceW = 30
        reduceH = int(reduceW*0.75)
        multi = float(300/(300-reduceW))
        neww = int(w*multi)
        newh = int(h*multi)
        
        if (x-reduceW) >5 and (y-reduceH) > 5:
            count += 1
            newimg = img.crop((reduceW, reduceH, 300, 225))
            newimg = newimg.resize((300, 225), Image.ANTIALIAS)
            newimg.save(path + 'rawdata/bmpraw{:0>3d}.bmp'.format(count), 'bmp')
            newx = int((x-reduceW)*multi-reduceW*(multi-1)/2)
            newy = int((y-reduceH)*multi-reduceH*(multi-1)/2)
            rettext = rettext + 'rawdata/bmpraw{:0>3d}.bmp'.format(count)+' '+1+' '+str(newx)+' '+str(newy)+' '+str(neww)+' '+str(newh)+'\n'
        
        if (x+w)<(300-reduceW-5) and y>(reduceW+5):
            count += 1
            newimg = img.crop((0, reduceH, (300-reduceW), 225))
            newimg = newimg.resize((300, 225), Image.ANTIALIAS)
            newimg.save(path + 'rawdata/bmpraw{:0>3d}.bmp'.format(count)+'bmp')
            newx = int(x*multi)
            newy = int((y-reduceH)*multi)
            rettext = rettext + 'rawdata/bmpraw{:0>3d}.bmp'.format(count)+' '+1+' '+str(newx)+' '+str(newy)+' '+str(neww)+' '+str(newh)+'\n'
        if (x-reduceW)>5 and (y+h)<(225-reduceH-5):
            count += 1
            newimg = img.crop((reduceW, 0, 300, 225-reduceH))
            newimg = newimg.resize((300, 225), Image.ANTIALIAS)
            newimg.save(path + 'rawdata/bmpraw{:0>3d}.bmp'.format(count)+'bmp')
            newx = int((x-reduceW)*multi)
            newy = int(y*multi)
            rettext = rettext + 'rawdata/bmpraw{:0>3d}.bmp'.format(count)+' '+1+' '+str(newx)+' '+str(newy)+' '+str(neww)+' '+str(newh)+'\n'
         
        if (x+w)<(300-reduceW-5) and (y+h)<(225-reduceH-5):
            count += 1
            newimg = img.crop((0,0,(300-reduceW), 225-reduceH))
            newimg = newimg.resize((300, 225), Image.ANTIALIAS)
            newimg.save(path + 'rawdata/bmpraw{:0>3d}.bmp'.format(count)+'bmp')
            newx = int(x*multi)
            newy = int(y*multi)
            rettext = rettext + 'rawdata/bmpraw{:0>3d}.bmp'.format(count)+' '+1+' '+str(newx)+' '+str(newy)+' '+str(neww)+' '+str(newh)+'\n'
        
    fp.close()
    
    fpmake = open(path + 'Info.txt', 'a')
    fpmake.write(rettext)
    fpmake.close()
    print('OK')      