from flask import Flask, flash, render_template, request, redirect

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register", 
           methods=["POST"])
def register():
    error = None

    if not request.form["username"] or not request.form["pass"] or not request.form["confirm"]:
        error = "Please fill out the details"
        return render_template("index.html", error=error)
    if request.form.get("pass") != request.form.get("confirm"):
        error = "Passwords do not match!"
        return render_template("index.html", error=error)
    flash("Successfully registered!")
    return redirect("/")
