from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# # request.session
app.add_middleware(SessionMiddleware, secret_key="secret123")

templates = Jinja2Templates(directory="templates")

products = [
   {"id": 1, "name": "ZOUK Vegan Leather Women's", "img": "https://th.bing.com/th/id/OIP.mxl1WkxqON8ZxtGZOvi-XgHaHa?w=189&h=189&c=7&r=0&o=7&dpr=1.5&pid=1.7&rm=3", "price": 1500},
   {"id": 2, "name": "Blue Saree", "img": "https://via.placeholder.com/200", "price": 2500},
   {"id": 3, "name": "Nermosa Women Printed Anarkali Kurta and Pant Set with Dupatta", "img": "https://m.media-amazon.com/images/I/71l2sZoikXL._SY879_.jpg", " price": 798},
   {"id": 4, "name": "T-Strap Sandals Chevron Ankle Strap Flats ", "img": "https://m.media-amazon.com/images/I/51+tM4POjEL._SY695_.jpg", "price": 374},
   {"id": 5, "name": "Campus Women Ogl-13 Sneakers", "img": "https://m.media-amazon.com/images/I/61-CyJbM7SL._SY695_.jpg", "price": 879},
   {"id": 6, "name": "BlissClub Ultimate Flare Pants Lite Regular for Women Upto 5'4 ft", "img": "https://m.media-amazon.com/images/I/41-MeW+9SQL._SX679_.jpg", "price": 999},
   {"id": 7, "name": "Women Casual Summer co ords Set Track ", "img": "https://m.media-amazon.com/images/I/51YlduFXCqL._SY879_.jpg", "price": 2500},
   {"id": 8, "name": "Generic Women Crop Top", "img": "https://m.media-amazon.com/images/I/71i2P-zEBGL._SX679_.jpg", "price": 245},
   {"id": 9, "name": "Peora Velvet Silk Thread Kundan Studded Chuda Bangles", "img": "https://m.media-amazon.com/images/I/91Zou9-6LzL._SY695_.jpg", "price": 962},
   {"id": 10, "name": "KEYMAX Alloy Brass Gold Jewellery Set ", "img": "https://m.media-amazon.com/images/I/61NfNr8IG1L._SY695_.jpg", "price": 466},
   {"id": 11, "name": "MEENAZ Peacock Big Round Jhumkas ", "img": "https://m.media-amazon.com/images/I/9130JNNtyBL._SY695_.jpg", "price": 260},
   {"id": 12, "name": "Nail Polish (Baby Pink) Glossy", "img": "https://m.media-amazon.com/images/I/71bevTSswkL._SX679_.jpg", "price": 199},
   {"id": 13, "name": " Hair Straightener with Ceramic Coated Plates & Curler Combo ", "img": "https://via.placeholder.com/200", "price": 2500},
   {"id": 14, "name": " Hair Styling Brand -Hair Dryer", "img": "https://m.media-amazon.com/images/I/51FGbb3EbgL._SX679_.jpg", "price": 799},
   {"id": 15, "name": "Women, Hair Straightener with Ceramic Coated Plates", "img": "https://m.media-amazon.com/images/I/61mUh0kQdML._SX679_.jpg", "price": 2049},
   {"id": 16, "name": "Deconstruct Gel Sunscreen for Oily skin SPF 50 PA++++ |100%", "img": "https://m.media-amazon.com/images/I/41jGahkFZZL._SX679_.jpg", "price": 219},
   {"id": 17, "name": "Lakme Forever Matte Lipstick, Waterproof", "img": "https://m.media-amazon.com/images/I/51xqGNcXqDL._SX679_.jpg", "price": 262},
   {"id": 18, "name": "Eyeliner - Matte Finish, Light Weight", "img": "https://m.media-amazon.com/images/I/41IXUBMQICL._AC_UL480_FMwebp_QL65_.jpg", "price": 2500}
]

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse(
        name="index.html",
        request=request,
        context={"products":products}
    )

@app.api_route("/cart", methods=["GET", "POST"], response_class=HTMLResponse)
async def cart(request: Request):
    cart_items = []

    if "cart" not in request.session:
        request.session["cart"] = []
    
    # the user has clicked on BUY button
    if request.method == "POST":
        form = await request.form()
        product_id = int(form.get("product_id"))    # fetches the id of the icecream the user wants to order
        request.session["cart"].append(product_id)          # adds (appends) the icecream to the user's cart (list)
        
        for p in products:        # iterate through the ice cream list
            if p["id"] in request.session["cart"]:
                cart_items.append(p)

        return templates.TemplateResponse(
            name="cart.html",
            request=request,
            context={"cart": cart_items}
        )