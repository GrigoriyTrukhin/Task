"""Обработка данных, подготовка к загрузке в бд"""
from couriesrs.database.create_sql import create_couriers_table


def change_type(text): # принимает список словарей с характеристиками
    text = add(text)
    for courier_info in text:
        courier_info = change(courier_info)
    do_table(text)


def add(text_list):
    full_list = []
    for courier in range(len(text_list)):
        to_add = text_list.pop(courier)
        print(to_add)
        for i in range(len(to_add['regions'])):
            print(i)
            print(to_add['regions'][i])
            for j in range(len(to_add['working_hours'])):
                to_add['regions'] = to_add['regions'][i]
                to_add['working_hours'] = to_add['working_hours'][j]
                full_list.append(to_add)
    print(full_list)
    return full_list


def do_table(text):    # переводит все данные в кортежи, для отправки в sql
    table_text = []
    for data in text:
        n = tuple(data[i] for i in data)
        table_text.append(n)
    print('текст изменён, готов к загрузке в бд')
    create_couriers_table(table_text)  #вызывает загрузку в sql
    return table_text


def change(data_dict):  # обрабатывает словарь с характеристиками
    for info in data_dict:            # Список в строку
        if type(data_dict[info]) == list:
            data_dict[info] = ', '.join([str(i) for i in data_dict[info]])
    return data_dict

