__author__ = '12345'
#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

con = None

try:
    con = lite.connect('bot.db')

    cur = con.cursor()
    cur.execute('SELECT id FROM questions')

    data = cur.fetchall()

    print("SQLite version: %s" % data )

except lite.Error:

    print("Error %s:" % lite.Error.args[0])
    sys.exit(1)

finally:

    if con:
        con.close()