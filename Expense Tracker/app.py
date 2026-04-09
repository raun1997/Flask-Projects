from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///expensetracker.db"
# initialize the app
db = SQLAlchemy(app)

# each table in the database needs a class to be created for it
# db.Model is required - don't change it
# identify all columns by name and data type
# create the model
class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(10), nullable=False, unique=True)
    category = db.Column(db.String(10), nullable=False, unique=True)
    amount = db.Column(db.Float, nullable=False, unique=True)
    date = db.Column(db.Date, nullable=False)

with app.app_context():
    db.create_all()

@app.route("/")
def index():
    expenses = db.session.execute(db.select(Expense)).scalars()
    return render_template("index.html", expenses=expenses)

@app.route("/add", methods=["GET", "POST"])
def add_expense():
    if request.method == "POST":
        expense = Expense(
            title = request.form.get("title"),
            category = request.form.get("category"),
            amount = request.form.get("amount"),
            date = request.form.get("date"))

        db.session.add(expense)
        db.session.commit()
        return redirect("/")
    
    return render_template("add.html")


if __name__=="__main__":
    app.run(debug=True)