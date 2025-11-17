from flask import Flask, render_template, request
from datetime import datetime


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html.jinja')


@app.route('/characters', methods=['GET', 'POST'])
def characters():
    characterName = ''
    heroClass= ''
    if request.method=='POST':
        characterName = request.form.get('name')
        heroClass = request.form.get('heroclass')
    return render_template('characters.html', characterName=characterName,
    heroClass=heroClass)