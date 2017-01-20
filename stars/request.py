__author__ = '12345'
import datetime
import telebot
import config
import urllib.request

bot = telebot.TeleBot(config.token)

link = ''
l2 = ['http://www.astronet.ru/cgi-bin/skyc.cgi?ut=', '&day=', '&month=', '&year=', '&longitude=', '&latitude=', '&height=90&m=5.0&colstars=1']

answers = []
questions1 = ["Введите час: ", "Введите минуту: ", "Введите день: ", "Введите месяц: ", "Введите год (полностью): ",
             "Долгота градусы:('-' для вост.): ", "Широта градусы:('-' для южн.): "]
questions = questions1[:]
#Функция ввода даты и времени
def generate_data(message):

    global questions1 #без этого всё и не работало
    global questions
    if message == "Всё автоматически":
        x = message.location.longitude
        y = message.location.latitude
        print (x, y)
        cur_date = datetime.datetime.now()  #Берём текущее время (Питер, прувет!)
        hour = cur_date.hour  #Выделяем текущий час
        minute = cur_date.minute  #текущую минуту
        day = cur_date.day  # текущий день
        month = cur_date.month  #текущий месяц
        year = cur_date.year  #текущий год
        # должен находить координаты но не находит
        hour -= 3  #Конвертируем часы в UT
        if hour < 0:
            hour += 24  #Чтобы не было отрицательного часа
        minute /= 0.6  #Конвертируем минуты, чуть-чуть не так работает, если минуты меньше 10
        time = "ut=" + str(hour) + '.' + str(int(minute))
        date = "&day=" + str(day) + "&month=" + str(month) + "&year=" + str(year)
        link = time + date
        print(link)
        return "Данные введены. Обрабатываю, подождите "
        # bot.send_chat_action(message.from_user.id, 'find_location')
        # bot.send_message(message.from_user.id, loc)

    if message == "Всё вручную":
        # questions = ["Введите час: ", "Введите минуту: ", "Введите день: ", "Введите месяц: ", "Введите год: ",
        #       "Долгота градусы ('-' для вост.): ", "Широта градусы ('-' для южн.): "]
        q = questions[0]
        questions.remove(q)
        return q
    elif not questions:
        answers.append(message)
        print(answers)
        answers.append('')  # Добавляет строчку в список для правильной генерации
        hrs = int(answers[0])
        hrs -= 3  #Конвертируем часы в UT
        if hrs < 0:
            hrs += 24  #Чтобы не было отрицательного часа
        mins = int(answers[1])
        mins /= 60
        ut = str(round(hrs + mins, 3))  # Теперь должно правильно работать
        #Тут должен быть конвертер. Но его пока не будет.
        #удаляем первые два элемента списка
        i = 0
        while i < 2:
            del answers [0]
            i += 1
        #вставляем вперёд списка новое значение
        answers.insert(0, ut)
        l = [x + y for x,y in zip(l2,answers)]  #Объединяет списки
        link = ''.join(l)  #Преобразовывает список в строку
        print (link)
        #Вот тут должна быть загрузка фото в диалог, но бот тут падает
        # urllib.request.urlretrieve(link, '1.jpg')
        # img = open('1.jpg', 'rb')
        # bot.send_chat_action(message.from_user.id, 'upload_photo')  #По задумке должен загрузить фотку, но падает
        # bot.send_photo(message.from_user.id, img)
        # img.close()
        questions = questions1[:] # копируем список для того, чтобы всё начать заново
        answers.clear() # очищаем список ответов
        return 'Готово, перейдите по ссылке' \
               ' ' + link
    else:
        answers.append(message)
        q = questions[0]
        questions.remove(q)
        return q
#         hour = message"Введите час: "))
#         minute = int(input("Введите минуту: "))
#         day = int(input("Введите день: "))
#         month = int(input("Введите месяц: "))
#         year = int(input("Введите год: "))
#
#         Думаю, пока можно не реализовывать полуавтоматический ввод
#     if message == 'Время вручную, координаты автоматически':
#         question = ["Введите часик: ", "Введите минуту: ", "Введите день: ", "Введите месяц: ", "Введите год: "]
#         q = question[0]
#         question.remove(q)
#         return q
#         answers.append(message)
#         return answers
#
#
# def generate_data_auto(message):
#
# def generate_data_half(message):
#
#     else:
#         return "Ничего не понял, попробуйте ещё раз, введите команду /go"
#     hour -= 3 #Конвертируем часы в UT
#     if hour < 0:
#         hour += 24 #Чтобы не было отрицательного часа
#     minute /= 0.6  #Конвертируем минуты
#     time = "ut=" + str(hour) + '.' + str(int(minute))
#     date = "&day=" + str(day) + "&month=" + str(month) + "&year=" + str(year)
#     link = time + date
#     print(link)
#     print(answers)
#     return "Данные введены нажмите для продолжения ввода "
