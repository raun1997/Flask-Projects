from flask import Flask, request, render_template, redirect, flash

app = Flask(__name__)

BIRTHDAYS = {}

@app.route("/")
def index():
    return render_template("index.html",
                           birthdays=BIRTHDAYS)

@app.route("/add_birthday", methods=["POST"])
def add_birthday():
    name = request.form.get("name")
    month = request.form.get("month")
    day = request.form.get("day")

    if not name or not month or not day:
        return render_template("failure.html")
    
    BIRTHDAYS[name] = "/".join([month, day])

    return redirect("/")

if __name__=="__main__":
    app.run(host="0.0.0.0", port=8080, debug=True, use_reloader=True)
