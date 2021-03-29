"""Принимает значение и обрабатывает для отправки в "update"."""
# coding=UTF-8
from couriesrs.prepeare import change
from couriesrs.change_id.update import update_bd

id = 2

new_info = {
    "regions": [11, 33, 2],
    "courier_type": "bike"
}


def check_upd(upd):
    for i in upd:
        if i == '' or i == []:
            return False
        return True


if check_upd(new_info):
    table_info = change(new_info)
    update_bd(table_info, id)
