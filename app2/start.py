from flask import Flask, render_template, request
from forms.car_form import CarForm

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/test')
def test():
    form = CarForm()
    if request.method == 'POST' and form.validate():
        print(form.test.data)
    return render_template('test.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
