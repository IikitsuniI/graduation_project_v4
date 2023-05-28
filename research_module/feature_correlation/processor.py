import numpy as np
from pymongo import MongoClient

# x = [1, 2, 3]
# y = [4, 5, 6]
client = MongoClient()
new_collection = client["data_cars"]["update_cars"]


#
def correlation_data(vector_1, vector_2):
    r = np.corrcoef(vector_1, vector_2)[0][1]
    return r


def process_mileage():
    price = []
    mileage = []
    for car in new_collection.find():
        if car["Цена"] and car["Пробег"]:
            price.append(car["Цена"])
            mileage.append(car["Пробег"])
    return "Кореляция цены и пробега: ", correlation_data(price, mileage)


def process_year_car():
    price = []
    year_car = []
    for car in new_collection.find():
        if car["Цена"] and car["Год выпуска"]:
            price.append(car["Цена"])
            year_car.append(car["Год выпуска"])
    return "Кореляция цены и года авто: ", correlation_data(price, year_car)


def process_car_generation():
    price = []
    car_generation = []
    white_data = {"unknown": 0}
    count = 0
    car_generation_update = []
    for car in new_collection.find():
        if car["Цена"] and car["Поколение"]:
            price.append(car["Цена"])
            car_generation.append(car["Поколение"])
    for el in car_generation:
        if el not in white_data:
            count += 1
            white_data[el] = count
    for el in car_generation:
        if el in white_data:
            car_generation_update.append(white_data[el])
        else:
            car_generation_update.append(white_data["unknown"])
    return "Кореляция цены и поколение: ", correlation_data(price, car_generation_update)


def process_pts():
    price = []
    pts = []
    white_data = {"unknown": 0}
    count = 0
    pts_update = []
    for car in new_collection.find():
        if car["Цена"] and car["ПТС"]:
            price.append(car["Цена"])
            pts.append(car["ПТС"])
    for el in pts:
        if el not in white_data:
            count += 1
            white_data[el] = count
    for el in pts:
        if el in white_data:
            pts_update.append(white_data[el])
        else:
            pts_update.append(white_data["unknown"])
    # return white_data
    return "Кореляция цены и ПТС: ", correlation_data(price, pts_update)
#     todo подумать над электронным птс


def process_owner_by_pts():
    price = []
    owner_by_pts = []
    white_data = {"unknown": 0}
    count = 0
    owner_by_pts_update = []
    for car in new_collection.find():
        if car["Цена"] and car["Владельцев по ПТС"]:
            price.append(car["Цена"])
            owner_by_pts.append(car["Владельцев по ПТС"])
    for el in owner_by_pts:
        if el not in white_data:
            count += 1
            white_data[el] = count
    for el in owner_by_pts:
        if el in white_data:
            owner_by_pts_update.append(white_data[el])
        else:
            owner_by_pts_update.append(white_data["unknown"])
    # return white_data
    return "Кореляция цены и владельцев по ПТС: ", correlation_data(price, owner_by_pts_update)


def process_state_car():
    price = []
    state_car = []
    white_data = {"unknown": 0}
    count = 0
    state_car_update = []
    for car in new_collection.find():
        if car["Цена"] and car["Состояние"]:
            price.append(car["Цена"])
            state_car.append(car["Состояние"])
    for el in state_car:
        if el not in white_data:
            count += 1
            white_data[el] = count
    for el in state_car:
        if el in white_data:
            state_car_update.append(white_data[el])
        else:
            state_car_update.append(white_data["unknown"])
    # return white_data
    return "Кореляция цены и состояние: ", correlation_data(price, state_car_update)


def process_modification():
    price = []
    modification = []
    white_data = {"unknown": 0}
    count = 0
    modification_update = []
    for car in new_collection.find():
        if car["Цена"] and car["Модификация"]:
            price.append(car["Цена"])
            modification.append(car["Модификация"])
    for el in modification:
        if el not in white_data:
            count += 1
            white_data[el] = count
    for el in modification:
        if el in white_data:
            modification_update.append(white_data[el])
        else:
            modification_update.append(white_data["unknown"])
    # return white_data
    return "Кореляция цены и модификация: ", correlation_data(price, modification_update)


def process_engine_capacity():
    price = []
    engine_capacity = []
    white_data = {"unknown": 0}
    count = 0
    engine_capacity_update = []
    for car in new_collection.find():
        if car["Цена"] and car["Объём двигателя"]:
            price.append(car["Цена"])
            engine_capacity.append(car["Объём двигателя"])
    for el in engine_capacity:
        if el not in white_data:
            count += 1
            white_data[el] = count
    for el in engine_capacity:
        if el in white_data:
            engine_capacity_update.append(white_data[el])
        else:
            engine_capacity_update.append(white_data["unknown"])
    # return white_data
    return "Кореляция цены и объём двигателя: ", correlation_data(price, engine_capacity_update)


