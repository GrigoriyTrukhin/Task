"""Здесь принимается Json и проверяются полученные данные:
    всё ли в порядке, если да - вызывет "prepeare_orders.py", которая отправляет в бд (SQL)
"""
import json
from prepeare_orders import change_type
from pprint import pprint

way = 'C:/Users/Григорий/PycharmProjects/YandexProject/orders/database/db_orders.json'  # файл с сервера
with open(way, 'r', encoding='utf-8') as outfile:
    text = json.load(outfile)  # начинаем обрабатывать json

print(text)
couriers_types = ['foot', 'bike', 'car']
good = set()
bad = set()
to_table = []


def result_bad(i):
    bad.add(i['order_id'])


def result_good(i):
    good.add(i['order_id'])


# Проверяет правильность принятых данных

def check(text_js):
    for i in text_js['data']:

        try:
            if i['order_id'] <= 0:
                result_bad(i)
            if i['weight'] < 0:
                result_bad(i)
            if i['region'] <= 0:
                result_bad(i)
            if type(i['delivery_hours']) != list or i['delivery_hours'] == []:
                result_bad(i)
            else:
                result_good(i)

        except KeyError:
            try:
                result_bad(i)
            except KeyError:
                bad.add('No change_id')

    if bad == set():
        print('прошли проверку, идём дальше')
        return True
    return False


# Возвращает результат работы и при успехе загружает в бд

def main():
    print('Начинаю работать с Json текст')
    if check(text):
        change_type(text['data'])
        return {'couriers': [{'change_id': i} for i in good]
                }
    return {'validation_error': {
        'couriers': [{'change_id': i} for i in bad]
    }
    }


main()
