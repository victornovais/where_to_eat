# -*- coding: utf-8 -*-
from random import choice
from datetime import datetime
from settings import LIMIT_DATE
from connection import connection_factory


def has_money():
    today = datetime.now().day

    if today < LIMIT_DATE:
        return True

    return False

def fetch_restaurants():
    connection = connection_factory()
    cursor = connection.cursor()

    sql = "SELECT * FROM Restaurant WHERE Times = (SELECT MIN(Times) FROM Restaurant)"

    if not has_money():
        sql += " AND Expensive = 0"

    cursor.execute(sql)

    return cursor.fetchall()

def where_to_eat():
    restaurants = fetch_restaurants()
    chosen_one = choice(restaurants)

    print chosen_one



if __name__ == '__main__':
    where_to_eat()