def process_engine_type():
    price = []
    engine_type = []
    white_data = {"unknown": 0}
    count = 0
    engine_type_update = []
    for car in new_collection.find():
        if car["Цена"] and car["Тип двигателя"]:
            price.append(car["Цена"])
            engine_type.append(car["Тип двигателя"])
    for el in engine_type:
        if el not in white_data:
            count += 1
            white_data[el] = count
    for el in engine_type:
        if el in white_data:
            engine_type_update.append(white_data[el])
        else:
            engine_type_update.append(white_data["unknown"])
    # return white_data
    return "Кореляция цены и тип двигателя: ", correlation_data(price, engine_type_update)


def process_transmission_car():
    price = []
    transmission_car = []
    white_data = {"unknown": 0}
    count = 0
    transmission_car_update = []
    for car in new_collection.find():
        if car["Цена"] and car["Коробка передач"]:
            price.append(car["Цена"])
            transmission_car.append(car["Коробка передач"])
    for el in transmission_car:
        if el not in white_data:
            count += 1
            white_data[el] = count
    for el in transmission_car:
        if el in white_data:
            transmission_car_update.append(white_data[el])
        else:
            transmission_car_update.append(white_data["unknown"])
    # return white_data
    return "Кореляция цены и коробка передач: ", correlation_data(price, transmission_car_update)


def process_drive_unit():
    price = []
    drive_unit = []
    white_data = {"unknown": 0}
    count = 0
    drive_unit_update = []
    for car in new_collection.find():
        if car["Цена"] and car["Привод"]:
            price.append(car["Цена"])
            drive_unit.append(car["Привод"])
    for el in drive_unit:
        if el not in white_data:
            count += 1
            white_data[el] = count
    for el in drive_unit:
        if el in white_data:
            drive_unit_update.append(white_data[el])
        else:
            drive_unit_update.append(white_data["unknown"])
    # return white_data
    return "Кореляция цены и привод: ", correlation_data(price, drive_unit_update)


def process_equipment_car():
    price = []
    equipment_car = []
    white_data = {"unknown": 0}
    count = 0
    equipment_car_update = []
    for car in new_collection.find():
        if car["Цена"] and car["Комплектация"]:
            price.append(car["Цена"])
            equipment_car.append(car["Комплектация"])
    for el in equipment_car:
        if el not in white_data:
            count += 1
            white_data[el] = count
    for el in equipment_car:
        if el in white_data:
            equipment_car_update.append(white_data[el])
        else:
            equipment_car_update.append(white_data["unknown"])
    # return white_data
    return "Кореляция цены и комплектация: ", correlation_data(price, equipment_car_update)


def process_body_type_car():
    price = []
    body_type_car = []
    white_data = {"unknown": 0}
    count = 0
    body_type_car_update = []
    for car in new_collection.find():
        if car["Цена"] and car["Тип кузова"]:
            price.append(car["Цена"])
            body_type_car.append(car["Тип кузова"])
    for el in body_type_car:
        if el not in white_data:
            count += 1
            white_data[el] = count
    for el in body_type_car:
        if el in white_data:
            body_type_car_update.append(white_data[el])
        else:
            body_type_car_update.append(white_data["unknown"])
    # return white_data
    return "Кореляция цены и тип кузова: ", correlation_data(price, body_type_car_update)


def process_car_color():
    price = []
    car_color = []
    white_data = {"unknown": 0}
    count = 0
    car_color_update = []
    for car in new_collection.find():
        if car["Цена"] and car["Цвет"]:
            price.append(car["Цена"])
            car_color.append(car["Цвет"])
    for el in car_color:
        if el not in white_data:
            count += 1
            white_data[el] = count
    for el in car_color:
        if el in white_data:
            car_color_update.append(white_data[el])
        else:
            car_color_update.append(white_data["unknown"])
    # return white_data
    return "Кореляция цены и цвет: ", correlation_data(price, car_color_update)


def process_steering_wheel_car():
    price = []
    steering_wheel_car = []
    white_data = {"unknown": 0}
    count = 0
    steering_wheel_car_update = []
    for car in new_collection.find():
        if car["Цена"] and car["Руль"]:
            price.append(car["Цена"])
            steering_wheel_car.append(car["Руль"])
    for el in steering_wheel_car:
        if el not in white_data:
            count += 1
            white_data[el] = count
    for el in steering_wheel_car:
        if el in white_data:
            steering_wheel_car_update.append(white_data[el])
        else:
            steering_wheel_car_update.append(white_data["unknown"])
    # return white_data
    return "Кореляция цены и руль: ", correlation_data(price, steering_wheel_car_update)


# print(process_mileage())
# print(process_year_car())
# print(process_car_generation())
# print(process_pts())
# print(process_owner_by_pts())
# print(process_state_car())
# print(process_modification())
# print(process_engine_capacity())
# print(process_engine_type())
# print(process_transmission_car())
# print(process_drive_unit())
# print(process_equipment_car())
# print(process_body_type_car())
# print(process_car_color())
# print(process_steering_wheel_car())


# print(process_steering_wheel_car())

# todo года поколения, описание, история пробега, ссылка, название авто - их не корелировал