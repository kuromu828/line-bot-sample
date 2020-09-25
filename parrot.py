from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,ImageSendMessage,
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

    if event.message.text=="HEY！":
        url =''
        line_bot_api.reply_message(
            event.reply_token,[
                TextSendMessage("作曲を依頼の方は\n以下のメールアドレスまで\nmitabinodoka123@gmail.com\n一曲1500en~"),
            ]
        )
    elif event.message.text=="2001/03/21":
        line_bot_api.reply_message(
            event.reply_token,[
                TextSendMessage("https://www.youtube.com/channel/UCl4pHQq8mo3VUFxRs6g_aZQ?pbjreload=102"),
                TextSendMessage("https://youtu.be/vIiM1gmEhRA"),
                TextSendMessage("https://www.nicovideo.jp/watch/sm37437653"),
            ]
        )
    elif event.message.text=="String taste Lollipop":
        url ='https://d.kuku.lu/53631ba44f'
        line_bot_api.reply_message(
            event.reply_token,[
                TextSendMessage("http://linux.mec.edc.ac.jp/~samson/"),
                TextSendMessage("出来損ないのHPです　MUSICとContact　のページだけ完成してます\n　いつか消します"),
                ImageSendMessage(url,url),
            ]
        )
    elif event.message.text=="一覧表":
        url ='https://i.ytimg.com/vi/0YSxmocFCJw/maxresdefault.jpg'
        line_bot_api.reply_message(
            event.reply_token,[
                TextSendMessage("こんにちは\nおはよう\nこんばんは\n食べ物\n秘密\n愚痴"),
            ]
        )
    elif event.message.text=="Different_world":
        line_bot_api.reply_message(
            event.reply_token,[
                TextSendMessage("https://twitter.com/nodoka_321"),
                TextSendMessage("https://www.instagram.com/mitabinodoka123/"),
            ]
        )
    elif event.message.text=="giggle":
        line_bot_api.reply_message(
            event.reply_token,[
                TextSendMessage("Coming soon"),
            ]
        )  
    elif "こんにちは\nおはよう\nこんばんは\n食べ物\n秘密\n愚痴" in event.message.text:
        line_bot_api.reply_message(
            event.reply_token,[
                TextSendMessage("普通まんまコピーするか？　そういうことじゃないって"),
            ]
        )
    elif "肥田彩花" in event.message.text:
        line_bot_api.reply_message(
            event.reply_token,[
                TextSendMessage("ずっと幸せを願う人"),
            ]
        )  
    elif "大﨑琴美" in event.message.text:
        line_bot_api.reply_message(
            event.reply_token,[
                TextSendMessage("怖いときに付き添ってくれた人"),
            ]
        )  
    elif "山﨑笙太郎" in event.message.text:
        line_bot_api.reply_message(
            event.reply_token,[
                TextSendMessage("完璧なデッサン人形"),
            ]
        )  
    elif "大屋悠斗" in event.message.text:
        line_bot_api.reply_message(
            event.reply_token,[
                TextSendMessage("きっと爆発の能力者だろう"),
            ]
        ) 
    elif "青笹大輝" in event.message.text:
        line_bot_api.reply_message(
            event.reply_token,[
                TextSendMessage("ギタリスト"),
            ]
        ) 
    elif "岩谷正文" in event.message.text:
        line_bot_api.reply_message(
            event.reply_token,[
                TextSendMessage("ドラムの天才"),
            ]
        ) 
    elif "松浦優斗" in event.message.text:
        line_bot_api.reply_message(
            event.reply_token,[
                TextSendMessage("テンパ"),
            ]
        ) 
    elif "テンパ" in event.message.text:
        line_bot_api.reply_message(
            event.reply_token,[
                TextSendMessage("松浦優斗"),
            ]
        ) 
    elif "米津玄師" in event.message.text:
        line_bot_api.reply_message(
            event.reply_token,[
                TextSendMessage("憧れ"),
            ]
        )  
    elif "二神巴野土香" in event.message.text:
        line_bot_api.reply_message(
            event.reply_token,[
                TextSendMessage("~ニノカミハ　ノドカ~多分いつか苗字を変えます"),
            ]
        )
    elif "食べ物" in event.message.text:
        line_bot_api.reply_message(
            event.reply_token,[
                TextSendMessage("日によって変わっちゃうな\nでも割と何でも好きだよ"),
            ]
        ) 
    elif "秘密" in event.message.text:
        line_bot_api.reply_message(
            event.reply_token,[
                TextSendMessage("漢字の名前がわかる人をどう思っているかはある程度ここに秘密をかいてるよ"),
            ]
        )  
    elif "愚痴" in event.message.text:
        line_bot_api.reply_message(
            event.reply_token,[
                TextSendMessage("直接聞くよ\nそれが億劫ならここに吐いていけばいい\n僕は何があろうと君の味方のつもりだ"),
            ]
        )  
    elif "かえる" in event.message.text:
        line_bot_api.reply_message(
            event.reply_token,[
                TextSendMessage("一生好きなもの"),
            ]
        )  
    elif "カエル" in event.message.text:
        line_bot_api.reply_message(
            event.reply_token,[
                TextSendMessage("一生好きなもの"),
            ]
        )
    elif "蛙" in event.message.text:
        line_bot_api.reply_message(
            event.reply_token,[
                TextSendMessage("一生好きなもの"),
            ]
        )  
    elif "こんにちは" in event.message.text:
        line_bot_api.reply_message(
            event.reply_token,[
                TextSendMessage(text=event.message.text+"　　スマホの中だと太陽も月も見えないから残念だ"),
            ]
        )
    elif "おはよう" in event.message.text:
        line_bot_api.reply_message(
            event.reply_token,[
                TextSendMessage(text=event.message.text+"　　スマホの中だと太陽も月も見えないから残念だ"),
            ]
        )
    elif "こんばんは" in event.message.text:
        line_bot_api.reply_message(
            event.reply_token,[
                TextSendMessage(text=event.message.text+"　　スマホの中だと太陽も月も見えないから残念だ"),
            ]
        )
    elif "[[["or"]]]" in event.message.text:
        line_bot_api.reply_message(
            event.reply_token,[
                TextSendMessage(text=event.message.text+"その文字に対応する文は作ってないな🐤"),
            ]
        )
    else:
        print("そんなコマンドはない")

if __name__ == "__main__":
#    app.run()
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)