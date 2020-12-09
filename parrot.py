from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,ImageSendMessage,AudioMessage,ImageMessage,
)
import os

app = Flask(__name__)

#環境変数取得
YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
YOUR_CHANNEL_SECRET = os.environ["YOUR_CHANNEL_SECRET"]

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

    if event.message.text=="店舗案内":
        line_bot_api.reply_message(
            event.reply_token,[
                TextSendMessage("未完成"),
            ]
        )
    elif event.message.text=="イベント予定":
        line_bot_api.reply_message(
            event.reply_token,[
                TextSendMessage("未予定"),
            ]
        )
    elif event.message.text=="従業員名簿":
        line_bot_api.reply_message(
            event.reply_token,[
                TextSendMessage("代表"),
                TextSendMessage("https://www.instagram.com/mako41443106/"),
                TextSendMessage("売上No1.桜木NAOTO"),
                TextSendMessage("https://www.instagram.com/naoto_sakuragi/"),
                TextSendMessage("クロム"),
                TextSendMessage("https://www.instagram.com/kuromu960_clubdna/"),
            ]
        )
    elif event.message.text=="道案内":
        url ='https://i.ytimg.com/vi/0YSxmocFCJw/maxresdefault.jpg'
        line_bot_api.reply_message(
            event.reply_token,[
                TextSendMessage("木屋ビル４F"),
                TextSendMessage("〒730-0021 広島県広島市中区胡町２−１３"),
            ]
        )
    elif event.message.text=="料金表":
        line_bot_api.reply_message(
            event.reply_token,[
                TextSendMessage("未完成"),
            ]
        )
    elif event.message.text=="求人":
        line_bot_api.reply_message(
            event.reply_token,[
                TextSendMessage("Coming soon"),
            ]
        )  

    elif "[[["or"]]]" in event.message.text:
        line_bot_api.reply_message(
            event.reply_token,[
                TextSendMessage(text=event.message.text+"    その文字に対応する文は作ってないな🐤"),
            ]
        )
    else:
        print("そんなコマンドはない")

if __name__ == "__main__":
#    app.run()
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
