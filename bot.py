__author__ = '12345'
import telebot
import config
import db
import stars.request as sr
import urllib.request


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
@bot.message_handler(commands=['go'])
def generate_markup(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    hand = telebot.types.KeyboardButton(text='Всё вручную')
    auto = telebot.types.KeyboardButton(text="Всё автоматически", request_location=True)  # Отдельная кнопка с возможностью получения координат''', request_location=True'''
    #halfauto = telebot.types.KeyboardButton(text="Время вручную, координаты автоматически", request_location=True) #пока не будет работать
    markup.row(hand, auto) #Генерим клаву
    #markup.row(halfauto)
    bot.send_message(message.from_user.id, 'Взять текущее время (только для Санкт-Петербурга) и координаты (только для '
                                           'устройств с навигацией) или введёте сами?', reply_markup=markup)

#Отвечает на все сообщения по умолчанию
@bot.message_handler(func=lambda m: True, content_types=['location', 'text'])
# def echo_all(message):
#     #print (message.location.longitude) #Вот это и то, что ниже принтит координаты. не знаю, как их передать программе
#     #print (message.location.latitude)
#     bot.reply_to(message, generate_data(message.text))
def echo_all(message):
    from stars.request1 import location_auto, location_by_heand

    if message.location:
        bot.send_message(message.from_user.id, location_auto(message))
    else: #message.text == 'Всё вручную':
        #bot.reply_to(message, location_by_heand(message.text))
        bot.send_message(message.from_user.id, location_by_heand(message.text))
    #else:
       # bot.send_message(message.from_user.id, 'Я не разобрал запрос, вот клавиатура еще раз', reply_markup=keyboard(message))

#Запуск бота
bot.polling()