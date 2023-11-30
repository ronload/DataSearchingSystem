from flask import Flask, render_template
from flask import request

app = Flask(
    __name__, 
    static_folder="static", 
    static_url_path="/static"
)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search_CustomerInfo")
def search_customer_info():
    return render_template("search_CustomerInfo.html")

@app.route("/search_ProductInfo")
def search_product_info():
    return render_template("search_ProductInfo.html")

@app.route("/search_OrderInfo")
def search_order_info():
    return render_template("search_OrderInfo.html")

@app.route("/search_CartInfo")
def search_cart_info():
    return render_template("search_CartInfo.html")

if __name__ == "__main__":
    app.run(debug=True)