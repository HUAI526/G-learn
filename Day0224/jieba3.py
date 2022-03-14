import jieba

jieba.set_dictionary('dictionary/dict.txt.big.txt')

sentence = '我這幾天都他媽超級想睡覺的啦幹!!'
breakword = jieba.cut(sentence, cut_all=False)
print('|'.join(breakword))