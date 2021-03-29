"""Обработка данных, подготовка к загрузке в бд"""
from orders.database.create_sql import create_orders_table


def change_type(text):            # принимает список словарей с характеристиками
    for courier_info in text:
        courier_info = change(courier_info)
    do_table(text)


def do_table(text):    # переводит все данные в кортежи, для отправки в sql
    table_text = []
    for data in text:
        n = tuple(data[i] for i in data)
        table_text.append(n)
    print('текст изменён, готов к загрузке в бд')
    create_orders_table(table_text)  #вызывает загрузку в sql
    return table_text


def change(data_dict):                # обрабатывает словарь с характеристиками
    for info in data_dict:            # Список в строку
        if type(data_dict[info]) == list:
            data_dict[info] = ', '.join([str(i) for i in data_dict[info]])
    return data_dict

