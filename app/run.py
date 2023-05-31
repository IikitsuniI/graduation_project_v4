from predict_module.predictor import *
from predict_module.features_predictor.predictor import FeaturesModel
from predict_module.desciption_predictor.predictor import DescriptionModel
from predict_module.modification_predictor.predictor import ModificationModel


price = 6499000
brand = 'Audi'
model = 'Q7'
year = 2020.0
breed = ' 4M рестайлинг '
milage = 115000.0
milage_history = '9 записей в отчёте Автотеки'
pts = None
n_owners = 2
condition = 'Не битый'
modification = ' 45 TDI 3.0 quattro Tiptronic (249 л.с.)'
engine_capacity = 3.0
engine_type = ' Дизель'
transmission =  ' Автомат'
drive_unit = ' Полный'
equipment = ' Advance'
body_type = ' Внедорожник 5-дверный'
color = ' Серый'
steering_wheel = ' Левый'
description = None
link = 'https://www.avito.ru/sankt-peterburg/avtomobili/audi_q7_2020_2888631536'


predictor = Predictor()
res = predictor.predict(brand, model, year, breed, milage, milage_history,
                pts, n_owners, condition, engine_capacity, engine_type,
                transmission, drive_unit, equipment, body_type, color,
                steering_wheel, description, modification)
print(res)
