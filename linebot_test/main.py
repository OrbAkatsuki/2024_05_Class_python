from flask import Flask, request, abort
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
import google.generativeai as genai
import openai
import os

load_dotenv()

app = Flask(__name__)
line_bot_api = LineBotApi(os.environ["CHANNEL_ACCESS_TOKEN"])
handler = WebhookHandler(os.environ["CHANNEL_SECRET"])
openai.api_key = os.environ["OPENAI_API_KEY"]

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

def get_gemini_response(prompt):
    genai.configure(api_key=os.environ["Gemini_API_KEY"])
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text

def get_chatgpt_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message['content']

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    user_message = event.message.text
    
    # 获取两个AI的回答
    gemini_response = get_gemini_response(user_message)
    chatgpt_response = get_chatgpt_response(user_message)
    
    # 组合两个AI的回答
    full_response = f"Gemini 回答：\n\n{gemini_response}\n\n" \
                    f"ChatGPT 回答：\n\n{chatgpt_response}"
    
    # 如果组合后的回答超过5000字符（Line的消息长度限制），则分开发送
    if len(full_response) > 5000:
        gemini_message = TextSendMessage(text=f"Gemini 回答：\n\n{gemini_response}")
        chatgpt_message = TextSendMessage(text=f"ChatGPT 回答：\n\n{chatgpt_response}")
        line_bot_api.reply_message(event.reply_token, [gemini_message, chatgpt_message])
    else:
        message = TextSendMessage(text=full_response)
        line_bot_api.reply_message(event.reply_token, message)

if __name__ == "__main__":
    app.run()