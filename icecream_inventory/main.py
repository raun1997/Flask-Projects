from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
db = SQLAlchemy(app)

class Icecream(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    flavour = db.Column(db.String(length=30), nullable=False)

    def __repr__(self):
        return f'Item {self.name}'


@app.route('/')
@app.route('/home')
def home_page():
    return "Hi"

@app.route('/icecreams')
def icecream_page():
    items = Icecream.query.all()
    return render_template('shop.html', items=items)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)