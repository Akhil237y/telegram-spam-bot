import telebot
import time

TOKEN = "7637038432:AAHUJ5cxZSmoeQNrQ4MDWvAnhtDBeTfrZo8"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: message.text and message.text.startswith(".raid"))
def raid(message):
    try:
        parts = message.text.split(maxsplit=2)
        if len(parts) < 3:
            bot.reply_to(message, "Usage: .raid <count> <text>")
            return

        count = int(parts[1])
        spam_text = parts[2]

        bot.reply_to(message, f"🚀 Spamming `{spam_text}` for `{count}` times...", parse_mode='Markdown')

        for i in range(count):
            bot.send_message(message.chat.id, spam_text)
            time.sleep(0.4)

    except Exception as e:
        bot.reply_to(message, f"Error: {e}")

print("🤖 Bot is running...")
bot.polling()
