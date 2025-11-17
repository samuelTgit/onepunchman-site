from flask import Flask, render_template
from datetime import datetime


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html.jinja')


@app.route('/characters')
def characters():
    return render_template('characters.html')