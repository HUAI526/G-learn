import jieba

jieba.set_dictionary('dictionary/dict.txt.big.txt')
jieba.load_userdict('dictionary/user_dict_test.txt')
with open('dictionary/stopWord_test.txt', 'r',encoding='utf-8-sig') as f:
    stops = f.read().split('\n')
    
sentence = '蔡英文我跟你說我這幾天都他媽超級想睡覺的啦幹!!'
breakword = jieba.cut(sentence, cut_all=False)
words = []
for word in breakword:
    if word not in stops:
        words.append(word)
print('|'.join(words))