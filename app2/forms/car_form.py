from wtforms import Form, SelectField


class CarForm(Form):
    model = SelectField(u'Programming Language', choices=['honda', 'bmw', 'lada'])