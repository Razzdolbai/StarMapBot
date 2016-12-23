__author__ = '12345'
import datetime
import telebot
import config
bot = telebot.TeleBot(config.token)
# from bot import bot

answers = []
# questions = ["Введите час: ", "Введите минуту: ", "Введите день: ", "Введите месяц: ", "Введите год: ",
#              "Долгота градусы:('-' для вост.): ", "Долгота минуты: ", "Широта градусы:('-' для южн.): ", "Широта минуты: "]

#Делаем клавиатуру
#@bot.message_handler(commands=['go'])
#Функция ввода даты и времени
def generate_data(message):
    if message == "Всё вручную":
        questions = ["Введите час: ", "Введите минуту: ", "Введите день: ", "Введите месяц: ", "Введите год: ",
              "Долгота градусы ('-' для вост.): ", "Широта градусы ('-' для южн.): "]
        q = questions[0]
        questions.remove(q)
        return q
        #a = answers[0]
        answers.append(message)
        return answers
        # hour = message"Введите час: "))
        # minute = int(input("Введите минуту: "))
        # day = int(input("Введите день: "))
        # month = int(input("Введите месяц: "))
        # year = int(input("Введите год: "))

    elif message == 'Всё автоматически':
        cur_date = datetime.datetime.now()  #Берём текущее время (Питер, прувет!)
        hour = cur_date.hour  #Выделяем текущий час
        minute = cur_date.minute  #текущую минуту
        day = cur_date.day  # текущий день
        month = cur_date.month  #текущий месяц
        year = cur_date.year  #текущий год
        # должен находить координаты но не находит
        loc = ''
        bot.send_chat_action(message.from_user.id, 'find_location')
        bot.send_message(message.from_user.id, loc)

    elif message == 'Время вручную, координаты автоматически':
        questions = ["Введите час: ", "Введите минуту: ", "Введите день: ", "Введите месяц: ", "Введите год: "]
        q = questions[0]
        questions.remove(q)
        return q
        answers.append(message)
        return answers

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
    return "Данные введены нажмите /next для продолжения ввода " + link + loc

#Функция ввода координат (реализовано по другому)
# def generate_loc(message):
#     questions = ["Долгота градусы:('-' для вост.): ", "Долгота минуты: ", "Широта градусы:('-' для южн.): ", "Широта минуты: "]
#     if message == 'Самостоятельный ввод':
#         q = questions[0]
#         questions.remove(q)
#         return q
#         answers.append(message)
#         return answers
#     elif message == 'Текущие координаты':
#         pass
#     else:
#         return "Ничего не понял, попробуйте ещё раз, введите команду /next"
#     return "Данные введены нажмите"