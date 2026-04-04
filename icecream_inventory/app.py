from flask import Flask, render_template, request

app = Flask(__name__)

flavours = ['Flavour 1', 
            'Flavour 2']

@app.route("/")
def index():
   return render_template("index.html", flavours=flavours)