import numpy as np
from pymongo import MongoClient


client = MongoClient()
new_collection = client["data_cars"]["update_cars"]


def get_full_price():
    price = []
    for car in new_collection.find():
        tmp = car["Цена"]
        # if tmp is not:
        #     price.append(tmp)
    return price


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
