from flask import Flask, request, abort
import main

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

import os

app = Flask(__name__)

@app.route("/")
def test():
    return "OK!"

line_bot_api = LineBotApi('1Z6hiCqj7SGQgZgF60g8tTqB4LYviStIMtQU+wfQ/obac5jO/A3uuy1hVDQhrMPeG5Tg12jKgwPeiLgA3CEbPoP5LMcgxsJgcn7bT2frm0du/FFeK+7szo8Kizl79ZN241wqxbZwCb/1deviAZcOGQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('6c0190b40864600e8ff8373d49471efa')

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    # app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

    returnMessage = main.execute(event.message.text, line_bot_api.get_profile(event.source.user_id))
    sendMessage(event,returnMessage)

if __name__ == "__main__":
    app.run()

def sendMessage(event,messages):
    messageList = []

    for message in messages:
        messageList.append(TextSendMessage(text=message))

    line_bot_api.reply_message(event.reply_token,messageList)