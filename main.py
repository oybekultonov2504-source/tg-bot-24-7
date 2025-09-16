import telebot
import os

TOKEN = os.getenv("BOT_TOKEN")  # бот будет брать токен из переменных окружения
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "Привет! Я работаю 24/7 в облаке 🚀")

@bot.message_handler(func=lambda m: True)
def echo(message):
    bot.reply_to(message, f"Ты написал: {message.text}")

print("Бот запущен...")
bot.infinity_polling()
