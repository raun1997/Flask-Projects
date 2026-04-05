from flask import Flask, redirect, render_template, request, session
from flask_session import Session

# configure app
app = Flask(__name__)

# configure session
app.config["SESSION_PERMANENT"] = False     # Sessions expire when the browser is closed
app.config["SESSION_TYPE"] = "filesystem"    # Store session data in files
# initialize flask session
Session(app)

@app.route('/')
def home():
    return render_template("index.html",
                                 name=session.get("name"))

@app.route("/login", 
           methods=["GET", "POST"])
def login():
    # POST: the user has clicked on the login button 
    if request.method == "POST":
        # store the username in the session
        session["name"] = request.form.get("name")
        return redirect("/")
    # GET: the user is just visiting the site
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()   # session is just a python dict 
    return redirect("/")