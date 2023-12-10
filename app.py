# app.py

from flask import Flask

# routes
from routes.index import index_bp
from routes.search import search_bp

# fetches
from fetches.fetch_index import fetch_index_bp
from fetches.fetch_customer import fetch_customer_bp
from fetches.fetch_product import fetch_product_bp

# Initialize Flask
app = Flask(
    __name__, 
    static_folder="static", 
    static_url_path="/static"
)

# register routes
app.register_blueprint(index_bp)
app.register_blueprint(search_bp)

# register fetchs
app.register_blueprint(fetch_index_bp)
app.register_blueprint(fetch_customer_bp)
app.register_blueprint(fetch_product_bp)

if __name__ == "__main__":
    app.run(debug=True)