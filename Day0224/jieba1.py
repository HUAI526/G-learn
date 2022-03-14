import jieba
sentence = '我這幾天都他媽超級想睡覺的啦幹!!'
breakword = jieba.cut(sentence)
print('|'.join(breakword))