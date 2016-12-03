__author__ = '12345'
import datetime

choice = int(input("Взять текущее (0) или введёте сами (1)?"))
if choice == 1:
    hour = int(input("Введите час: "))
    minute = int(input("Введите минуту: "))
    day = int(input("Введите день: "))
    month = int(input("Введите месяц: "))
    year = int(input("Введите год: "))
else:
    cur_date = datetime.datetime.now() #Берём текущее время
    hour = cur_date.hour #Выделяем текущий час
    minute = cur_date.minute #текущую минуту
    day = cur_date.day #текущий день
    month = cur_date.month #текущий месяц
    year = cur_date.year #текущий год
hour -= 3 #Конвертируем время в UT
minute /= 0.6 #Конвертируем минуты
time = "ut="+ str(hour) + '.' + str(int(minute))
date = "&day=" + str(day) + "&month=" + str(month) + "&year=" + str(year)
link = time + date
print(link)

