import csv

csvtable = [
    ['姓名', '身高','體重'],
    ['KK', 170, 80],
    ['Hower', 174, 50]
    ]

with open('test2.csv', 'w', newline='') as csvfile:

    writer = csv.writer(csvfile)
    writer.writerows(csvtable)