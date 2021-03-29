""" Обновление данных о курьере по change_id """
import sqlite3

way = 'C:/Users/Григорий/PycharmProjects/YandexProject/couriesrs/couriers.db'
# coding=UTF-8
db = sqlite3.connect(way)
cur = db.cursor()


def update_bd(new_info, id):
    for i in new_info:
        sql_update = f"""
    UPDATE couriers 
    SET {i} = '{new_info[i]}'
    WHERE courier_id = {id} 
    """
        cur.execute(sql_update)
        db.commit()

    sql = f"""
    SELECT *
    FROM couriers
    WHERE courier_id = {id}
    """

    cur.execute(sql)
    print(*cur.fetchall(), sep='\n')