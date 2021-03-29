import sqlite3
# coding=UTF-8


def create_couriers_table(info):
    print(info)
    db = sqlite3.connect('couriers.db')
    cur = db.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS couriers
                    (courier_id integer,
                    courier_type text,
                    regions text,
                    working_hours text 
                    )
    """)

    cur.executemany("""INSERT INTO couriers VALUES(?,?,?,?);""", info)

    db.commit()
    print('текст загружен в бд')
    sql = """
    SELECT  *
    FROM couriers 
    """
    cur.execute(sql)
    print(*cur.fetchall(), sep='\n')
    print('ЧТо?')