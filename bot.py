__author__ = '12345'
import telebot
import config
bot = telebot.TeleBot('291257487:AAEjpho3RF5tKC7HA2k38RSYInG0L2NDhS4')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет, как дела?")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()