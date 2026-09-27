from flask import Flask, render_template, abort

app = Flask(__name__)


products = [

    {
        "id": 1,
        "name": "Gaming Mouse",
        "price": 799,
        "old_price": 1199,
        "rating": 5,
        "discount": "33% OFF",
        "category": "Gaming",
        "emoji": "🖱️",
        "store": "Amazon",
        "link": "https://www.amazon.in/",
        "description": "A comfortable gaming mouse suitable for gaming, school work and everyday computer use."
    },

    {
        "id": 2,
        "name": "Wireless Headphones",
        "price": 1499,
        "old_price": 1999,
        "rating": 4,
        "discount": "25% OFF",
        "category": "Electronics",
        "emoji": "🎧",
        "store": "Flipkart",
        "link": "https://www.flipkart.com/",
        "description": "Wireless headphones designed for music, videos, gaming and everyday use."
    },

    {
        "id": 3,
        "name": "Gaming Keyboard",
        "price": 999,
        "old_price": 1499,
        "rating": 5,
        "discount": "33% OFF",
        "category": "Gaming",
        "emoji": "⌨️",
        "store": "Amazon",
        "link": "https://www.amazon.in/",
        "description": "A gaming keyboard with a comfortable layout for gaming, typing and everyday computer use."
    }

]


@app.route("/")
def home():

    return render_template(
        "index.html",
        products=products
    )


@app.route("/product/<int:product_id>")
def product_page(product_id):

    product = None

    for item in products:

        if item["id"] == product_id:
            product = item
            break

    if product is None:
        abort(404)

    return render_template(
        "product.html",
        product=product
    )


if __name__ == "__main__":
    app.run(debug=True)