import requests
from bs4 import BeautifulSoup as soup
from PIL import Image
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import jieba
import numpy as np
from collections import Counter

urls = []
url = 'https://udn.com/news/breaknews/1'
html = requests.get(url)
sp = soup(html.text, 'html.parser')
data1 = sp.select('div.story-list__news h2 a')
print(data1)
for d in data1:
    urls.append(d.get('title'))
    
text_news =''
i = 1
for url in urls:
    text_news+=url
    i += 1

jieba.set_dictionary('dictionary/dict.txt.big.txt')
with open('dictionary/stopWord_union.txt', 'r',encoding='utf-8-sig') as f:
    stops = f.read().split('\n')
terms = []
for t in jieba.cut(text_news, cut_all=False):
    if t not in stops:
        terms.append(t)
diction=Counter(terms)

font = 'msch.ttf'
mask = np.array(Image.open("heart.png"))
unioncloud = WordCloud(background_color="white", mask=mask,font_path=font)
unioncloud.generate_from_frequencies(frequencies=diction)

plt.figure(figsize=(6,6))
plt.imshow(unioncloud)
plt.axis('off')
plt.show()

unioncloud.to_file("union_Wordcloud.png")