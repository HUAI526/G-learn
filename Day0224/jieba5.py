import jieba

jieba.set_dictionary('dictionary/dict.txt.big.txt')
jieba.load_userdict('dictionary/user_dict_test.txt')

sentence = '蔡英文我跟你說我這幾天都他媽超級想睡覺的啦幹!!'
breakword = jieba.cut(sentence, cut_all=False)
print('|'.join(breakword))