from flask import Blueprint, render_template, request, abort
from datetime import datetime
import requests
from .validator import Validator, ValidError

app1 = Blueprint('app1', __name__, template_folder='template')


@app1.route('/time')
def time():
    now = str(datetime.now().isoformat('#'))
    return f'<center><strong><font size="10" color="red">{now}</font></strong></center>'


@app1.route('/quote')
def quote():
    for key, value in request.args.items():
        q = value
        just_lst = []
        if q is None:
            r = requests.get('https://api.kanye.rest')
            for value in r.json().values():
                just_lst.append(value)
                return render_template('index.html', just_lst=just_lst)
        elif int(q) > 0:
            i = 1
            while i <= int(q):
                r = requests.get('https://api.kanye.rest')
                for value in r.json().values():
                    just_lst.append(value)
                i += 1
            return render_template('index.html', just_lst=just_lst)


@app1.route('/register', methods=["POST","GET"])
def register():
    if request.method == 'POST':
        username = request.form.get('username')  # запрос к данным формы
        password = request.form.get('password')
        email = request.form.get('email')
        validator_1 = Validator(username, password, email)  
        if validator_1.valid():
            abort(405)
        else:
            ValidError  
            abort(404)  
    return render_template('login.html')

@app1.errorhandler(405)
def valid_accept(error):
    return 'All good', 405


@app1.errorhandler(404)
def valid_error(error):
    return 'This page does not exist', 404