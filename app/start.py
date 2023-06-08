from flask import Flask, render_template, request
from app.forms.car_form import *
from app.hander import MODELS
from predict_module.predictor import Predictor
from predict_module.features_predictor.predictor import *
from predict_module.desciption_predictor.predictor import *
from predict_module.modification_predictor.predictor import *
from predict_module.predictor import *


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
predictor = Predictor()


# todo добавить поле для модификаций иописание и цена
# todo добавить литературу в док файл

def _get_prediction(form):
    brand = form.brand.data
    form.models.choices = MODELS[brand]
    model = form.models.data
    print(brand, model)
    year = form.year.data
    breed = form.breed.data
    milage = form.milage.data
    milage_history = form.milage_history.data
    pts = form.pts.data
    n_owners = form.owners_by_pts.data
    condition = form.state.data
    engine_capacity = form.engine_capacity.data
    engine_type = form.types_engine.data
    transmission = form.transmission.data
    drive_unit = form.car_drive.data
    equipment = form.equipment.data
    body_type = form.types_body.data
    color = form.colors.data
    steering_wheel = form.steering_wheel.data
    modification = form.modification.data
    description = form.description.data
    predicted_price = predictor.predict(
        brand=brand, model=model, year=year, breed=breed, milage=milage, milage_history=milage_history, pts=pts,
        n_owners=n_owners, condition=condition, engine_capacity=engine_capacity, engine_type=engine_type,
        transmission=transmission, drive_unit=drive_unit, equipment=equipment, body_type=body_type, color=color,
        steering_wheel=steering_wheel, description=description, modification=modification
    )
    return predicted_price



def _is_too_difference(num1, num2):
    diff = abs(num1 - num2)
    avg = (num1 + num2) / 2
    percent_diff = (diff / avg) * 100
    return percent_diff > 20


def clf(num1, num2):
    try:
        num1 = int(num1.replace(' ', ''))
        num2 = int(num2.replace(' ', ''))
        if _is_too_difference(num1, num2) and num1 > num2:
            return 'Цена завышена'
        elif _is_too_difference(num1, num2) and num1 < num2:
            return 'Цена занижена'
        else:
            return 'Оптимальная цена'
    except:
        return "Цена не указана"


@app.route('/', methods=['GET', 'POST'])
def index():
    predicted_price, result = '', ''
    form = CarForm()
    if form.is_submitted():
        true_price = form.price.data
        predicted_price = _get_prediction(form)
        print(predicted_price)
        result = clf(true_price, predicted_price)
    return render_template('index.html', form=form, predicted_price=predicted_price, result=result)


@app.route('/test', methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        if request.form['submit_button'] == 'Button 1':
            # Обработка нажатия первой кнопки
            return 'Нажата первая кнопка'
        elif request.form['submit_button'] == 'Button 2':
            # Обработка нажатия второй кнопки
            return 'Нажата вторая кнопка'
    else:
        # Отображение формы
        return render_template('test.html')


if __name__ == '__main__':
    app.run(debug=True)