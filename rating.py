# {
# "courier_id": 2,
# "courier_type": "foot",
# "regions": [11, 33, 2],
# "working_hours": ["09:00-18:00"],
# "rating": 4.93,
# "earnings": 10000
# } - ПРИМЕР ОТВЕТА
import math

#sum = ∑(500 * C),
coef = {'foot': 2,
        'bike': 5,
        'car': 15
        }

reating =  (60*60 - min(t, 60*60))/(60*60) * 5