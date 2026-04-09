from flask import Flask, render_template, request, redirect, g
import sqlite3          # for persistent storage

DATABASE = 'expensetracker.db'

# configure app
app = Flask(__name__)
app.secret_key = "bqed6xgwq66_($%$!Vjhb"

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        cur = db.cursor()
        cur.execute("SELECT * FROM expenses")
        expenses = cur.fetchall()
        return expenses 

# Create DB
def init_db():
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            amount REAL,
            category TEXT
        )
    """)
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect("expensetracker.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM expenses")
    data = cur.fetchall()
    conn.close()

    total = sum([row[2] for row in data])

    return render_template("index.html", expenses=data, total=total)

# @app.route("/add", methods=["GET", "POST"])
# def add():
#     if request.method == 'POST':
#         name = request.form.get("name")
#         amount = request.form.get("amount")
#         category = request.form.get("category")

#         conn = sqlite3.connect("expensetracker.db")
#         cur = conn.cursor()
#         cur.executemany(
#         "INSERT INTO expenses (title, amount, category) VALUES (?, ?, ?)",(name, amount, category))
#         conn.commit()
#         conn.close()
#         return redirect("/")
    
#     else:
#         return render_template("add.html")


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    conn = sqlite3.connect("expensetracker.db")
    cur = conn.cursor()

    if request.method == 'POST':
        title = request.form['title']
        amount = request.form['amount']
        category = request.form['category']

        cur.execute("UPDATE expenses SET title=?, amount=?, category=? WHERE id=?",
                    (title, amount, category, id))
        conn.commit()
        conn.close()
        return redirect('/')

    cur.execute("SELECT * FROM expenses WHERE id=?", (id,))
    expense = cur.fetchone()
    conn.close()

    return render_template("edit.html", expense=expense)