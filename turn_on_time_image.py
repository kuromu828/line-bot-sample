# -*- coding: utf-8 -*-
import os
from pathlib import Path
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from flask import Flask, abort, request
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import (ImageMessage, ImageSendMessage, MessageEvent,
                            TextMessage, TextSendMessage)


app = Flask(__name__)

YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
YOUR_CHANNEL_SECRET = os.environ["YOUR_CHANNEL_SECRET"]

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)

APP_NAME = "xxxxxxxxxxxxx" # 自分のHerokuのアプリ名にしてください。
SRC_IMAGE_PATH = "static/images/{}.jpg"
MAIN_IMAGE_PATH = "static/images/{}_main.jpg"
PREVIEW_IMAGE_PATH = "static/images/{}_preview.jpg"

@app.route("/")
def hello_world():
    return "hello world!"

@app.route("/callback", methods=["POST"])
def callback():
    # get X-Line-Signature header value
    signature = request.headers["X-Line-Signature"]

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return "OK"


@handler.add(MessageEvent, message=ImageMessage)
def handle_image(event):
    message_id = event.message.id

    src_image_path = Path(SRC_IMAGE_PATH.format(message_id)).absolute()
    main_image_path = MAIN_IMAGE_PATH.format(message_id)
    preview_image_path = PREVIEW_IMAGE_PATH.format(message_id)
    save_image(message_id, src_image_path)
    date_the_image(src=src_image_path, desc=Path(main_image_path).absolute())
    date_the_image(src=src_image_path, desc=Path(preview_image_path).absolute())
    image_message = ImageSendMessage(
        original_content_url="https://{0}.herokuapp.com/{1}".format(APP_NAME, main_image_path),
        preview_image_url="https://{0}.herokuapp.com/{1}".format(APP_NAME, preview_image_path),
    )
    app.logger.info("https://{0}herokuapp.com/{1}".format(APP_NAME, main_image_path))
    line_bot_api.reply_message(event.reply_token, image_message)
    src_image_path.unlink()


def save_image(message_id: str, save_path: str) -> None:
    """保存"""
    print ("Wrightpath: {}".format(save_path))
    message_content = line_bot_api.get_message_content(message_id)
    with open(save_path, "wb") as f:
        for chunk in message_content.iter_content():
            f.write(chunk)

def date_the_image(src: str, desc: str, size=800) -> None:
    im = Image.open(src)
    if im.width > size:
        proportion = size / im.width
        im = im.resize((int(im.width * proportion), int(im.height * proportion)))
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype("./fonts/fonts-japanese-gothic.ttf", 60)
    text = datetime.now().strftime("%Y/%m/%d")
    x = 10
    y = 10
    margin = 5
    text_width = draw.textsize(text, font=font)[0] + margin
    text_height = draw.textsize(text, font=font)[1] + margin
    draw.rectangle(
        (x - margin, y - margin, x + text_width, y + text_height), fill=(255, 255, 255)
    )
    draw.text((x, y), text, fill=(0, 0, 0), font=font)
    im.save(desc)

if __name__ == "__main__":
#    app.run()
    port = int(os.getenv("PORT"))
    app.run(host="0.0.0.0", port=port)
