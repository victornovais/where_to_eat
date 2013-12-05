# -*- coding:utf-8 -*-
import sqlite3 as lite


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

# Factory to connect to database and to change the result set of fetch to a dict
def connection_factory():
    connection = lite.connect('restaurant.db')
    connection.row_factory = dict_factory

    return connection


