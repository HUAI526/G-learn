from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba
import numpy as np
from collections import Counter

text = open('news1.txt', "r",encoding="utf-8").read()

jieba.set_dictionary('dictionary/dict.txt.big.txt')
with open('dictionary/stopWord_cloud.txt', 'r',encoding='utf-8-sig') as f:
    stops = f.read().split('\n')
terms = []
for t in jieba.cut(text, cut_all=False):
    if t not in stops:
        terms.append(t)
diction=Counter(terms)

font = 'msch.ttf'
wordcloud = WordCloud(font_path=font)
wordcloud.generate_from_frequencies(frequencies=diction)

plt.figure(figsize=(6,6))
plt.imshow(wordcloud)
plt.axis('off')
plt.show()

wordcloud.to_file("news_Wordcloud.png")