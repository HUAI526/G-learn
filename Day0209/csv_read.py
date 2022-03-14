import csv
with open('test1.csv', newline='') as csvfile:
    rows = csv.reader(csvfile)
    
    for row in rows:
        print(row[0])