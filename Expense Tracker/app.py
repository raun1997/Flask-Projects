from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

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
    title = db.Column(db.String(10), nullable=False)
    category = db.Column(db.String(10), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return self.title

with app.app_context():
    db.create_all()

@app.route("/")
def index():
    expenses = Expense.query.all()
    total = sum([e.amount for e in expenses])
    return render_template("index.html", expenses=expenses, total=total)

@app.route("/add", methods=["GET", "POST"])
def add_expense():
    if request.method == "POST":

        title = request.form.get("title")
        category = request.form.get("category")
        amount = request.form.get("amount")
        date = request.form.get("date")
        # converting the date string object to python datetime object
        dateobj = datetime.strptime(date, "%Y-%m-%d").date()

        expense = Expense(
            title = title,
            category = category,
            amount = amount,
            date = dateobj)

        db.session.add(expense)
        db.session.commit()
        return redirect("/")
    
    return render_template("add.html")

@app.route("/delete/<int:id>")
def delete_expense(id):
    expense = Expense.query.get(id)

    if expense:
        db.session.delete(expense)
        db.session.commit()
        return redirect("/")


if __name__=="__main__":
    app.run(debug=True)