
import telebot
import os
from flask import Flask, request

API_TOKEN = '7637038432:AAHUJ5cxZSmoeQNrQ4MDWvAnhtDBeTfrZo8'
bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

# /raid command handler
@bot.message_handler(commands=['raid'])
def handle_raid(message):
    try:
        args = message.text.split()[1:]
        if len(args) < 2:
            bot.send_message(message.chat.id, "❗Usage: /raid <count> <message>")
            return

        count = int(args[0])
        spam_text = ' '.join(args[1:])

        for i in range(count):
            bot.send_message(message.chat.id, spam_text)
    except Exception as e:
        bot.send_message(message.chat.id, f"⚠️ Error: {str(e)}")

# Flask route for Telegram webhook
@app.route('/' + API_TOKEN, methods=['POST'])
def webhook():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return '', 200

# Set webhook when server starts
@app.route('/')
def index():
    bot.remove_webhook()
    webhook_url = os.environ.get('RENDER_EXTERNAL_URL') + API_TOKEN
    bot.set_webhook(url=webhook_url)
    return 'Webhook set ✅'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
