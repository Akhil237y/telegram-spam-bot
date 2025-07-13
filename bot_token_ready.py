
import telebot
import time

API_TOKEN = '7637038432:AAHUJ5cxZSmoeQNrQ4MDWvAnhtDBeTfrZo8'
bot = telebot.TeleBot(API_TOKEN)

# /raid command ka handler
@bot.message_handler(commands=['raid'])
def handle_raid(message):
    try:
        args = message.text.split()[1:]  # raid ke baad jo likha ho
        if len(args) < 2:
            bot.send_message(message.chat.id, "❗Usage: /raid <count> <message>")
            return

        count = int(args[0])
        spam_text = ' '.join(args[1:])

        for i in range(count):
            bot.send_message(message.chat.id, spam_text)
            time.sleep(0.4)  # 0.4 second delay

    except Exception as e:
        bot.send_message(message.chat.id, f"⚠️ Error: {str(e)}")

# Bot ko polling se start karo
print("🤖 Bot is running...")
bot.infinity_polling()
