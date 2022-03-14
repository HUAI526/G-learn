import jieba
sentence = '我這幾天都他媽超級想睡覺的啦幹!!'
breakword = jieba.cut(sentence)
print('精確模式' + '|'.join(breakword))

breakword = jieba.cut(sentence, cut_all=True)
print('全文模式' + '|'.join(breakword))

breakword = jieba.cut_for_search(sentence)
print('搜尋引擎模式' + '|'.join(breakword))