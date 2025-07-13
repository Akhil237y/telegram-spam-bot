
import telebot
import time
import os

# Telegram bot token (Render me environment variable ke roop me set hoga)
TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

# Har user ka apna spam text store karne ke liye
spam_text = {}

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    spam_text[user_id] = "Jai Shree Ram"  # default message
    bot.reply_to(
        message,
        "Welcome, dear! 😊 Akhil's Spam Bot ❤️ is ready to do something crazy! ☠️\n\n"
        "👉 Mujhe koi bhi message bhejo – wahi spam text ban jayega.\n"
        "🧨 Fir likho `.raid 5 @username` – spam chalu ho jayega!"
    )

@bot.message_handler(func=lambda message: True)
def handle_all(message):
    user_id = message.from_user.id
    text = message.text

    if text.startswith(".raid"):
        try:
            parts = text.split()
            count = int(parts[1])
            target = parts[2]

            for _ in range(count):
                bot.send_message(message.chat.id, f"{target} {spam_text.get(user_id, '💥')}")
                time.sleep(0.4)
        except:
            bot.reply_to(message, "❌ Format: .raid 5 @username")
    else:
        spam_text[user_id] = text
        bot.reply_to(message, f"✅ Saved your spam text: '{text}'\nNow send `.raid x @username` to begin.")

bot.polling()
