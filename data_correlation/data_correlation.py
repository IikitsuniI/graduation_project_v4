# from preprocess_data.update_data import DataProcessing
# from preprocess_data.update_data_interface import DataProcessingInterface
import math

# x = [1, 2, 3]
# y = [4, 5, 6]


# def correlation_data(x, y, n):
#     xy = []
#     x2 = []
#     y2 = []
#     for i in range(len(x)):
#         xy.append(x[i] * y[i])
#         x2.append(x[i] ** 2)
#         y2.append(y[i] ** 2)
#     #     NΣXY - (ΣX)(ΣY) / Sqrt([NΣX2 - (ΣX)2][NΣY2 - (ΣY)2])
#     tmp_1 = (sum(xy) - ((sum(x) * sum(y)) / n)) / (math.sqrt((sum(x2) - ((sum(x) ** 2) / n))) * (sum(y2) - ((sum(y) ** 2) / n)))
#     # tmp_2 = (n * sum(xy) - ((sum(x) * sum(y)))) / (math.sqrt((n * sum(x2) - (sum(x) ** 2)) * (sum(y2) - (sum(y) ** 2))))
#     print(tmp_1)
#     # print(tmp_2)
#
#
# correlation_data(x, y, 3)


import numpy as np
from pymongo import MongoClient

# x = [1, 2, 3]
# y = [4, 5, 6]
client = MongoClient()
new_collection = client["data_cars"]["update_cars"]


def get_full_price():
    price = []
    for car in new_collection.find():
        tmp = car["Цена"]
        # if tmp is not:
        #     price.append(tmp)
    return price

# todo проверятьв одной функции сразу два массива и добавлять если оба не нан
def get_full_mileage():
    mileage = []
    for car in new_collection.find():
        tmp = car["Пробег"]
        if tmp != "None":
            mileage.append(tmp)
    return mileage


def correlation_data():
    price = get_full_price()
    mileage = get_full_mileage()
    r = np.corrcoef(np.array(price), np.array(mileage))[0][1]
    return r

print(correlation_data())
