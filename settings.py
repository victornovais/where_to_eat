# -*- coding:utf-8 -*-

# Approved restaurants must be here.
# Example: ('McDonalds', 0,) -> Not expensive
#          ('The Fifties', 1,) -> Expensive

APPROVED_RESTAURANTS = (
    ('Alma Carioca', 1),
    ('Montana Grill', 1),
    ('Otime', 0),
    ('Parme', 0),
    ('Mexicano', 0),
    ('Gourmet', 1),
    ('As meninas', 0),
    ('Imperial', 0),
    ('Colarinho', 1),
    ('Versao carioca', 1),
    ('Boteco 98', 0),
    ('Atrium', 0),
    ('Sabor e Recheio', 0),
    ('Chopp Time', 0),
    ('Escritorio', 1),
)

# This setting determines until what day of the month you're willing to pay more for better(or not) meal.
LIMIT_DATE = 10