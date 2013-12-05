# -*- coding:utf-8 -*-
import sqlite3 as lite
from settings import APPROVED_RESTAURANTS as my_restaurants
from connection import connection_factory


try:
    connection = connection_factory()
    cursor = connection.cursor()

    cursor.executescript("""
        DROP TABLE IF EXISTS Restaurant;
        CREATE TABLE Restaurant(Id INTEGER PRIMARY KEY, Name TEXT, Expensive NUMERIC, Times INTEGER DEFAULT 0);
    """)

    cursor.executemany("INSERT INTO Restaurant (Name, Expensive) VALUES(?, ?)", my_restaurants)

    connection.commit()

except lite.Error, e:
    if connection:
        connection.rollback()

        print "Error %s:" % e.args[0]

finally:
    if connection:
        connection.close()
