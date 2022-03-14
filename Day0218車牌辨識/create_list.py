import glob,os
from macpath import basename

fp = open('./Haar-Training_carPlate/training/negative/bg.txt', 'w')
files = glob.glob("./Haar-Training_carPlate/training/negative/*.jpg")
print('開始產生 bg.txt')
text=""
for file in files:
    basename=os.path.basename(file)
    filename="negative/" + basename 
    text += filename + "\n"
    print(text)
    
fp.write(text)
fp.close()
print('bg.txt!完成!')
