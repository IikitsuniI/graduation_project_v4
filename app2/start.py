from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import SelectField
import numpy as np
from pymongo import MongoClient

client = MongoClient()
collection = client["data_cars"]["update_cars"]


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'


allocation = {'BMW': ['BMW1', 'BMW2', 'BMW3'], 'Audi': ['Audi1', 'Audi2', 'Audi3']}

data_color = {'colors': ['--Выберите параметр--','Коричневый', 'Зелёный', 'Голубой', 'Бежевый', 'Золотой', 'Бордовый',
                        'Красный', 'Белый', 'Оранжевый','Пурпурный', 'Фиолетовый', 'Серый', 'Жёлтый', 'Серебряный',
                         'Синий', 'Чёрный']}

types_body = {'types_body': ['--Выберите параметр--', 'Универсал', 'Купе', 'Кабриолет', 'Внедорожник 5-дверный',
                             'Хетчбек 5-дверный', 'Лифтбек', 'Седан', 'Хетчбек 3-дверный']}

steering_wheel = {'steering_wheel': ['--Выберите параметр--', 'Левый', 'Правый']}
pts = {'pts': ['--Выберите параметр--', 'Оригинал', 'Дубликат']}
state = {'state': ['--Выберите параметр--', 'Не битый', 'Битый']}
types_engine = {'types_engine': ['--Выберите параметр--', 'Бензин', 'Дизель', 'Гибрид']}
transmission = {'transmission': ['--Выберите параметр--', 'Механика', 'Автомат', 'Вариатор', 'Робот']}
car_drive = {'car_drive': ['--Выберите параметр--', 'Передний', 'Задний', 'Полный']}
owners_by_pts = {'owners_by_pts': ['--Выберите параметр--', '1', '2', '3', '4', 'Более 4']}

# todo добавить поле для модификаций иописание и цена
# todo добавить литературу в док файл
class MyForm(FlaskForm):
    brand = SelectField('Brand', choices=['BMW', 'Audi'])
    models = SelectField('Model', choices=allocation['BMW'])
    colors = SelectField('Colors', choices=data_color['colors'])
    types_body = SelectField('Types_body', choices=types_body['types_body'])
    steering_wheel = SelectField('steering_wheel', choices=steering_wheel['steering_wheel'])
    pts = SelectField('Pts', choices=pts['pts'])
    state = SelectField('State', choices=state['state'])
    types_engine = SelectField('Types_engine', choices=types_engine['types_engine'])
    transmission = SelectField('Transmission', choices=transmission['transmission'])
    car_drive = SelectField('Car_drive', choices=car_drive['car_drive'])
    owners_by_pts = SelectField('Owners_by_pts', choices=owners_by_pts['owners_by_pts'])


@app.route('/test', methods=['GET', 'POST'])
def test():
    form = MyForm()
    if form.validate_on_submit():
        brand = form.brand.data
        form.models.choices = allocation[brand]
    return render_template('test.html', form=form)


@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyForm()
    if form.validate_on_submit():
        brand = form.brand.data
        form.models.choices = allocation[brand]
    return render_template('index.html', form=form)



if __name__ == '__main__':
    app.run(debug=True)