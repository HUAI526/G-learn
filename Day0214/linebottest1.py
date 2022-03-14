from flask import Flask
app = Flask(__name__)

from flask import request, abort
from linebot import  LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

line_bot_api = LineBotApi('xWq+357/jAgdBhUeYKa2oxdiAxVOVjsoi1uTufUbpsQd0XDV5L8Nt0qJtKGU547wBxLQ8479oXVpVTKpUj7mEHpHHlPhIpHoq7xuenPyz99IETstCPT+qAZAqMhK6lERVmnxcX4wZm+sbe+nrjkKHQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('745d365d6636ce2eab38992f05c4bc5b')

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        handler.handle(body,signature)
    except InvalidSignatureError:
        abort(400)
    return 'ok'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text=event.message.text
    print('收到',text)
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text=event.message.text))
    
if __name__ == '__main__':
    app.run()