#!/usr/bin/env python3
import json
import sys
from librip.ctxmngrs import timer
from librip.decorators import print_result
from librip.gens import field, gen_random
from librip.iterators import Unique as unique
import re

path = r"data_light_cp1251.json"



with open(path) as f:
    data = json.load(f)



@print_result
def f1(arg):
    return list(unique(field(arg, 'job-name'), ignore_case=True))


@print_result
def f2(arg):
    return list(filter(lambda x: re.match("^[п,П]программист", x) is not None, arg))


@print_result
def f3(arg):
    return list(map(lambda x: x+" опыт Python", arg))


@print_result
def f4(arg):
    li = list(zip(arg, list(gen_random(100000, 200000, len(arg)))))
    return list(map(lambda x: x[0]+",зарплата "+str(x[1])+" руб", li))


with timer():
    f4(f3(f2(f1(data))))


