__author__ = '12345'
import telebot
import config
import db
import requests

#соединение с ботом
bot = telebot.TeleBot(config.token)

#Отвечает на команды
@bot.message_handler(commands=['start'])
def send_welcome(message):
    query = "SELECT answer FROM questions WHERE id=1"
    result = db.query(query)
    result[0]
    print(result[0])
    bot.reply_to(message, result)

@bot.message_handler(commands=['help'])
def send_welcome(message):
    query = "SELECT answer FROM questions WHERE id=2"
    result = db.query(query)
    result[0]
    print(result[0])
    bot.reply_to(message, result)

#Отвечает на все сообщения по умолчанию
@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)

#Запуск бота
bot.polling()