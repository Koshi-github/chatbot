from flask import Flask, request, abort
import random
from tenki import getTenkiInfo
from tenki import getDayTenkiInfo
from syokuzai import SpreadSheet

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

syokuzaiModeFlag = False  #食材モードフラグ

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
    global syokuzaiModeFlag
    nyanMessage = ""

    if  syokuzaiModeFlag:
        sp = SpreadSheet()
        sp.__init__()
        ryoriName = sp.Read(1,1)
        nyanMessage = "これが" + ryoriName + "の材料ニャン！"

        syokuzaiModeFlag = False
    else:
        profile = line_bot_api.get_profile(event.source.user_id)
        nyanMessage = message + "ニャン！" + profile.user_id

    if "食材教えて" in message:
        syokuzaiModeFlag = True
        nyanMessage = "何の食材が知りたいニャン？"
    elif "天気" in message and "今日" in message:
        nyanMessage = "今日の" + getDayTenkiInfo(0)
    elif "天気" in message and "明日" in message:
        nyanMessage = "明日の" + getDayTenkiInfo(1)
    elif "天気" in message and "明後日" in message:
        nyanMessage = "明後日の" + getDayTenkiInfo(2)
    elif "天気" in message:
        nyanMessage = "現在の" + getTenkiInfo()

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=nyanMessage)
    )

    # line_bot_api.reply_message(
    #     event.reply_token,
    #     [TextSendMessage(text=nyanMessage), TextSendMessage(text="あげあげニャン！")]
    # )

if __name__ == "__main__":
    app.run()