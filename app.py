from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///heroes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Hero(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    hero_class = db.Column(db.String(50), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('index.html.jinja')

@app.route('/characters', methods=['GET', 'POST'])
def characters():
    if request.method == 'POST':
        characterName = request.form.get('name')
        heroClass = request.form.get('heroclass')

        try:
            new_hero = Hero(name=characterName, hero_class=heroClass)
            db.session.add(new_hero)
            db.session.commit()
            return redirect('/admin_characters')
        except:
            db.session.rollback()
            return "Error saving hero to database"

    return render_template('characters.html')

@app.route('/admin_characters')
def admin_characters():
    heroes = Hero.query.order_by(Hero.timestamp.desc()).all()
    return render_template('admin_characters.html', heroes=heroes)
if __name__ == '__main__':
    app.run(debug=True)
    