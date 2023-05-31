from flask_wtf import FlaskForm
from wtforms.validators import InputRequired
from wtforms import SelectField, StringField, TextAreaField, SubmitField
from app.hander import *


class CarForm(FlaskForm):
    brand = SelectField('Марка', choices=BRANDS)
    models = SelectField('Модель', choices=MODELS['BMW'])
    colors = SelectField('Цвет', choices=COLORS)
    types_body = SelectField('Кузов', choices=TYPE_BODY)
    steering_wheel = SelectField('Руль', choices=STEERING_WHEEL)
    pts = SelectField('ПТС', choices=PTS)
    state = SelectField('Состояние', choices=CONDITION)
    types_engine = SelectField('Тип двигателя', choices=ENGINE_TYPE)
    transmission = SelectField('Коробка передач', choices=TRANSMISSION)
    car_drive = SelectField('Привод', choices=DRIVE_UNIT)
    owners_by_pts = SelectField('Количество владельцев', choices=N_OWNERS)
    year = StringField('Год выпуска')
    milage = StringField('Пробег')

    breed = StringField('Поколение')
    milage_history = StringField('История пробега')
    engine_capacity = StringField('Объём двигателя')
    equipment = StringField('Комплектация')
    modification = StringField('Модификации')
    description = TextAreaField('Описание')
    price = StringField('Цена', validators=[InputRequired()])

    submit = SubmitField()
