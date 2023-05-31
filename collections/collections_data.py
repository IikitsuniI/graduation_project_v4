import numpy as np
from pymongo import MongoClient

client = MongoClient()
collection = client["data_cars"]["update_cars"]

def fill_color():
    colors = set()
    new_collection = client["data_cars"]["colors"]
    for car in collection.find():
        if 'Цвет' in car:
            color = car['Цвет']
            if color is not None:
                colors.add(color)
    print(colors)
    # for color in colors:
    #     new_collection.insert_one({"color": color})

def fill_models():
    allocation = {}
    for car in collection.find():
        if 'Автомобиль' in car:
            car = car['Автомобиль']
            brand = car[:car.index(' ')].strip()
            model = car[car.index(' '):car.index(',')].strip()
            if brand not in allocation:
                allocation[brand] = set()
            allocation[brand].add(model)
    for brand in allocation:
        new_collection = client['data_cars'][brand]
        for model in allocation[brand]:
            new_collection.insert_one({"model": model})


def fill_type_body():
    types_body = set()
    new_collection = client["data_cars"]["types_body"]
    for car in collection.find():
        if 'Тип кузова' in car:
            type_body = car['Тип кузова']
            if type_body is not None:
                types_body.add(type_body)
    print(types_body)
    # for type_body in types_body:
    #     new_collection.insert_one({"type_body": type_body})


# fill_color()
# fill_models()
fill_type_body()