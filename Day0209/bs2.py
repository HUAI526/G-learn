from bs4 import BeautifulSoup
html ='''
<html>
    <head><meta cgarset="UTF-8"><title>我是網頁標題</title>
    <body>
        <p id='p1'>我是段落一</p>
        <p id='p2' class='red'>我是散落二</p>
    </body>
</html>
'''
sp = BeautifulSoup(html, 'html.parser')
print(sp.find('p'))
print(sp.find_all('p'))
print(sp.find('p',{'id':'p2','class':'red'}))
print(sp.find('p',id='p2', class_='red'))