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
                TextSendMessage("広島エリアでイケメンあり･笑いありの最高の場所と言えば\n『DNA』全てはお客様に満足していただく為に…!!\n最高のイケメン達が今宵、今までにない興奮と感動を貴方に届けます。/nこの素敵な時間を味わって下さい♪"),
                TextSendMessage("ホスホス\n https://www.host2.jp/shop/neo_2/"),
                TextSendMessage("WILLIST\n https://willist.jp/shop/?area=1&cat=5&sid=662"),
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
                TextSendMessage("代表\nhttps://www.instagram.com/mako41443106/"),
                TextSendMessage("売上No1.桜木NAOTO\nhttps://www.instagram.com/naoto_sakuragi/"),
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
    elif event.message.text=="部屋料金":
        line_bot_api.reply_message(
            event.reply_token,[
                TextSendMessage("----システム----\n
初回　無料（1時間）\n
女性　￥3,000- (2時間)\n
男性　￥3,000- (1時間)\n
延長　￥2,000- (1時間)\n
\n
セミVIP   ￥3,000-\n
VIP     ￥5,000-\n
"),
            ]
        )
    elif event.message.text=="ドリンク料金":
        line_bot_api.reply_message(
            event.reply_token,[
                TextSendMessage(""),
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
