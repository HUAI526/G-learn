import csv
with open('test3.csv', newline='') as csvfile:
    rows = csv.DictReader(csvfile)
    
    for row in rows:
        print(row['姓名'], row['身高'], row['體重'])