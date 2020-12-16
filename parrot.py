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
                TextSendMessage("広島エリアでイケメンあり･笑いありの最高の場所と言えば\n『DNA』全てはお客様に満足していただく為に…!!\n最高のイケメン達が今宵、今までにない興奮と感動を貴方に届けます。\nこの素敵な時間を味わって下さい♪"),
                TextSendMessage("ホスホス\n https://www.host2.jp/shop/neo_2/"),
                TextSendMessage("WILLIST\n https://willist.jp/shop/?area=1&cat=5&sid=662"),
            ]
        )
    elif event.message.text=="イベント":
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
                TextSendMessage("初回飲み放題メニュー\n・焼酎（鏡月　JINRO　ふんわり　黒霧島　いいちこ）\n・ブランデー\n・カクテル\n・ソフトドリンク（緑茶　午後の紅茶　オレンジ　アップル　その他）\n・ビール　（瓶は別料金）\n・指名料無料\n・tax＆service \n-通常フロア10%-\n-VIP フロア20%-\n\n当店は永久指名担当制となっております\n好みの男の子を数人選んでいただいた後順番に席につかせていただきます。\n（混雑状況により希望通り回れない場合もございますのでご確認ください）\n\n番号交換は原則1名まで。\n2回目のご来店の際の指名が担当になります、なおその際の担当変えは受け付けておりませんのでご了承ください。\n\n初回1時間のセット料金は無料ですが、男の子の飲み物や延長は別料金ですのでご注意ください。\n最初の延長以降は自動延長となりますのでお時間の管理はお客様自身でお願いいたします。\n"),
                TextSendMessage("----システム----\n初回　無料（1時間）\n女性　￥3,000- (2時間)\n男性　￥3,000- (1時間)\n延長　￥2,000- (1時間)\n\nセミVIP   ￥3,000-\nVIP     ￥5,000-\n"),
            ]
        )
    elif event.message.text=="ドリンク料金":
        line_bot_api.reply_message(
            event.reply_token,[
                TextSendMessage("----ドリンク----\n【ビール】\nビール　￥1,000-\nジーマ　￥1,000-\nコロナ　￥1,000-\n【Cocktail】\n各種　  ￥1,000-\n【Decanter】\nピッチャー　￥2,000-\nビールP　　￥2,000-\nカクテルP　￥3,000-\n【Other】\nスカイ　　　　￥1,000-\nﾉﾝアルコール　￥1,000-\n\n----ボトル----\n【焼酎】\n鏡月      　　　 ￥5,000-\nJapan　　　　　　￥5,000-\nSazan　　　　　　￥5,000-\nJinro　　　　　　￥5,000-\nふんわり　　　　 ￥6,000-\n鍛高譚（たんたかたん）　　￥7,000-\n黒霧島（くろきりしま）　　￥8,000-\n鍛高譚梅（たんたかたんうめ）￥8,000-\nいいちこ　　　　　　        ￥8,000-\nし　　ろ\n￥8,000-\n吉四六（きっちょむ）　　    ￥15,000-\n赤霧島 (あかきりしま)　　　 ￥20,000-\n富乃宝山（とみのほうざん）　￥30,000-\n魔　　王　　　　　　        ￥80,000-\n【Liqueur】\n上等梅酒（じょうとううめしゅ）￥7,000-\nゆずこまち　　　　          　￥8,000-\n杏露酒（しんるちゅう）　    　￥8,000-\nブル　シア　　　　　          ￥25,000-\nシンデレラ　　　　          　￥40,000-"),
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
