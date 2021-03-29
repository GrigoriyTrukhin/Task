import sqlite3
# coding=UTF-8


def create_orders_table(info):
    db = sqlite3.connect('orders.db')
    cur = db.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS orders
                    (order_id integer,
                    weight float,
                    region integer,
                    delivery_house text 
                    )
    """)

    cur.executemany("""INSERT INTO orders VALUES(?,?,?,?);""", info)

    db.commit()
    print('текст загружен в бд')
    sql = """
    SELECT  *
    FROM orders
    """
    cur.execute(sql)
    print(*cur.fetchall(), sep='\n')
    print('ЧТо?')