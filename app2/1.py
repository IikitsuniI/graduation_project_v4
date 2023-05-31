from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import SelectField


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'


allocation = {'BMW': ['BMW1', 'BMW2', 'BMW3'], 'Audi': ['Audi1', 'Audi2', 'Audi3']}


class MyForm(FlaskForm):

    brand = SelectField('Brand', choices=['BMW', 'Audi'])
    models = SelectField('Model', choices=allocation['BMW'])


@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyForm()
    if form.validate_on_submit():
        brand = form.brand.data
        form.models.choices = allocation[brand]
    return render_template('test.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)