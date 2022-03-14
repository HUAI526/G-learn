import csv
with open('test3.csv', 'w', newline='') as csvfile:
    fieldnames = ['姓名', '身高','體重']
    
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    
    writer.writerow({'姓名':'Chiou','身高' :170,'體重' :65})
    writer.writerow({'姓名':'David','身高' :175,'體重' :75})