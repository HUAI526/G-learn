from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.languages import AVA
from nltk import chat

chatbot1 = ChatBot('Gjun')
trainer1 = ChatterBotCorpusTrainer(chatbot1)
availableLanguages=[
    'english',
    'traditionalchinese']

availableCategories=[
    'sports',
    'science',
    'psychology',
    'politics',
    'movies',
    'money',
    'literature',
    'humor',
    'history',
    'greetings',
    'gossip',
    'food',
    'emotion',
    'conversations',
    'botprofile',
    'AI',
    'trivia']

for availableLanguage in availableLanguages:
    trainer1.train('chatterbot.corpus.'+availableLanguage)
    for availableCategory in availableCategories:
        trainer1.train('chatterbot.corpus.'+str(availableLanguage)+'.'+str(availableCategory))


ask1 = chatbot1.get_response('你好嗎')
while True:
    ask=input("請問您的回覆:")
    if ask.upper()=='bye'.upper():
        print('歡迎下次再來')
        break
    print('ChatterBot:'+str(chatbot1.get_response(ask)))        