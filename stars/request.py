__author__ = '12345'
import datetime
# import telebot
# from bot import bot

answers = []
questions = ["Введите час: ", "Введите минуту: ", "Введите день: ", "Введите месяц: ", "Введите год: "]

#Делаем клавиатуру
#@bot.message_handler(commands=['go'])
#Функция ввода даты и времени
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
        return answers
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
    if hour - 3 < 0:
        hour += 24 #Чтобы не было отрицательного часа
    hour -= 3 #Конвертируем часы в UT
    minute /= 0.6  #Конвертируем минуты
    time = "ut=" + str(hour) + '.' + str(int(minute))
    date = "&day=" + str(day) + "&month=" + str(month) + "&year=" + str(year)
    link = time + date
    print(link)
    return "Данные введены нажмите /next для продолжения ввода" + link

#Функция ввода координат
def generate_coord(message):
    questions = ["Долгота градусы:('-' для вост.): ", "Долгота минуты: ", "Широта градусы:('-' для южн.): ", "Широта минуты: "]
    if message == 'Самостоятельный ввод':
        q = questions[0]
        questions.remove(q)
        return q
        answers.append(message)
        return answers
    elif message == 'Текущие координаты':
        pass
    else:
        return "Ничего не понял, попробуйте ещё раз, введите команду /next"
