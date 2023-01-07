from flask import Blueprint
from datetime import datetime
import requests

app1 = Blueprint('app1',__name__)

@app1.route('/time')
def time():
    now = str(datetime.now().isoformat('#'))
    return f'<center><strong><font size="10" color="red">{now}</font></strong></center>'

@app1.route('/quote')
def quote():
    r = requests.get('https://api.kanye.rest')
    return f'<center><font size="5" face="fantasy">{r.text[9:-1]}</font></center>'