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

# Функция для автоматической обработки координат
def location_auto(message):
    if message.location:# == "Всё автоматически":
        x = round(message.location.longitude, 3)
        y = round(message.location.latitude, 3)
        print (x, y)
        x *= -1  #Конвертирую долготу
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
        minute /= 60  #Конвертируем минуты
        time = "ut=" + str(round(hour + minute, 3))
        date = "&day=" + str(day) + "&month=" + str(month) + "&year=" + str(year)
        locate = "&longitude=" + str(x) + "&latitude=" + str(y)
        link = "http://www.astronet.ru/cgi-bin/skyc.cgi?" + time + date + locate + "&height=90&m=5.0&colstars=1"
        print(link)
        return 'Готово, перейдите по ссылке' \
               ' ' + link

# Функция ввода координат вручную
def location_by_heand(message):
    #message.text = 'Всё вручную'
    global questions1 #без этого всё и не работало
    global questions
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
    #return message.text
