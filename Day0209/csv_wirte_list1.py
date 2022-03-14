import csv
# 開啟輸出的CSV檔案
with open('test1.csv','w',newline='') as csvfile:
    #建立CSV黨寫入物件
    writer = csv.writer(csvfile)
    
    #寫入欄位名稱
    writer.writerow(['姓名', '身高','體重'])
    #寫入資料
    writer.writerow(['Chiou', 170, 65])
    writer.writerow(['David', 175, 75])