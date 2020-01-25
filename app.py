from flask import Flask, render_template, request
from functions import getResult, listDoctors

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        eye = request.form['eye']
        result = getResult(eye)
        if result in [0, 1]:
            return 'You are safe'
        else:
            return render_template('public/doctors.html', result=result, doctors=listDoctors())
    else:
        return render_template('public/index.html')

@app.route('/contact/<doctorName>', methods=['GET'])
def contact(doctorName):
    return f'{doctorName} has received your appointment request'

if __name__ == '__main__':
    app.run()
