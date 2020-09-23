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
        url ='https://i.ytimg.com/vi/0YSxmocFCJw/maxresdefault.jpg'
        line_bot_api.reply_message(
            event.reply_token,[
                TextSendMessage(text=event.message.text+"!!!!!!!!!!"),
                ImageSendMessage(url, url), 
            ]
        )
    elif event.message.text=="2001/03/21":
        url ='https://i.ytimg.com/vi/0YSxmocFCJw/maxresdefault.jpg'
        line_bot_api.reply_message(
            event.reply_token,[
                TextSendMessage(text=event.message.text+"!!!!!!!!!!"),
                ImageSendMessage(url, url), 
            ]
        )
    elif event.message.text=="String taste Lollipop":
        url ='https://i.ytimg.com/vi/0YSxmocFCJw/maxresdefault.jpg'
        line_bot_api.reply_message(
            event.reply_token,[
                TextSendMessage(text=event.message.text+"!!!!!!!!!!"),
                ImageSendMessage(url, url), 
            ]
        )
    elif event.message.text=="一覧表":
        url ='https://i.ytimg.com/vi/0YSxmocFCJw/maxresdefault.jpg'
        line_bot_api.reply_message(
            event.reply_token,[
                ImageSendMessage(url, url), 
            ]
        )
    elif event.message.text=="Different_world":
        url ='https://i.ytimg.com/vi/0YSxmocFCJw/maxresdefault.jpg'
        line_bot_api.reply_message(
            event.reply_token,[
                TextSendMessage(text=event.message.text+"!!!!!!!!!!"),
                ImageSendMessage(url, url), 
            ]
        )
    elif event.message.text=="giggle":
        url ='https://i.ytimg.com/vi/0YSxmocFCJw/maxresdefault.jpg'
        line_bot_api.reply_message(
            event.reply_token,[
                TextSendMessage(text=event.message.text+"!!!!!!!!!!"),
                ImageSendMessage(url, url), 
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
    elif "米津玄師" in event.message.text:
        line_bot_api.reply_message(
            event.reply_token,[
                TextSendMessage("憧れ"),
            ]
        )  
    elif "かえる"or"カエル"or"蛙" in event.message.text:
        line_bot_api.reply_message(
            event.reply_token,[
                TextSendMessage("憧れ"),
            ]
        )  
    else:
        print("そんなコマンドはない")

if __name__ == "__main__":
#    app.run()
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)