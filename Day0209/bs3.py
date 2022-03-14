from bs4 import BeautifulSoup
html = '''
<html>
    <head><meta cgarset="UTF-8"><title>我是網頁標題</title>
    <body>
        <p id='p3'>我是段落一</p>
        <p id='p2' class='red'>我是散落二</p>
    </body>
</html>
'''
sp = BeautifulSoup(html, 'html.parser')
print(sp.select('title'))
print(sp.select('p'))
print(sp.select('#p3'))
print(sp.select('.red'))