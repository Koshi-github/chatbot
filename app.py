from flask import Flask, request, abort
import random

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

numberGameFlag = False  #数当てゲームフラグ
target = 0  #ターゲット

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

    message = event.message.text
    global numberGameFlag
    nyanMessage = ""

    if  numberGameFlag:
        nyanMessage = numberGame(message)
    else:
        nyanMessage = message + "ニャン！"

    if  message == "数当てゲーム":
        #数当てゲーム開始
        nyanMessage = "数当てゲーム開始だニャン！\n僕が考えた数を当てるニャンよ！"
        global target
        target = random.randrange(100)
        numberGameFlag = True
    elif message == "やめる":
        #数当てゲーム終了
        nyanMessage = "数当てゲームを終了するニャン！"
        numberGameFlag = False

    # line_bot_api.reply_message(
    #     event.reply_token,
    #     TextSendMessage(text=nyanMessage)
    # )

    line_bot_api.reply_message(
        event.reply_token,
        [TextSendMessage(text=nyanMessage), TextSendMessage(text="あげあげニャン！")]
    )

#数当てゲーム
def numberGame(message):

    if not message.isdigit():
        return "数字を入力してニャン！"

    global target
    number = int(message)

    if target == number:
        nyankoMessege = "正解だニャン！"
        global numberGameFlag
        numberGameFlag = False
    elif target < number:
        nyankoMessege = "もっと低い数字だニャン！"
    else:
        nyankoMessege = "もっと大きい数字だニャン！"
    
    return nyankoMessege

if __name__ == "__main__":
    app.run()