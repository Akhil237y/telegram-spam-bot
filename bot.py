from pyrogram import Client, filters

API_ID = 21073191
API_HASH = "272a189777e9c47af345a0dd52b1f0f9"
BOT_TOKEN = "8111757881:AAG-kuKRjphQi_E_vxMKJjgwbk806NYHFqY"

bot = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@bot.on_message(filters.command("start"))
async def start(client, message):
    await message.reply("🔥 बॉट चल रहा है!")

print("Bot Started!")
bot.run()
