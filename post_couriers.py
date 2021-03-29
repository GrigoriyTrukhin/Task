"""Здесь принимается Json и проверяются полученные данные:
    всё ли в порядке, если да - вызывет "prepeare_orders.py", которая отправляет в бд (SQL)
"""
import json
from prepeare import change_type
from pprint import pprint

way = 'C:/Users/Григорий/PycharmProjects/YandexProject/couriesrs/database/db_couriers.json'  # файл с сервера
with open(way, 'r', encoding='utf-8') as outfile:
    text = json.load(outfile)  # начинаем обрабатывать json

couriers_types = ['foot', 'bike', 'car']
good = set()
bad = set()
to_table = []


def result_bad(i):
    bad.add(i['courier_id'])


def result_good(i):
    good.add(i['courier_id'])


# Проверяет правильность принятых данных

def check(text_js):
    for i in text_js['data']:

        try:
            if i['courier_id'] <= 0:
                result_bad(i)
            if i['courier_type'] not in couriers_types:
                result_bad(i)
            if type(i['regions']) != list:
                result_bad(i)
            if type(i['working_hours']) != list or i['working_hours'] == []:
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
