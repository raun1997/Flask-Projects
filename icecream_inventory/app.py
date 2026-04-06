from flask import Flask, render_template, request

app = Flask(__name__)

# icecreams = ['Kwality Wall\'s Belgian Chocolate Magnum', 
#             'Baskin Robins Very Strawberry Ice Cup']

icecreams = [
   {"name":"Kwality Wall's Belgian Chocolate Magnum", "img":"https://rukmini1.flixcart.com/image/300/300/xif0q/ice-cream/e/n/q/-original-imahesrbyxaqbcje.jpeg"},
   {"name":"Kwality Wall's Belgian Chocolate Magnum", "img":"https://rukmini1.flixcart.com/image/300/300/xif0q/ice-cream/e/n/q/-original-imahesrbyxaqbcje.jpeg"}
   ]

@app.route("/")
def index():
   return render_template("index.html", icecreams=icecreams)