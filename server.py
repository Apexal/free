from flask import Flask, escape, request, render_template
from parsing import get_periods
import json

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/events')
def get_events():
    crns = request.args.get('crns', '').split(',')
    periods = list(map(lambda p: p.as_fullcalendar_event(), get_periods('202001', crns)))
    return json.dumps(periods)