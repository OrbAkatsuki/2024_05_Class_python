from flask import Flask,request,abort
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
import google.generativeai as genai
#import openai
import os
load_dotenv()

app = Flask(__name__)
line_bot_api = LineBotApi(os.environ["CHANNEL_ACCESS_TOKEN"])
handler = WebhookHandler(os.environ["CHANNEL_SECRET"])
#openai.api_key = os.environ["OPENAI_API_KEY"]

@app.route("/")
def index():
    return "<h1>LineBot的Webhook</h1>"

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    app.logger.info("Request body: " + str(request.get_data(as_text=True)))
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    genai.configure(api_key=os.environ["Gmini_API_KEY"])
    model = genai.get_model("gemini-1.5-flash")
    response = model.generate_content(event.message.text)
    message = TextSendMessage(text=response.text)
    line_bot_api.reply_message(event.reply_token, message)