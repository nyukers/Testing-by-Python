# -*- coding: utf-8 -*-
import mysql.connector
#from fixture.db import DbFixture
from fixture.orm import ORMFixture

"""
connection = mysql.connector.connect(host="127.0.0.1", database="addressbook", user="root", password="")

try:
    cursor = connection.cursor()
    cursor.execute("select * from group_list")
    for row in cursor.fetchall():
        print(row)
except:
    print('Failed to connect')
finally:
    connection.close()


db = DbFixture(host="127.0.0.1", database="addressbook", user="root", password="")

try:
    groups = db.get_group_list()
    for group in groups:
        print(group)
    print(len(groups))
except:
    print('Failed to connect')
finally:
    db.destroy()
"""

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    l = db.get_group_list()
    for item in l:
        print(item)
    print(len(l))
except:
    print('Failed to connect')
finally:
    pass