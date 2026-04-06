from flask import Flask, render_template, request, session, redirect
from flask_session import Session

# configure app
app = Flask(__name__)

# configure session
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

icecreams = [
   {"id":1, "name":"Kwality Wall's Belgian Chocolate Magnum", "img":"https://cdn.grofers.com/cdn-cgi/image/f=auto,fit=scale-down,q=70,metadata=none,w=180/da/cms-assets/cms/product/a5f2160c-815d-4ca0-97f0-a85798dd6e63.png"},
   {"id":2, "name":"Kwality Wall's Belgian Chocolate Magnum", "img":"https://cdn.grofers.com/cdn-cgi/image/f=auto,fit=scale-down,q=70,metadata=none,w=360/da/cms-assets/cms/product/ddf5f7b6-6be5-4f07-91a7-c2f70ba7f3e4.png"}
   ]

@app.route("/")
def index():
   return render_template("index.html", icecreams=icecreams)

@app.route("/cart", methods=["GET", "POST"])
def cart():
   cart_items = []

   if "cart" not in session:
      session["cart"] = []
   
   # the user has clicked on BUY button
   if request.method == "POST":
      icecream_id = int(request.form.get("icecream_id"))    # fetches the id of the icecream the user wants to order
      session["cart"].append(icecream_id)          # adds (appends) the icecream to the user's cart (list)
      
      for icecream in icecreams:        # iterate through the ice cream list
         if icecream["id"] in session["cart"]:
            cart_items.append(icecream)
      
      return render_template("cart.html", cart=cart_items)


