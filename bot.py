__author__ = '12345'
import telebot
import config
import db


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

@bot.message_handler(commands=['about'])
def send_welcome(message):
    query = "SELECT answer FROM questions WHERE id=3"
    result = db.query(query)
    result[0]
    print(result[0])
    bot.reply_to(message, result)

from stars.request import generate_data
#Делаем клавиатуру
@bot.message_handler(commands = ['go'])
def generate_markup(message):
     markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
     markup.row('Взять текущее','Самостоятельно')
     bot.send_message(message.from_user.id, 'Взять текущее время или введёте сами?', reply_markup=markup)

from stars.request import generate_coord
@bot.message_handler(commands = ['next'])
def generate_marku2(message):
     markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
     markup.row('Текущие координаты','Самостоятельный ввод')
     bot.send_message(message.from_user.id, 'Взять текущие координаты или введёте сами?', reply_markup=markup)

# # Генератор звёздного неба
# @bot.message_handler(commands=['stars'])
# def send_welcome(message):
#     bot.reply_to(message, generate_data(message.text))

#Отвечает на все сообщения по умолчанию
@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, generate_data(message.text))
    #bot.reply_to(message, message.text)

#Запуск бота
bot.polling()