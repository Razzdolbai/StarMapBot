__author__ = '12345'
import telebot
import config
import db
import stars.request as sr


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
     markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
     #Временно
     hand = telebot.types.KeyboardButton(text='Всё вручную')

     auto = telebot.types.KeyboardButton(text="Всё автоматически")# Отдельная кнопка с возможностью получения координат''', request_location=True'''
     halfauto = telebot.types.KeyboardButton(text="Время вручную, координаты автоматически", request_location=True)
     markup.row(hand, auto)
     markup.row(halfauto)
     #markup.row('Всё вручную', 'Всё автоматически')
     # #markup.row('Время вручную, координаты автоматически')
     bot.send_message(message.from_user.id, 'Взять текущее время (только для Санкт-Петербурга) и координаты (только для '
                                            'устройств с навигацией) или введёте сами?', reply_markup=markup)

#Отвечает на все сообщения по умолчанию
@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, generate_data(message.text))
    bot.reply_to(message, sr.generate_data_auto(message.text))
    bot.reply_to(message, sr.generate_data_half(message.text))
    # #bot.reply_to(message, message.text)

#Запуск бота
bot.polling()