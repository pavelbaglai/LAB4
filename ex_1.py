#!/usr/bin/env python3
from librip.gens import *

goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
    {'title': 'Стелаж', 'price': 7000, 'color': 'white'},
    {'title': 'Вешалка для одежды', 'price': 800, 'color': 'white'}
]

g1 = field(goods, 'title')
print(' '.join(map(str, g1)))
g2 = field(goods, 'title', 'price')
print(' '.join(map(str, g2)))
g3 = gen_random(1,5,4)
print(' '.join(map(str, g3)))
