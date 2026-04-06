from flask import Flask, render_template, request

app = Flask(__name__)

# icecreams = ['Kwality Wall\'s Belgian Chocolate Magnum', 
#             'Baskin Robins Very Strawberry Ice Cup']

icecreams = [
   {"name":"Kwality Wall's Belgian Chocolate Magnum", "img":"https://cdn.grofers.com/cdn-cgi/image/f=auto,fit=scale-down,q=70,metadata=none,w=180/da/cms-assets/cms/product/a5f2160c-815d-4ca0-97f0-a85798dd6e63.png"},
   {"name":"Kwality Wall's Belgian Chocolate Magnum", "img":"https://cdn.grofers.com/cdn-cgi/image/f=auto,fit=scale-down,q=70,metadata=none,w=360/da/cms-assets/cms/product/ddf5f7b6-6be5-4f07-91a7-c2f70ba7f3e4.png"}
   ]

@app.route("/")
def index():
   return render_template("index.html", icecreams=icecreams)