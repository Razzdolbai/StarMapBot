__author__ = '12345'
import datetime
# import telebot
# from bot import bot

answers = []
questions = ["Введите час: ", "Введите минуту: ", "Введите день: ", "Введите месяц: ", "Введите год: "]

#Делаем клавиатуру
#@bot.message_handler(commands=['go'])
def generate_data(message):
    # markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    # markup.row('Взять текущее', 'Самостоятельно')
    # bot.send_message(message.from_user.id, 'Взять текущее время или введёте сами?', reply_markup=markup)
    #def generate_data(message):
    # if message == "/stars":
    #     return "Взять текущее время (0) или введёте сами (1)?"
    # # # elif (message == 0 or message == 1):
    # # #     q = questions[0]
    # # #     questions.remove(q)
    # # #     return q
    # else:
    # # Этот кусок кода выше скорее бесполезен

    if message == 'Самостоятельно':
        q = questions[0]
        questions.remove(q)
        return q
        #a = answers[0]
        answers.append(message)
        # hour = message"Введите час: "))
        minute = int(input("Введите минуту: "))
        day = int(input("Введите день: "))
        month = int(input("Введите месяц: "))
        year = int(input("Введите год: "))
    elif message == 'Взять текущее':
        cur_date = datetime.datetime.now()  #Берём текущее время
        hour = cur_date.hour  #Выделяем текущий час
        minute = cur_date.minute  #текущую минуту
        day = cur_date.day  # текущий день
        month = cur_date.month  #текущий месяц
        year = cur_date.year  #текущий год
    else:
        return "Ничего не понял, попробуйте ещё раз, введите команду /go"
    hour -= 3  #Конвертируем время в UT
    minute /= 0.6  #Конвертируем минуты
    time = "ut=" + str(hour) + '.' + str(int(minute))
    date = "&day=" + str(day) + "&month=" + str(month) + "&year=" + str(year)
    link = time + date
    print(link)
