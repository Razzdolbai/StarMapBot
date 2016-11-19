__author__ = '12345'
#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

con = None

try:
    con = lite.connect('bot.db')

    cur = con.cursor()

    #Функция занесения вопроса в базу
    def add_queestion(usrquestion,usranswer):
        cur.execute("INSERT INTO questions (question,answer) VALUES ('%s','%s')"%(usrquestion,usranswer))
        con.commit()
    #Вводим данные
    question = input("Введите Логин\n")
    answer = input("Введите Пароль\n")
    print('\n')

    cur.execute('SELECT id FROM questions')

    data = cur.fetchall()

    print("SQLite version: %s" % data )

except lite.Error:

    print("Error %s:" % lite.Error.args[0])
    sys.exit(1)

finally:

    if con:
        con.close()
