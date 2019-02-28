from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)


line_bot_api = LineBotApi('H8CZqRJCA8DO+BwVsUdCOEEM1FKyci+44dlt+lZlJAGqKhrf/MU6pFav69+DB61Pg913aIXgAoEnCkGteD2eqgOEeNvzEWgzgNqCM1+A2Ic8FntKsDQLLIePDg4DufJDmzY6g+WWnN6B1Q2Izzz8nwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('a14e2fdc65787632ed1deec346df41f2')

@app.route("/", methods=['GET'])
def hello():
    return "Hello World!"

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    print("Request body: " + body, "Signature: " + signature)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
       abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    print(msg)
    msg = msg.encode('utf-8')
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text=event.message.text))

if __name__ == "__main__":
    app.run(debug=True)