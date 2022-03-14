import openpyxl

workbook=openpyxl.Workbook()
sheet = workbook.worksheets[0]

sheet['A1'] = 'Hello'
sheet['B1'] = 'World'

listtitle=["姓名", "電話"]
sheet.append(listtitle)
listdata=["David", "0957892366"]
sheet.append(listdata)

workbook.save('test.xlsx')