# -*- coding: utf-8 -*-
from settings import approved_restaurants as my_restaurants
from random import choice


def where_to_eat():
    chosen_one = choice(my_restaurants)
    print chosen_one['name']



if __name__ == '__main__':
    where_to_eat()

